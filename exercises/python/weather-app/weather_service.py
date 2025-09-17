"""
Weather Service Module with OpenWeatherMap API Integration
Implements best practices from OpenWeatherMap API documentation
"""
import time
import logging
from typing import Dict, Optional, Tuple
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Configure logging
logger = logging.getLogger(__name__)


class WeatherAPIError(Exception):
    """Custom exception for weather API errors"""
    def __init__(self, message: str, code: int = None, parameters: list = None):
        super().__init__(message)
        self.code = code
        self.parameters = parameters


class WeatherService:
    """
    Service class for OpenWeatherMap API interactions
    Implements proper error handling and retry logic as per API documentation
    """

    # API endpoints
    GEOCODING_ENDPOINT = "http://api.openweathermap.org/geo/1.0/direct"
    ONECALL_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"

    # Retry configuration for 5xx errors (as recommended in docs)
    MAX_RETRIES = 3
    RETRY_BACKOFF = 1  # seconds

    def __init__(self, api_key: str):
        """Initialize weather service with API key"""
        self.api_key = api_key
        self.session = self._create_session()

    def _create_session(self) -> requests.Session:
        """
        Create a requests session with retry logic for 5xx errors
        As per API docs: "Retry the request and contact support"
        """
        session = requests.Session()
        retry = Retry(
            total=self.MAX_RETRIES,
            backoff_factor=self.RETRY_BACKOFF,
            status_forcelist=[500, 502, 503, 504],  # 5xx server errors
            allowed_methods=["GET"]
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session

    def _handle_api_error(self, response: requests.Response, endpoint: str):
        """
        Handle API errors according to OpenWeatherMap error structure

        Error codes from documentation:
        - 400: Bad Request (missing/incorrect parameters)
        - 401: Unauthorized (invalid API key)
        - 404: Not Found (data doesn't exist)
        - 429: Too Many Requests (quota exceeded)
        - 5xx: Server errors (should retry)
        """
        try:
            error_data = response.json()
            code = error_data.get('cod')
            message = error_data.get('message', 'Unknown error')
            parameters = error_data.get('parameters', [])

            # Log the error for debugging
            logger.error(f"API Error on {endpoint}: Code {code}, Message: {message}")

            # Handle specific error codes
            if code == 401:
                raise WeatherAPIError(
                    "Invalid API key. Please check your OpenWeatherMap API key.",
                    code=401
                )
            elif code == 404:
                raise WeatherAPIError(
                    "Weather data not found for the specified location.",
                    code=404
                )
            elif code == 429:
                raise WeatherAPIError(
                    "API rate limit exceeded. Please try again later.",
                    code=429
                )
            elif code == 400:
                param_str = ", ".join(parameters) if parameters else "unknown"
                raise WeatherAPIError(
                    f"Invalid request parameters: {param_str}",
                    code=400,
                    parameters=parameters
                )
            else:
                raise WeatherAPIError(message, code=code)

        except (KeyError, ValueError):
            # If response isn't valid JSON, raise generic error
            raise WeatherAPIError(
                f"Server error: {response.status_code}",
                code=response.status_code
            )

    def get_coordinates(self, city_query: str) -> Tuple[float, float, str]:
        """
        Get coordinates for a city using Geocoding API

        Returns:
            Tuple of (latitude, longitude, location_name)

        Raises:
            WeatherAPIError: If geocoding fails
        """
        params = {
            "q": city_query,
            "appid": self.api_key,
            "limit": 3
        }

        try:
            response = self.session.get(self.GEOCODING_ENDPOINT, params=params)

            # Check for HTTP errors
            if response.status_code != 200:
                self._handle_api_error(response, "Geocoding")

            location_data = response.json()

            # Check if we got results
            if not location_data:
                raise WeatherAPIError(
                    f"City '{city_query}' not found. Please check the spelling.",
                    code=404
                )

            # Return first result
            first_result = location_data[0]
            location_name = first_result.get('name', city_query)
            if 'state' in first_result:
                location_name += f", {first_result['state']}"
            if 'country' in first_result:
                location_name += f", {first_result['country']}"

            return (
                first_result['lat'],
                first_result['lon'],
                location_name
            )

        except requests.exceptions.RequestException as e:
            logger.error(f"Network error during geocoding: {e}")
            raise WeatherAPIError(f"Network error: Unable to reach weather service")

    def get_weather_data(self, lat: float, lon: float) -> Dict:
        """
        Get weather data using One Call API 3.0

        Returns:
            Dictionary with weather data

        Raises:
            WeatherAPIError: If weather data fetch fails
        """
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key,
            "units": "metric",
            "exclude": "minutely,alerts"  # Exclude data we don't need
        }

        try:
            response = self.session.get(self.ONECALL_ENDPOINT, params=params)

            # Check for HTTP errors
            if response.status_code != 200:
                # For 401 errors, provide specific guidance about API 3.0
                if response.status_code == 401:
                    raise WeatherAPIError(
                        "API key not authorized for One Call API 3.0. "
                        "Please ensure you have subscribed to the One Call API 3.0 plan.",
                        code=401
                    )
                self._handle_api_error(response, "One Call API")

            weather_data = response.json()

            # Validate we have required fields
            required_fields = ['current', 'daily']
            for field in required_fields:
                if field not in weather_data:
                    raise WeatherAPIError(
                        f"Incomplete weather data received: missing {field}",
                        code=500
                    )

            return weather_data

        except requests.exceptions.Timeout:
            logger.error("Timeout while fetching weather data")
            raise WeatherAPIError("Request timed out. Please try again.")
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error during weather fetch: {e}")
            raise WeatherAPIError(f"Network error: Unable to reach weather service")

    def process_weather_response(self, weather_data: Dict) -> Dict:
        """
        Process and validate weather API response
        Returns cleaned data ready for display
        """
        try:
            current = weather_data['current']
            daily = weather_data['daily']

            # Extract current weather with validation
            processed_data = {
                'current_temp': round(current.get('temp', 0)),
                'current_weather': current.get('weather', [{}])[0].get('main', 'Unknown'),
                'wind_speed': current.get('wind_speed', 0),
                'humidity': current.get('humidity', 0),
                'feels_like': round(current.get('feels_like', 0)),
                'uvi': current.get('uvi', 0),
                'visibility': current.get('visibility', 10000) / 1000,  # Convert to km
            }

            # Process daily forecast
            if daily and len(daily) > 0:
                today = daily[0]
                processed_data['min_temp'] = round(today.get('temp', {}).get('min', 0))
                processed_data['max_temp'] = round(today.get('temp', {}).get('max', 0))

                # Get 5-day forecast
                processed_data['five_day_temps'] = []
                processed_data['five_day_weather'] = []

                for day in daily[:5]:
                    temp = day.get('temp', {})
                    processed_data['five_day_temps'].append(
                        round(temp.get('day', 0))
                    )
                    weather = day.get('weather', [{}])[0]
                    processed_data['five_day_weather'].append(
                        weather.get('main', 'Unknown')
                    )

                # Add AI summary if available (new in API 3.0)
                if 'summary' in daily[0]:
                    processed_data['daily_summary'] = daily[0]['summary']

            return processed_data

        except (KeyError, IndexError, TypeError) as e:
            logger.error(f"Error processing weather data: {e}")
            raise WeatherAPIError(
                "Invalid weather data format received from API",
                code=500
            )

    def get_weather_for_city(self, city_query: str) -> Tuple[Dict, str]:
        """
        Complete workflow to get weather for a city

        Returns:
            Tuple of (weather_data, location_display_name)
        """
        # Get coordinates
        lat, lon, location_name = self.get_coordinates(city_query)

        # Get weather data
        weather_data = self.get_weather_data(lat, lon)

        # Process response
        processed_data = self.process_weather_response(weather_data)

        return processed_data, location_name