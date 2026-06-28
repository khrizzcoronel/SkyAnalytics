import { NextResponse } from 'next/server';
import { StrategicRepository } from '@/lib/services/StrategicRepository';

export async function GET() {
  try {
    const repo = StrategicRepository.getInstance();
    const telemetry = await repo.fetchSreTelemetry();

    // 4.38 min/month = 262.8 seconds
    const TOTAL_ERROR_BUDGET_SECONDS = 262.8; 
    
    // Simplificación: si uptime global es 99.995%, la caída fue 0.005%. 
    // En 30 días = 2,592,000 segundos. El 0.005% = 129.6s consumidos.
    const downtimePercentage = 100 - telemetry.global_uptime;
    const SECONDS_IN_MONTH = 30 * 24 * 60 * 60;
    const consumedSeconds = (downtimePercentage / 100) * SECONDS_IN_MONTH;
    
    const remainingSeconds = TOTAL_ERROR_BUDGET_SECONDS - consumedSeconds;
    const consumedPercentage = (consumedSeconds / TOTAL_ERROR_BUDGET_SECONDS) * 100;

    return NextResponse.json({
      success: true,
      data: {
        ...telemetry,
        error_budget_consumed_seconds: consumedSeconds,
        error_budget_remaining_seconds: remainingSeconds > 0 ? remainingSeconds : 0,
        error_budget_consumed_percentage: consumedPercentage,
        status_indicator: consumedPercentage >= 80 ? 'danger' : 'healthy'
      }
    });
  } catch (error) {
    return NextResponse.json({ success: false, error: 'Internal Server Error' }, { status: 500 });
  }
}
