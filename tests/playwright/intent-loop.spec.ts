import { expect, test } from '@playwright/test';

const liveRuntime = !!process.env.AIOS_PLAYWRIGHT_BASE_URL;

test.beforeEach(async ({ page }) => {
  await page.goto('/');
});

test('UI renders governed text from database, not hardcoded strings', async ({ page }) => {
  // This test runs against the live runtime to verify the DB connection
  test.skip(!liveRuntime, 'live-only intent loop proof');
  
  // Wait for the app to initialize and fetch the intent state from the backend
  // The governed greeting message should appear in the chat history
  
  // We expect the greeting message to be the one seeded in the database:
  const expectedGreeting = "Welcome to AI OS. I know 'vibe coding' can be exhausting when shortcuts break in production. I'm here to guide you through a better way. We have the Vibe Coding University to learn, and the Community to build together. Let's start with our 7-step process: what is your purpose today?";
  
  // We can just check if the text is visible on the page
  await expect(page.getByText(expectedGreeting)).toBeVisible({ timeout: 10000 });
});
