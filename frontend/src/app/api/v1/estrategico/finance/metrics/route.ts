import { NextResponse } from 'next/server';
import { StrategicRepository } from '@/lib/services/StrategicRepository';

export async function GET() {
  try {
    const repo = StrategicRepository.getInstance();
    const analytics = await repo.fetchFinanceAnalytics();

    return NextResponse.json({
      success: true,
      data: analytics
    });
  } catch (error) {
    return NextResponse.json({ success: false, error: 'Internal Server Error' }, { status: 500 });
  }
}
