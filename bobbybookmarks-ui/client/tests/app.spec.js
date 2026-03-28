import { test, expect } from '@playwright/test';

test.describe('BobbyBookmarks Dashboard UI', () => {
  test('should load the dashboard and display correct header and version', async ({ page }) => {
    await page.goto('http://localhost:5173');
    await expect(page.locator('h1')).toContainText("Bobby's Research Command");
    await expect(page.locator('.version-tag')).toContainText('v0.1.0');
  });

  test('should display all main view navigation buttons', async ({ page }) => {
    await page.goto('http://localhost:5173');
    const buttons = ['Catalog', 'Features', 'Insights', 'Clusters', 'Nebula', 'Peer Review', 'Reports', 'Network', 'Live Feed', 'Mind Map', 'Surprise'];
    for (const btnText of buttons) {
      await expect(page.locator(`.header-actions button:has-text("${btnText}")`)).toBeVisible();
    }
  });

  test('should toggle semantic search mode and update placeholder', async ({ page }) => {
    await page.goto('http://localhost:5173');
    const toggleBtn = page.locator('.search-toggle');
    await expect(toggleBtn).toContainText('Keyword');
    await toggleBtn.click();
    await expect(toggleBtn).toContainText('Semantic');
    
    const searchInput = page.locator('.search-bar input');
    await expect(searchInput).toHaveAttribute('placeholder', /Describe what you're looking for/i);
  });
});
