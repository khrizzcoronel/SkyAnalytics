import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const isExistingCustomer = body.is_existing_customer || false;
    const visits = body.visits || 1000;
    const pValue = body.p_value || 0.1;
    
    console.log(`[GROWTH ABTEST] Evaluando enrutamiento y estadisticas de Pricing...`);
    
    // Regla RN-T10-002: Grandfathering
    if (isExistingCustomer) {
      console.log(`[GROWTH ABTEST] [AMARILLO] Cliente existente detectado. Forzando Variante A (Legacy Pricing). Grandfathering activo.`);
      return NextResponse.json({
        variant: 'A',
        price: 499,
        message: 'Legacy plan enforced.'
      }, { status: 200 });
    }
    
    // Regla RN-T10-001: Significancia
    if (visits >= 10000 && pValue < 0.05) {
      console.log(`[GROWTH ABTEST] [VERDE] Experimento Concluyente: Significancia alcanzada (P-Value: ${pValue}). Desplegando Variante B ($599).`);
      return NextResponse.json({
        status: 'conclusive',
        winner: 'B',
        recommendation: 'Deploy to 100%'
      }, { status: 200 });
    }
    
    console.log(`[GROWTH ABTEST] Experimento en progreso. Trafico 50/50. (Visitas: ${visits}, P-Value: ${pValue})`);
    return NextResponse.json({
      status: 'in_progress',
      variant: Math.random() > 0.5 ? 'A' : 'B',
      message: 'Keep gathering data.'
    }, { status: 200 });
    
  } catch (error) {
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}
