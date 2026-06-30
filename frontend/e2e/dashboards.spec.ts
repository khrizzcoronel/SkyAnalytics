import { test, expect } from '@playwright/test';

test.describe('Strategic dashboards', () => {
  test.beforeEach(async ({ context }) => {
    await context.addCookies([
      {
        name: 'pb_auth',
        value: 'board-member-token',
        domain: 'localhost',
        path: '/',
      },
    ]);
  });

  test('BSC page renders the title', async ({ page }) => {
    await page.goto('/dashboard/bsc');
    await expect(page.locator('h1')).toContainText('Balanced Scorecard');
  });

  test('Finance page renders ARR metric', async ({ page }) => {
    await page.goto('/dashboard/finance');
    await expect(page.locator('h1')).toContainText('Métricas Financieras');
    await expect(page.locator('text=ARR Consolidado')).toBeVisible();
  });

  test('Engineering page renders SRE health', async ({ page }) => {
    await page.goto('/dashboard/engineering');
    await expect(page.getByRole('heading', { name: 'Salud del Sistema (SRE)' })).toBeVisible();
  });
});
