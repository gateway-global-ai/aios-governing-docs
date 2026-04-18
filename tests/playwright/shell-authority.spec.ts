import { expect, test } from '@playwright/test';

async function rect(locator: Parameters<typeof expect>[0]) {
  return locator.boundingBox();
}

test.beforeEach(async ({ page }) => {
  await page.goto('/');
});

test('header and footer remain fixed protected chrome', async ({ page }) => {
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
  await expect(page).toHaveScreenshot('shell-authority-idle.png', {
    animations: 'disabled',
    caret: 'hide',
  });
});

test('visual proof of header system menu contract', async ({ page }) => {
  await page.getByRole('button', { name: 'Open system shell menu' }).click();
  await expect(page).toHaveScreenshot('shell-authority-header-menu.png', {
    animations: 'disabled',
    caret: 'hide',
  });
});

test('visual proof of footer user menu contract', async ({ page }) => {
  await page.getByRole('button', { name: 'Open user surface menu' }).click();
  await expect(page).toHaveScreenshot('shell-authority-footer-menu.png', {
    animations: 'disabled',
    caret: 'hide',
  });
});
