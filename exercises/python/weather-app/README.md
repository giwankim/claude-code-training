# Weather App

A modern Flask-based weather application that provides real-time weather data and 5-day forecasts using the OpenWeatherMap API 3.0. Features a simplistic UI optimized for both mobile and desktop through CSS grid, flexbox, and media queries.

## Recent Improvements (2025)

- **API Migration**: Updated to OpenWeatherMap One Call API 3.0
- **Architecture**: Refactored with modular service layer and proper separation of concerns
- **Error Handling**: Comprehensive error recovery with automatic retry logic
- **US City Search**: Smart detection of US states with automatic country code appending
- **Testing**: Added 70 E2E tests using Playwright across 5 browser environments
- **Documentation**: Added architecture diagrams and comprehensive documentation

## Features

- 🌡️ Real-time weather data with current temperature, humidity, wind speed
- 📅 5-day weather forecast with daily temperatures
- 🗺️ Smart US city search (e.g., "Austin, TX" automatically becomes "Austin, TX, US")
- 🌍 Global city search with geocoding
- 📱 Responsive design for mobile and desktop
- ⚡ Robust error handling with user-friendly messages
- 🔄 Automatic retry logic for server errors

## Screenshots (Desktop)
<img src="/screenshots/weather_app_desktop_home_page_screenshot.png">
<img src="/screenshots/weather_app_desktop_forecast_page_screenshot.png">
<img src="/screenshots/weather_app_desktop_error_page_screenshot.png">

## Screenshots (Mobile)
<img src="/screenshots/weather_app_iphone_forecast_page_screenshot.png" style="width:400px;"> <img src="/screenshots/weather_app_iphone_home_page_screenshot.png" style="width:400px;">

## Quick Start

### Prerequisites
- Python 3.11+
- OpenWeatherMap API key (One Call API 3.0 subscription)
- Node.js (for running tests)

### Installation

1. Clone the repository and navigate to the weather app:
```bash
cd exercises/python/weather-app
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Create .env file with your API key
echo "OWM_API_KEY=your_api_key_here" > .env
```

5. Run the application:
```bash
python main.py
```

The app will be available at `http://localhost:5001`

## Architecture

The application now follows a modular architecture:
- `main.py` - Flask routes and application logic
- `weather_service.py` - OpenWeatherMap API integration with error handling
- `templates/` - Jinja2 HTML templates
- `static/` - CSS and image assets
- `tests/` - Playwright E2E tests

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed system design and diagrams.

## Testing

Run the comprehensive E2E test suite:
```bash
npm install  # First time only
npm test     # Run all tests
npm run test:report  # View HTML report
```

## Original Author's Reflection
Building a Python project from scratch without relying on a tutorial taught me a lot but I was also able to implement the app's key functionality (getting and displaying weather data) due to the work I did with APIs in Angela Yu's Python bootcamp. While deploying this web app, I  learned about git and version control as well as storing API keys as environment variables with .env and the purpose of .gitignore. This project turned out to be frustrating and complicated at times but I learned and grew a lot as a developer by tackling each problem. For instance, I struggled to make this website responsive because I discovered that the Chrome browser tools are not entirely accurate for the mobile view. Hence, when the app was deployed, the website didn't look the way I expected ore desired on mobile. So I switched to a free desktop application called Responsively and it provided views for multiple devices which allowed me to improve my CSS. In addition, I had difficulty positioning my footer at the bottom of my page and had to refer to [this resource](https://stackoverflow.com/questions/51683107/making-a-footer-stay-at-the-bottom-of-the-page-both-in-mobile-view-and-desktop-v) to adjust my CSS accordingly. 

If I were to do this project again, there are a few changes I would make. I would make the website render beautifully on iPads as well by eliminating the space between elements. I also wasn't sure how to add more functionality to this app while maintaining a seamless UI/UX design this time and I would love to do so in the future. E.g. I could add an option for users to specify the country of the city they enter (if multiple countries share the same city name). I could also display the low and high temperatures for each day in the five day forecast instead of only displaying the temperature at noon (which I understand is not an accurate estimate of the overall temperature). It would also be useful to enable location detection to allow the user to get more accurate weather data for their current location by using their precise coordinates instead of relying on the geocoding API provided by OpenWeather.  

## Useful Resources
- [OpenWeather API Documentation](https://openweathermap.org/api/one-call-3)
- [Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [Guide to CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)
- [StackOverflow Post on Centering in CSS Grid](https://stackoverflow.com/questions/45536537/centering-in-css-grid)
- [Youtube video on searching blog posts with Flask](https://www.youtube.com/watch?v=kmtZTo-_gJY)
- [Article on retrieving HTML form data with Flask](https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/)
- [StackOverflow post on building Flask app search bar](https://stackoverflow.com/questions/39960942/flask-app-search-bar)
- [Article on storing API keys as environment variables](https://jonathansoma.com/lede/foundations-2019/classes/apis/keeping-api-keys-secret/)
– [StackOverflow post on storing API keys in Heroku](https://stackoverflow.com/questions/71593743/storing-api-key-in-heroku)
- [Making a footer stay at the bottom of the page both in mobile view and desktop view](https://stackoverflow.com/questions/51683107/making-a-footer-stay-at-the-bottom-of-the-page-both-in-mobile-view-and-desktop-v)

## Image Credit
- [Home page background image](https://unsplash.com/photos/2KXEb_8G5vo)
- [Error page desktop background image](https://unsplash.com/photos/U-Kty6HxcQc)

### Icons 
- <a target="_blank" href="https://icons8.com/icon/pLiaaoa41R9n/wind">Wind</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/37802/thermometer">Thermometer</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/99328/clouds">Clouds</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/101829/rain">Rain</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/67657/fog">Fog</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/hXkspV0LTEoE/snow">Snow</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/G3xS4dQTvswX/rainy-weather">Rainy Weather</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/101843/storm">Storm</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/59878/search">Search</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/39789/chevron-left">Chevron Left</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/99362/summer">Summer</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/akbaie9da2Be/tornado">Tornado</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
