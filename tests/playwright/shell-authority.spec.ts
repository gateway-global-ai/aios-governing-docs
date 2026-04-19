import { expect, test } from '@playwright/test';

async function rect(locator: Parameters<typeof expect>[0]) {
  return locator.boundingBox();
}

const liveRuntime = !!process.env.AIOS_PLAYWRIGHT_BASE_URL;

test.beforeEach(async ({ page }) => {
  await page.goto('/');
});

test('header and footer remain fixed protected chrome', async ({ page }) => {
  test.skip(liveRuntime, 'fixture-only authority proof');
  const header = page.getByRole('banner', { name: 'AIOS shell header' });
  const footer = page.getByLabel('AIOS shell footer');

  await expect(header).toBeVisible();
  await expect(footer).toBeVisible();

  await expect(header).toHaveCSS('position', 'fixed');
  await expect(footer).toHaveCSS('position', 'fixed');

  const headerBox = await rect(header);
  const footerBox = await rect(footer);

  expect(headerBox).not.toBeNull();
  expect(footerBox).not.toBeNull();

  expect(Math.round(headerBox!.y)).toBe(0);
  expect(Math.round(footerBox!.y + footerBox!.height)).toBe(Math.round(page.viewportSize()!.height));
});

test('header system menu is attached to the header and shell-owned', async ({ page }) => {
  test.skip(liveRuntime, 'fixture-only authority proof');
  const button = page.getByRole('button', { name: 'Open system shell menu' });
  const menu = page.getByLabel('System shell menu panel');
  const header = page.getByRole('banner', { name: 'AIOS shell header' });

  await button.click();
  await expect(menu).toBeVisible();
  await expect(menu).toHaveAttribute('data-menu-zone', 'header_system');
  await expect(menu).toHaveAttribute('data-permission-class', 'shell_system');

  const menuBox = await rect(menu);
  const headerBox = await rect(header);

  expect(menuBox).not.toBeNull();
  expect(headerBox).not.toBeNull();
  expect(menuBox!.y).toBeGreaterThanOrEqual(headerBox!.y + headerBox!.height - 2);
  expect(menuBox!.y).toBeLessThanOrEqual(headerBox!.y + headerBox!.height + 16);
});

test('footer menu stays secondary and user-focused', async ({ page }) => {
  test.skip(liveRuntime, 'fixture-only authority proof');
  const button = page.getByRole('button', { name: 'Open user surface menu' });
  const menu = page.getByLabel('User surface menu panel');
  const footer = page.getByLabel('AIOS shell footer');

  await button.click();
  await expect(menu).toBeVisible();
  await expect(menu).toHaveAttribute('data-menu-zone', 'footer_user');
  await expect(menu).toHaveAttribute('data-permission-class', 'user_surface');
  await expect(menu).toContainText('Knowledge');

  const menuBox = await rect(menu);
  const footerBox = await rect(footer);

  expect(menuBox).not.toBeNull();
  expect(footerBox).not.toBeNull();
  expect(menuBox!.y + menuBox!.height).toBeLessThanOrEqual(footerBox!.y + 2);
});

test('visual proof of shell authority contract', async ({ page }) => {
  test.skip(liveRuntime, 'fixture-only authority proof');
  await expect(page).toHaveScreenshot('shell-authority-idle.png', {
    animations: 'disabled',
    caret: 'hide',
  });
});

test('visual proof of header system menu contract', async ({ page }) => {
  test.skip(liveRuntime, 'fixture-only authority proof');
  await page.getByRole('button', { name: 'Open system shell menu' }).click();
  await expect(page).toHaveScreenshot('shell-authority-header-menu.png', {
    animations: 'disabled',
    caret: 'hide',
  });
});

test('visual proof of footer user menu contract', async ({ page }) => {
  test.skip(liveRuntime, 'fixture-only authority proof');
  await page.getByRole('button', { name: 'Open user surface menu' }).click();
  await expect(page).toHaveScreenshot('shell-authority-footer-menu.png', {
    animations: 'disabled',
    caret: 'hide',
  });
});

test('runtime cue drawer stays cue-only without duplicate settings', async ({ page }) => {
  test.skip(!process.env.AIOS_PLAYWRIGHT_BASE_URL, 'requires live runtime');

  await page.getByRole('button', { name: 'Open audio cue menu' }).click();
  await expect(page.getByText('Audio cue')).toBeVisible();
  await expect(page.getByText('Switch voice route')).toHaveCount(0);
  await expect(page.getByText('Voice settings')).toHaveCount(0);
});

test('runtime voice box opens as four-intent menu', async ({ page }) => {
  test.skip(!process.env.AIOS_PLAYWRIGHT_BASE_URL, 'requires live runtime');

  await page.getByRole('button', { name: 'Open system shell menu' }).click();
  await page.getByRole('button', { name: /Voice control/i }).click();
  await page.getByRole('button', { name: /Voice profiles/i }).click();
  await page.getByRole('button', { name: /Voice Box/i }).click();

  await expect(page.getByText('Voice Box', { exact: true }).first()).toBeVisible();
  await expect(page.locator('button', { hasText: 'View Profiles' }).first()).toBeVisible();
  await expect(page.locator('button', { hasText: 'Create Profile' }).first()).toBeVisible();
  await expect(page.locator('button', { hasText: 'Record Voice' }).first()).toBeVisible();
  await expect(page.locator('button', { hasText: 'Upload Profile' }).first()).toBeVisible();
});

test('runtime voice box record voice renders governed detail surface', async ({ page }) => {
  test.skip(!process.env.AIOS_PLAYWRIGHT_BASE_URL, 'requires live runtime');

  await page.getByRole('button', { name: 'Open system shell menu' }).click();
  await page.getByRole('button', { name: /Voice control/i }).click();
  await page.getByRole('button', { name: /Voice profiles/i }).click();
  await page.getByRole('button', { name: /Voice Box/i }).click();
  await page.getByRole('button', { name: /Record Voice/i }).click();

  await expect(page.locator('label', { hasText: 'Select a profile' })).toBeVisible();
  await expect(page.getByText(/0 \/ 5 recommended/i)).toBeVisible();
  await expect(page.getByText(/Read this aloud/i)).toBeVisible();
  await expect(page.locator('p', { hasText: 'Hold to speak' })).toBeVisible();
});

test('runtime appearance overlay stays top-aligned with intent menu', async ({ page }) => {
  test.skip(!process.env.AIOS_PLAYWRIGHT_BASE_URL, 'requires live runtime');

  const header = page.locator('header[role="banner"]').first();
  await page.getByRole('button', { name: 'Open system shell menu' }).click();
  await page.getByRole('button', { name: /Appearance/i }).click();

  await expect(header).toBeVisible();
  await expect(page.locator('button', { hasText: 'Color Scheme' }).first()).toBeVisible();
  await expect(page.locator('button', { hasText: 'Background Source' }).first()).toBeVisible();

  const headerBox = await rect(header);
  const panelBox = await rect(page.getByRole('heading', { name: 'Color Scheme' }));
  expect(headerBox).not.toBeNull();
  expect(panelBox).not.toBeNull();
  expect(panelBox!.y).toBeGreaterThanOrEqual(headerBox!.height - 2);
});

test('runtime agent identity overlay stays top-aligned with intent menu', async ({ page }) => {
  test.skip(!process.env.AIOS_PLAYWRIGHT_BASE_URL, 'requires live runtime');

  const header = page.locator('header[role="banner"]').first();
  await page.getByRole('button', { name: 'Open system shell menu' }).click();
  await page.getByRole('button', { name: /Governed configuration/i }).click();
  await page.getByRole('button', { name: /Agent Identity/i }).click();

  await expect(header).toBeVisible();
  await expect(page.locator('button', { hasText: 'Agent Identity' }).first()).toBeVisible();
  await expect(page.locator('button', { hasText: 'Desired Outcome' }).first()).toBeVisible();

  const headerBox = await rect(header);
  const panelBox = await rect(page.getByRole('heading', { name: 'Agent Identity' }));
  expect(headerBox).not.toBeNull();
  expect(panelBox).not.toBeNull();
  expect(panelBox!.y).toBeGreaterThanOrEqual(headerBox!.height - 2);
});
