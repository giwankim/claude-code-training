import datetime
import requests
import string
from flask import Flask, render_template, request, redirect, url_for
import os
from dotenv import load_dotenv
load_dotenv()

# One Call API 3.0 endpoint - combines current, minutely, hourly, and daily data
OWM_ONECALL_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
# Geocoding API remains the same
GEOCODING_API_ENDPOINT = "http://api.openweathermap.org/geo/1.0/direct"
api_key = os.getenv("OWM_API_KEY")
# api_key = os.environ.get("OWM_API_KEY")

app = Flask(__name__)


# Display home page and get city name entered into search form
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        city = request.form.get("search")
        return redirect(url_for("get_weather", city=city))
    return render_template("index.html")


# Display weather forecast for specific city using data from OpenWeather API
@app.route("/<city>", methods=["GET", "POST"])
def get_weather(city):
    # Format city name and get current date to display on page
    city_name = string.capwords(city)
    today = datetime.datetime.now()
    current_date = today.strftime("%A, %B %d")

    # List of US state abbreviations and full names
    us_states_abbrev = {
        'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
        'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
        'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
        'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
        'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'DC'
    }

    us_states_full = {
        'alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado',
        'connecticut', 'delaware', 'florida', 'georgia', 'hawaii', 'idaho',
        'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana',
        'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota',
        'mississippi', 'missouri', 'montana', 'nebraska', 'nevada',
        'new hampshire', 'new jersey', 'new mexico', 'new york',
        'north carolina', 'north dakota', 'ohio', 'oklahoma', 'oregon',
        'pennsylvania', 'rhode island', 'south carolina', 'south dakota',
        'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington',
        'west virginia', 'wisconsin', 'wyoming'
    }

    # Check if user entered a US city with state but no country
    # Formats: "City, ST" or "City, State" -> append ", US"
    search_query = city_name
    if ',' in city_name:
        parts = [p.strip() for p in city_name.split(',')]
        # If we have exactly 2 parts (city and state)
        if len(parts) == 2:
            state_part = parts[1]
            # Check for state abbreviation or full state name
            if state_part.upper() in us_states_abbrev or state_part.lower() in us_states_full:
                search_query = f"{parts[0]}, {state_part}, US"
                city_name = f"{parts[0]}, {state_part}"  # Keep display name clean

    # Get latitude and longitude for city
    location_params = {
        "q": search_query,
        "appid": api_key,
        "limit": 3,
    }

    location_response = requests.get(GEOCODING_API_ENDPOINT, params=location_params)
    location_data = location_response.json()

    # Prevent IndexError if user entered a city name with no coordinates by redirecting to error page
    if not location_data:
        return redirect(url_for("error"))
    else:
        lat = location_data[0]['lat']
        lon = location_data[0]['lon']

    # Get One Call API 3.0 data - combines current, hourly, and daily forecasts
    weather_params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric",
        "exclude": "minutely,alerts"  # Exclude data we don't need
    }
    onecall_response = requests.get(OWM_ONECALL_ENDPOINT, weather_params)
    onecall_response.raise_for_status()
    onecall_data = onecall_response.json()

    # Get current weather data from One Call API
    current = onecall_data['current']
    current_temp = round(current['temp'])
    current_weather = current['weather'][0]['main']
    wind_speed = current['wind_speed']

    # Get today's min/max from daily forecast
    today_daily = onecall_data['daily'][0]
    min_temp = round(today_daily['temp']['min'])
    max_temp = round(today_daily['temp']['max'])

    # Get 5-day forecast data from daily array
    # One Call API provides 8 days of daily forecasts
    five_day_temp_list = [round(day['temp']['day']) for day in onecall_data['daily'][:5]]
    five_day_weather_list = [day['weather'][0]['main'] for day in onecall_data['daily'][:5]]

    # Get next four weekdays to show user alongside weather data
    five_day_unformatted = [today, today + datetime.timedelta(days=1), today + datetime.timedelta(days=2),
                            today + datetime.timedelta(days=3), today + datetime.timedelta(days=4)]
    five_day_dates_list = [date.strftime("%a") for date in five_day_unformatted]

    return render_template("city.html", city_name=city_name, current_date=current_date, current_temp=current_temp,
                           current_weather=current_weather, min_temp=min_temp, max_temp=max_temp, wind_speed=wind_speed,
                           five_day_temp_list=five_day_temp_list, five_day_weather_list=five_day_weather_list,
                           five_day_dates_list=five_day_dates_list)


# Display error page for invalid input
@app.route("/error")
def error():
    return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
