import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const namespace = body.namespace || 'production';
    const experimentType = body.experiment_type || 'blackhole_network';
    const simulatedP95Latency = body.simulated_p95_latency || 600;
    
    console.log(`[CHAOS ORCHESTRATOR] Solicitud de experimento: ${experimentType} en namespace '${namespace}'`);
    
    // Regla RNF-T09-001: Kill Switch para Producción
    if (namespace !== 'staging') {
      console.log(`[CHAOS ORCHESTRATOR] [ROJO] KILL SWITCH ACTIVADO: Abortando experimento. Solo permitido en 'staging'.`);
      return NextResponse.json({
        status: 'aborted',
        reason: 'Chaos experiments are strictly restricted to staging environments.'
      }, { status: 403 });
    }
    
    console.log(`[CHAOS ORCHESTRATOR] Ejecutando experimento en staging...`);
    
    // Regla RN-T09-001: Validación de Latencia P95
    if (simulatedP95Latency > 500) {
      console.log(`[CHAOS ORCHESTRATOR] [ROJO] Experimento Fallido: Latencia p95 (${simulatedP95Latency}ms) superó el umbral de 500ms.`);
      return NextResponse.json({
        status: 'failed',
        p95_latency: simulatedP95Latency,
        message: 'Resiliency criteria not met. Service degraded.'
      }, { status: 200 });
    }
    
    console.log(`[CHAOS ORCHESTRATOR] [VERDE] Experimento Exitoso: HPA auto-escaló y la latencia p95 se mantuvo en ${simulatedP95Latency}ms.`);
    return NextResponse.json({
      status: 'passed',
      p95_latency: simulatedP95Latency,
      message: 'Service recovered gracefully.'
    }, { status: 200 });
    
  } catch (error) {
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}
