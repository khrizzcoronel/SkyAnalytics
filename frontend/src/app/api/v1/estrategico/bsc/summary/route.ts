import { NextResponse } from 'next/server';
import { StrategicRepository } from '@/lib/services/StrategicRepository';

function calculateSemaphore(kpi: string, current: number, target: number): 'green' | 'yellow' | 'red' {
  const percentage = (current / target) * 100;
  
  // Regla especial para Uptime
  if (kpi === 'process_uptime') {
    if (current >= 99.0) return 'green';
    if (current >= 95.0) return 'yellow';
    return 'red';
  }

  // Regla general (Finanzas, Cliente, etc.)
  if (percentage >= 100) return 'green';
  if (percentage >= 80) return 'yellow';
  return 'red';
}

export async function GET() {
  try {
    const repo = StrategicRepository.getInstance();
    
    // Cruce de datos en memoria (BFF Pattern)
    const targets = await repo.fetchTargets('2025-Q1');
    const analytics = await repo.fetchAnalytics();

    const bscSummary = Object.keys(targets).map((key) => {
      const target = targets[key];
      const current = analytics[key] || 0;
      return {
        kpi_name: key,
        target_value: target,
        current_value: current,
        status: calculateSemaphore(key, current, target)
      };
    });

    return NextResponse.json({
      success: true,
      data: bscSummary
    });
  } catch (error) {
    return NextResponse.json({ success: false, error: 'Internal Server Error' }, { status: 500 });
  }
}

