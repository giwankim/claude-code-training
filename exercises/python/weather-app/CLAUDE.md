# Weather App - Claude Code Context

## Project Overview
Flask-based weather application using OpenWeatherMap API 3.0. Originally created as a learning project, now enhanced with production-ready features including comprehensive error handling, E2E testing, and architectural improvements.

## Recent Session Summary (2025)
- Migrated from OpenWeatherMap API 2.5 to 3.0 (One Call API)
- Refactored architecture with `weather_service.py` module
- Added comprehensive error handling following API best practices
- Enhanced US city search with automatic state detection
- Created 70 Playwright E2E tests across 5 browsers
- Added architecture documentation with Mermaid diagrams

## Key Components

### Core Files
- `main.py` - Flask application with routes and error handling
- `weather_service.py` - API integration with retry logic and error recovery
- `templates/` - Jinja2 templates (index.html, city.html, error.html)
- `static/` - CSS styles and weather icons
- `tests/weather-app.spec.js` - Comprehensive E2E test suite
- `ARCHITECTURE.md` - System design documentation with diagrams

### API Configuration
- Uses OpenWeatherMap One Call API 3.0
- API key stored in `.env` as `OWM_API_KEY`
- Implements all documented error codes (400, 401, 404, 429, 5xx)
- Automatic retry logic for server errors
- Session management with connection pooling

### US City Enhancement
The app automatically detects US states and appends ", US" for proper geocoding:
- State abbreviations: "Austin, TX" → "Austin, TX, US"
- Full state names: "Seattle, Washington" → "Seattle, Washington, US"
- Uses sets for O(1) lookup performance

### Testing Infrastructure
- Playwright configuration in `playwright.config.js`
- 70 tests covering all functionality
- Cross-browser testing (Chrome, Firefox, Safari, Mobile)
- Automatic Flask server startup before tests
- HTML report generation

## Current State
- ✅ API 3.0 migration complete
- ✅ Production-ready error handling
- ✅ Comprehensive E2E test coverage
- ✅ Architecture documentation
- ✅ US city search enhancement
- ✅ All tests passing (100% success rate)

## Development Workflow

### Running the App
```bash
source .venv/bin/activate
python main.py  # Runs on port 5001
```

### Running Tests
```bash
npm test  # Run all E2E tests
npm run test:report  # View HTML report
```

### Making Changes
1. Create a branch before significant changes
2. Test with both valid and invalid cities
3. Run E2E tests to ensure nothing breaks
4. Update documentation if adding features

## Known Patterns

### Error Handling Flow
```python
try:
    weather_data, location = weather_service.get_weather_for_city(query)
except WeatherAPIError as e:
    if e.code == 404:  # City not found
    elif e.code == 401:  # API key issue
    elif e.code == 429:  # Rate limited
```

### API Response Structure
- One Call API returns `current`, `daily`, `hourly`, `minutely`
- We exclude `minutely` and `alerts` to reduce payload
- Daily forecast includes AI-generated summaries (when available)

## Future Enhancements to Consider

### High Priority
- [ ] Add caching to reduce API calls for repeated searches
- [ ] Implement user preferences/favorites storage
- [ ] Add weather alerts display
- [ ] Create unit tests for weather_service.py

### Medium Priority
- [ ] Add hourly forecast view
- [ ] Implement location detection
- [ ] Add weather maps integration
- [ ] Create Docker configuration

### Nice to Have
- [ ] Historical weather data
- [ ] Weather comparisons between cities
- [ ] Export weather data to CSV/JSON
- [ ] PWA features for offline access

## Common Issues & Solutions

### "City not found" for US cities
- Already solved with automatic US state detection
- Checks both abbreviations and full state names

### API Rate Limiting
- Free tier: 1,000 calls/day
- Consider implementing Redis caching
- Show clear message to users when rate limited

### Test Failures
- Ensure Flask app is running on port 5001
- Check selectors match current HTML structure
- Verify API key is valid and has 3.0 subscription

## Dependencies

### Python (requirements.txt)
- Flask 2.1.2 with Werkzeug 2.0.2 (compatibility verified)
- requests (with retry adapter)
- python-dotenv
- logging (built-in)

### JavaScript (package.json)
- @playwright/test ^1.40.0

## Environment Variables
```env
OWM_API_KEY=your_api_key_here  # Required
SECRET_KEY=your_secret_key     # Optional (has default)
```

## Git Branches
- `main` - Production branch
- `cc_sep2025` - Current development branch with all improvements

## Design Decisions

### Why One Call API 3.0?
- Single API call vs multiple (efficient)
- Richer data including AI summaries
- Future-proof as 2.5 is deprecated
- Better rate limit economy

### Why Separate Service Module?
- Separation of concerns
- Easier to test
- Reusable for other views/APIs
- Centralizes error handling

### Why Playwright over pytest?
- E2E tests validate user experience
- Cross-browser testing crucial for weather app
- Visual regression capabilities
- Better for UI-heavy applications

## Testing Strategy
- E2E tests for user workflows
- Unit tests for service logic (TODO)
- Manual testing for edge cases
- Performance testing for API calls (TODO)

## Original Credits
- Original author: Rachana Hegde (UI/UX design)
- Weather icons: Icons8
- Background images: Unsplash

## Notes for Future Sessions
- App uses metric units by default
- Port 5001 chosen to avoid conflicts
- Flask debug mode enabled for development
- Backup files (main_original.py, main_improved.py) kept locally but not in git
- Test reports in playwright-report/ (gitignored)