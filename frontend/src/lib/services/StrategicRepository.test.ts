import { describe, it, expect, beforeEach } from 'vitest';
import { StrategicRepository, DataProvider } from './StrategicRepository';

describe('StrategicRepository', () => {
  beforeEach(() => {
    StrategicRepository.resetInstance();
  });

  it('returns default mocked targets for a quarter', async () => {
    const repo = StrategicRepository.getInstance();
    const targets = await repo.fetchTargets('2025-Q1');
    expect(targets.finance_arr).toBe(1000000);
    expect(targets.process_uptime).toBe(99.0);
    expect(targets.customer_csat).toBe(95);
  });

  it('returns default mocked analytics', async () => {
    const repo = StrategicRepository.getInstance();
    const analytics = await repo.fetchAnalytics();
    expect(analytics.process_uptime).toBe(99.5);
    expect(analytics.finance_arr).toBe(950000);
  });

  it('returns default SRE telemetry with endpoints', async () => {
    const repo = StrategicRepository.getInstance();
    const telemetry = await repo.fetchSreTelemetry();
    expect(telemetry.global_uptime).toBeGreaterThan(99);
    expect(telemetry.endpoints.length).toBeGreaterThan(0);
    expect(telemetry.endpoints[0]).toHaveProperty('name');
  });

  it('allows injecting a custom provider', async () => {
    const customProvider: DataProvider = {
      fetchTargets: async () => ({ custom_target: 42 }),
      fetchAnalytics: async () => ({ custom_target: 40 }),
      fetchFinanceAnalytics: async () => ({ arr_total: 123 }),
      fetchSreTelemetry: async () => ({
        global_uptime: 99.9,
        regional_status: 'ok',
        endpoints: [],
      }),
    };

    const repo = StrategicRepository.getInstance(customProvider);
    const targets = await repo.fetchTargets('2025-Q1');
    expect(targets.custom_target).toBe(42);
    const analytics = await repo.fetchAnalytics();
    expect(analytics.custom_target).toBe(40);
  });

  it('returns deterministic historical data shape', async () => {
    const repo = StrategicRepository.getInstance();
    const history = await repo.fetchHistoricalData('finance_arr', 6);
    expect(history).toHaveLength(6);
    expect(history[0]).toHaveProperty('date');
    expect(history[0]).toHaveProperty('value');
  });
});
