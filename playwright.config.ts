import { defineConfig, devices } from '@playwright/test';

const externalBaseUrl = process.env.AIOS_PLAYWRIGHT_BASE_URL?.trim();
const baseURL = externalBaseUrl || 'http://127.0.0.1:4174';

export default defineConfig({
  testDir: './tests/playwright',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  reporter: [
    ['list'],
    ['html', { outputFolder: 'artifacts/browser_review/report', open: 'never' }],
  ],
  outputDir: 'artifacts/browser_review/results',
  snapshotPathTemplate:
    'artifacts/browser_review/golden/{projectName}/{testFilePath}/{arg}{ext}',
  use: {
    baseURL,
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
    viewport: { width: 1440, height: 900 },
  },
  webServer: externalBaseUrl
    ? undefined
    : {
        command: 'py -3 -m http.server 4174 --bind 127.0.0.1 --directory tests/playwright/fixtures',
        url: 'http://127.0.0.1:4174',
        reuseExistingServer: !process.env.CI,
        stdout: 'ignore',
        stderr: 'pipe',
        timeout: 30000,
      },
  projects: [
    {
      name: 'desktop-chromium',
      use: {
        ...devices['Desktop Chrome'],
        viewport: { width: 1440, height: 900 },
      },
    },
    {
      name: 'mobile-chromium',
      use: {
        ...devices['Pixel 7'],
      },
    },
  ],
});
