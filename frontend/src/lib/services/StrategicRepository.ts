export interface KPI {
  kpi_name: string;
  target_value: number;
  current_value: number;
}

export interface EndpointTelemetry {
  name: string;
  uptime: number;
  traffic: number;
  errors_5xx: number;
}

export interface SreTelemetry {
  global_uptime: number;
  regional_status: string;
  endpoints: EndpointTelemetry[];
}

export interface DataProvider {
  fetchTargets(quarter: string): Promise<Record<string, number>>;
  fetchAnalytics(): Promise<Record<string, number>>;
  fetchFinanceAnalytics(): Promise<Record<string, number>>;
  fetchSreTelemetry(): Promise<SreTelemetry>;
  fetchHistoricalData?(
    kpiName: string,
    months: number
  ): Promise<{ date: string; value: number }[]>;
}

class MockDataProvider implements DataProvider {
  private readonly targets: Record<string, number> = {
    finance_arr: 1000000,
    customer_csat: 95,
    process_uptime: 99.0,
    learning_retention: 90,
  };

  private readonly analytics: Record<string, number> = {
    finance_arr: 950000,
    customer_csat: 98,
    process_uptime: 99.5,
    learning_retention: 85,
  };

  async fetchTargets(): Promise<Record<string, number>> {
    return { ...this.targets };
  }

  async fetchAnalytics(): Promise<Record<string, number>> {
    return { ...this.analytics };
  }

  async fetchFinanceAnalytics(): Promise<Record<string, number>> {
    return {
      arr_total: 1000000,
      ltv_cac_ratio: 3.5,
      gross_margin: 78,
      nrr: 98,
      mrr_churn: 5000,
    };
  }

  async fetchSreTelemetry(): Promise<SreTelemetry> {
    return {
      global_uptime: 99.995,
      regional_status: 'healthy',
      endpoints: [
        { name: '/api/v1/auth', uptime: 99.99, traffic: 150000, errors_5xx: 12 },
        { name: '/api/v1/data', uptime: 99.95, traffic: 850000, errors_5xx: 450 },
        { name: '/graphql', uptime: 98.5, traffic: 35000, errors_5xx: 520 },
      ],
    };
  }

  async fetchHistoricalData(
    kpiName: string,
    months = 12
  ): Promise<{ date: string; value: number }[]> {
    const base = kpiName.includes('uptime') ? 99 : 800000;
    const amplitude = kpiName.includes('uptime') ? 1 : 150000;
    return Array.from({ length: months }).map((_, i) => {
      const date = new Date();
      date.setMonth(date.getMonth() - (months - 1 - i));
      return {
        date: date.toLocaleDateString('es-ES', { month: 'short', year: 'numeric' }),
        value: Number(
          (base + Math.sin(i) * amplitude * 0.5 + Math.random() * amplitude * 0.5).toFixed(2)
        ),
      };
    });
  }
}

export class StrategicRepository {
  private static instance: StrategicRepository;
  private provider: DataProvider;

  private constructor(provider?: DataProvider) {
    this.provider = provider ?? StrategicRepository.createProvider();
  }

  private static createProvider(): DataProvider {
    const useMock = process.env.DATA_PROVIDER === 'mock';
    if (!process.env.DATA_PROVIDER || useMock) {
      return new MockDataProvider();
    }
    // Future providers: 'pocketbase', 'monetdb', 'rest'
    // e.g., return new PocketBaseDataProvider();
    return new MockDataProvider();
  }

  public static getInstance(provider?: DataProvider): StrategicRepository {
    if (!StrategicRepository.instance) {
      StrategicRepository.instance = new StrategicRepository(provider);
    }
    return StrategicRepository.instance;
  }

  public static resetInstance(): void {
    StrategicRepository.instance = undefined as unknown as StrategicRepository;
  }

  public setProvider(provider: DataProvider): void {
    this.provider = provider;
  }

  public async fetchTargets(quarter: string): Promise<Record<string, number>> {
    return this.provider.fetchTargets(quarter);
  }

  public async fetchAnalytics(): Promise<Record<string, number>> {
    return this.provider.fetchAnalytics();
  }

  public async fetchFinanceAnalytics(): Promise<Record<string, number>> {
    return this.provider.fetchFinanceAnalytics();
  }

  public async fetchSreTelemetry(): Promise<SreTelemetry> {
    return this.provider.fetchSreTelemetry();
  }

  public async fetchHistoricalData(
    kpiName: string,
    months = 12
  ): Promise<{ date: string; value: number }[]> {
    if (this.provider.fetchHistoricalData) {
      return this.provider.fetchHistoricalData(kpiName, months);
    }
    return new MockDataProvider().fetchHistoricalData(kpiName, months);
  }
}
