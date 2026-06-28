import { NextResponse } from 'next/server';

export async function GET(request: Request) {
  try {
    const { searchParams } = new URL(request.url);
    const sandboxToken = searchParams.get('sandbox_token');
    const endpoint = searchParams.get('endpoint') || 'weather';
    
    // Regla RN-T07-002: Validacion de Sandbox Token
    if (!sandboxToken || sandboxToken === '') {
      console.log(`[DEVEX PORTAL] [ROJO] Rechazando peticion: Token de Sandbox ausente.`);
      return NextResponse.json({ error: 'Missing sandbox_token' }, { status: 401 });
    }
    
    console.log(`[DEVEX PORTAL] [VERDE] Peticion de prueba recibida para endpoint '${endpoint}' con token temporal.`);
    
    // Mock Data Response
    if (endpoint === 'weather') {
      const mockResponse = {
        airport_code: "LHR",
        prediction: {
          condition: "Thunderstorm",
          visibility_km: 2.5,
          delay_risk: "HIGH",
          confidence_score: 0.92
        },
        _metadata: {
          environment: "sandbox",
          latency_ms: 45
        }
      };
      return NextResponse.json(mockResponse, { status: 200 });
    }
    
    return NextResponse.json({ error: 'Endpoint mock not found' }, { status: 404 });
    
  } catch (error) {
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}
