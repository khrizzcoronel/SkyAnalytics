import { NextResponse } from 'next/server';
import { StrategicRepository } from '@/lib/services/StrategicRepository';

export async function GET() {
  try {
    const repo = StrategicRepository.getInstance();
    const telemetry = await repo.fetchSreTelemetry();

    // 99.0% SLA => 1% downtime mensual permitido
    // 30 días = 2,592,000 segundos => 1% = 25,920 segundos = 432 minutos
    const TOTAL_ERROR_BUDGET_SECONDS = 25920;

    // Simplificación: caída acumulada = 100 - uptime_global
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
