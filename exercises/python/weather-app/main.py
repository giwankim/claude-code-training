import datetime
import string
from flask import Flask, render_template, request, redirect, url_for, flash
import os
from dotenv import load_dotenv
import logging
from weather_service import WeatherService, WeatherAPIError

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")

# Initialize weather service
api_key = os.getenv("OWM_API_KEY")
if not api_key:
    raise ValueError("OWM_API_KEY environment variable not set")

weather_service = WeatherService(api_key)

# US states for enhancement
US_STATES_ABBREV = {
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
    'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'DC'
}

US_STATES_FULL = {
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


def enhance_us_city_search(city_name):
    """Enhance US city searches by adding country code when appropriate"""
    if ',' in city_name:
        parts = [p.strip() for p in city_name.split(',')]
        if len(parts) == 2:
            state_part = parts[1]
            if state_part.upper() in US_STATES_ABBREV or state_part.lower() in US_STATES_FULL:
                return f"{parts[0]}, {state_part}, US"
    return city_name


@app.route("/", methods=["GET", "POST"])
def home():
    """Display home page and handle city search"""
    if request.method == "POST":
        city = request.form.get("search")
        if not city:
            flash("Please enter a city name", "warning")
            return render_template("index.html")
        return redirect(url_for("get_weather", city=city))
    return render_template("index.html")


@app.route("/<city>", methods=["GET", "POST"])
def get_weather(city):
    """Display weather forecast for specific city"""
    try:
        # Format city name
        city_name = string.capwords(city)

        # Enhance US city search
        search_query = enhance_us_city_search(city_name)

        # Get weather data using the service
        weather_data, location_name = weather_service.get_weather_for_city(search_query)

        # Get current date
        today = datetime.datetime.now()
        current_date = today.strftime("%A, %B %d")

        # Generate day names for forecast
        five_day_dates_list = [
            (today + datetime.timedelta(days=i)).strftime("%a")
            for i in range(5)
        ]

        # Prepare template data
        template_data = {
            'city_name': location_name,
            'current_date': current_date,
            'current_temp': weather_data['current_temp'],
            'current_weather': weather_data['current_weather'],
            'min_temp': weather_data['min_temp'],
            'max_temp': weather_data['max_temp'],
            'wind_speed': weather_data['wind_speed'],
            'five_day_temp_list': weather_data['five_day_temps'],
            'five_day_weather_list': weather_data['five_day_weather'],
            'five_day_dates_list': five_day_dates_list,
            'humidity': weather_data['humidity'],
            'feels_like': weather_data['feels_like'],
            'visibility': weather_data['visibility'],
            'uvi': weather_data['uvi']
        }

        # Add AI summary if available
        if 'daily_summary' in weather_data:
            template_data['weather_summary'] = weather_data['daily_summary']

        return render_template("city.html", **template_data)

    except WeatherAPIError as e:
        # Log the error
        logger.error(f"Weather API error for city '{city}': {e}")

        # Handle specific error codes
        if e.code == 404:
            flash(f"City '{city}' not found. Please check the spelling and try again.", "error")
        elif e.code == 401:
            flash("Weather service authentication error. Please contact support.", "error")
        elif e.code == 429:
            flash("Too many requests. Please try again in a few minutes.", "warning")
        else:
            flash(f"Weather service error: {str(e)}", "error")

        return redirect(url_for("error"))

    except Exception as e:
        # Catch any unexpected errors
        logger.error(f"Unexpected error for city '{city}': {e}")
        flash("An unexpected error occurred. Please try again later.", "error")
        return redirect(url_for("error"))


@app.route("/error")
def error():
    """Display error page with any flashed messages"""
    return render_template("error.html")


@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template("error.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {e}")
    flash("Internal server error. Please try again later.", "error")
    return render_template("error.html"), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)