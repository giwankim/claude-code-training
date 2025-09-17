// @ts-check
const { test, expect } = require('@playwright/test');

test.describe('Weather App Homepage', () => {
  test('should display the homepage with search bar', async ({ page }) => {
    await page.goto('/');

    // Check page title
    await expect(page).toHaveTitle(/Weather App/);

    // Check main heading
    const heading = page.locator('h1');
    await expect(heading).toContainText('Weather');

    // Check search bar exists
    const searchInput = page.locator('input[name="search"]');
    await expect(searchInput).toBeVisible();
    await expect(searchInput).toHaveAttribute('placeholder', 'Search for a city');

    // Check search icon
    const searchIcon = page.locator('.search-icon');
    await expect(searchIcon).toBeVisible();
  });

  test('should navigate to weather page on search', async ({ page }) => {
    await page.goto('/');

    // Enter city and submit
    const searchInput = page.locator('input[name="search"]');
    await searchInput.fill('London');
    await searchInput.press('Enter');

    // Should redirect to city weather page
    await expect(page).toHaveURL(/\/London/);

    // City name should be displayed (h1 in city-header)
    const cityName = page.locator('.city-header h1');
    await expect(cityName).toContainText('London');
  });
});

test.describe('Weather Display', () => {
  test('should display weather data for a valid city', async ({ page }) => {
    await page.goto('/');

    // Search for a city
    const searchInput = page.locator('input[name="search"]');
    await searchInput.fill('Paris');
    await searchInput.press('Enter');

    // Wait for weather data to load
    await page.waitForSelector('#current-temp');

    // Check current temperature is displayed
    const currentTemp = page.locator('#current-temp');
    await expect(currentTemp).toBeVisible();
    await expect(currentTemp).toContainText(/\d+ºC/);

    // Check weather sections exist
    const dailyForecast = page.locator('.daily-forecast');
    await expect(dailyForecast).toBeVisible();

    // Check wind speed in forecast text
    const windSpeed = page.locator('.forecast-text').filter({ hasText: 'meter/sec' });
    await expect(windSpeed).toBeVisible();

    // Check temperature range
    const tempRange = page.locator('.forecast-text').filter({ hasText: /\d+° - \d+°/ });
    await expect(tempRange).toBeVisible();
  });

  test('should display 5-day forecast', async ({ page }) => {
    await page.goto('/');

    // Search for a city
    const searchInput = page.locator('input[name="search"]');
    await searchInput.fill('Tokyo');
    await searchInput.press('Enter');

    // Wait for forecast to load
    await page.waitForSelector('.five-day');

    // Check forecast items exist
    const forecastItems = page.locator('.forecast-item');
    await expect(forecastItems).toHaveCount(5);

    // Check each forecast item has required elements
    for (let i = 0; i < 5; i++) {
      const dayItem = forecastItems.nth(i);

      // Check day name exists (first p tag)
      const dayName = dayItem.locator('p').first();
      await expect(dayName).toBeVisible();

      // Check temperature exists (last p tag)
      const dayTemp = dayItem.locator('p').last();
      await expect(dayTemp).toBeVisible();
      await expect(dayTemp).toContainText(/\d+º/);

      // Check weather icon exists
      const weatherIcon = dayItem.locator('.weather-icon');
      await expect(weatherIcon).toBeVisible();
    }
  });

  test('should have a back button that returns to homepage', async ({ page }) => {
    await page.goto('/London');

    // Find and click back button (CHANGE CITY link)
    const backButton = page.locator('.change-button a');
    await expect(backButton).toBeVisible();
    await backButton.click();

    // Should be back on homepage
    await expect(page).toHaveURL('/');
    const searchInput = page.locator('input[name="search"]');
    await expect(searchInput).toBeVisible();
  });
});

test.describe('Error Handling', () => {
  test('should show error page for invalid city', async ({ page }) => {
    await page.goto('/');

    // Search for invalid city
    const searchInput = page.locator('input[name="search"]');
    await searchInput.fill('InvalidCityName12345');
    await searchInput.press('Enter');

    // Should redirect to error page
    await expect(page).toHaveURL(/\/error/);

    // Check error message is displayed
    const errorMessage = page.locator('#error-text');
    await expect(errorMessage).toBeVisible();
    await expect(errorMessage).toContainText(/does not exist|error|not found|invalid/i);

    // Should have a way to go back
    const backLink = page.locator('a[href="/"]');
    await expect(backLink).toBeVisible();
  });

  test('should handle empty search input', async ({ page }) => {
    await page.goto('/');

    // Try to submit empty search
    const searchInput = page.locator('input[name="search"]');
    await searchInput.fill('');
    await searchInput.press('Enter');

    // Should stay on homepage or show validation
    // The exact behavior depends on form validation
    const url = page.url();
    expect(url === 'http://127.0.0.1:5001/' || url.includes('/error')).toBeTruthy();
  });

  test('should handle special characters in search', async ({ page }) => {
    await page.goto('/');

    // Search with special characters
    const searchInput = page.locator('input[name="search"]');
    await searchInput.fill('@#$%^&*');
    await searchInput.press('Enter');

    // Should handle gracefully (either error page or stay on homepage)
    await page.waitForLoadState('networkidle');
    const url = page.url();
    expect(url.includes('/error') || url === 'http://127.0.0.1:5001/').toBeTruthy();
  });
});

test.describe('US City Search Enhancement', () => {
  test('should find US city with state abbreviation', async ({ page }) => {
    await page.goto('/');

    // Search for US city with state abbreviation
    const searchInput = page.locator('input[name="search"]');
    await searchInput.fill('Austin, TX');
    await searchInput.press('Enter');

    // Should successfully display weather
    await page.waitForSelector('#current-temp');
    const cityName = page.locator('.city-header h1');
    await expect(cityName).toContainText('Austin');

    // Temperature should be displayed
    const currentTemp = page.locator('#current-temp');
    await expect(currentTemp).toBeVisible();
    await expect(currentTemp).toContainText(/\d+ºC/);
  });

  test('should find US city with full state name', async ({ page }) => {
    await page.goto('/');

    // Search for US city with full state name
    const searchInput = page.locator('input[name="search"]');
    await searchInput.fill('Seattle, Washington');
    await searchInput.press('Enter');

    // Should successfully display weather
    await page.waitForSelector('#current-temp');
    const cityName = page.locator('.city-header h1');
    await expect(cityName).toContainText('Seattle');

    // Temperature should be displayed
    const currentTemp = page.locator('#current-temp');
    await expect(currentTemp).toBeVisible();
    await expect(currentTemp).toContainText(/\d+ºC/);
  });

  test('should handle multiple US cities with same name', async ({ page }) => {
    await page.goto('/');

    // Search for Springfield with state (there are many Springfields)
    const searchInput = page.locator('input[name="search"]');
    await searchInput.fill('Springfield, IL');
    await searchInput.press('Enter');

    // Should successfully display weather for Springfield, IL
    await page.waitForSelector('#current-temp');
    const cityName = page.locator('.city-header h1');
    await expect(cityName).toContainText('Springfield');

    // Temperature should be displayed
    const currentTemp = page.locator('#current-temp');
    await expect(currentTemp).toBeVisible();
  });

  test('should still work for international cities', async ({ page }) => {
    await page.goto('/');

    // Search for international city
    const searchInput = page.locator('input[name="search"]');
    await searchInput.fill('Berlin');
    await searchInput.press('Enter');

    // Should successfully display weather
    await page.waitForSelector('#current-temp');
    const cityName = page.locator('.city-header h1');
    await expect(cityName).toContainText('Berlin');

    // Temperature should be displayed
    const currentTemp = page.locator('#current-temp');
    await expect(currentTemp).toBeVisible();
    await expect(currentTemp).toContainText(/\d+ºC/);
  });
});

test.describe('Responsive Design', () => {
  test('should be responsive on mobile devices', async ({ page }) => {
    // Set mobile viewport
    await page.setViewportSize({ width: 375, height: 667 });
    await page.goto('/');

    // Check that search is still accessible
    const searchInput = page.locator('input[name="search"]');
    await expect(searchInput).toBeVisible();

    // Search for a city
    await searchInput.fill('Madrid');
    await searchInput.press('Enter');

    // Weather should display properly on mobile
    await page.waitForSelector('#current-temp');
    const currentTemp = page.locator('#current-temp');
    await expect(currentTemp).toBeVisible();

    // Forecast should still be visible
    const forecastItems = page.locator('.forecast-item');
    const count = await forecastItems.count();
    expect(count).toBeGreaterThan(0);
  });

  test('should work on tablet devices', async ({ page }) => {
    // Set tablet viewport
    await page.setViewportSize({ width: 768, height: 1024 });
    await page.goto('/');

    // Test navigation and search
    const searchInput = page.locator('input[name="search"]');
    await searchInput.fill('Barcelona');
    await searchInput.press('Enter');

    // Verify layout works on tablet
    await page.waitForSelector('#current-temp');
    const cityName = page.locator('.city-header h1');
    await expect(cityName).toBeVisible();

    const forecastSection = page.locator('.five-day');
    await expect(forecastSection).toBeVisible();
  });
});