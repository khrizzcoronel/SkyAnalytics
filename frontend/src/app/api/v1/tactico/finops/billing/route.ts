import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const serviceName = body.service || 'AmazonS3';
    const actualCost = parseFloat(body.actual_cost) || 0;
    const forecastCost = parseFloat(body.forecast_cost) || 1;
    
    console.log(`[FINOPS ANALYZER] Analizando costos para el servicio: ${serviceName}...`);
    
    // Regla RN-T08-001: Calculo de desviación
    const deltaPercentage = ((actualCost - forecastCost) / forecastCost) * 100;
    
    if (deltaPercentage > 20) {
      console.log(`[FINOPS ANALYZER] [ROJO] ALERTA: Sobrecosto detectado en ${serviceName}.`);
      console.log(`[FINOPS ANALYZER] Desviacion: +${deltaPercentage.toFixed(2)}% (Actual: $${actualCost}, Forecast: $${forecastCost}).`);
      console.log(`[SLACK] Notificando al canal #finops...`);
      
      // Simular Rightsizing
      const recommendation = serviceName.includes('EC2') || serviceName.includes('EKS')
        ? "Consider rightsizing from m5.2xlarge to m5.xlarge based on CPU utilization."
        : "Consider implementing lifecycle policies to transition unused objects to Glacier.";
        
      return NextResponse.json({
        status: 'alert',
        service: serviceName,
        delta_percentage: deltaPercentage,
        recommendation: recommendation
      }, { status: 200 });
    }
    
    console.log(`[FINOPS ANALYZER] [VERDE] Gasto dentro de lo proyectado para ${serviceName} (Delta: ${deltaPercentage.toFixed(2)}%).`);
    return NextResponse.json({
      status: 'ok',
      service: serviceName,
      delta_percentage: deltaPercentage
    }, { status: 200 });
    
  } catch (error) {
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}
