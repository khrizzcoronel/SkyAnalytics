import { NextResponse } from 'next/server';

const EXPECTED_PROXY_SECRET = process.env.RAPIDAPI_PROXY_SECRET || 'test_secret_123';

export async function GET(request: Request) {
  try {
    const proxySecret = request.headers.get('x-rapidapi-proxy-secret');
    const rapidApiUser = request.headers.get('x-rapidapi-user');
    
    // Regla RNF-T02-001: Validación de seguridad
    if (!proxySecret || proxySecret !== EXPECTED_PROXY_SECRET) {
      console.log(`[RAPIDAPI GATEWAY] [ROJO] Intento de bypass detectado. Proxy Secret invalido u omitido.`);
      return NextResponse.json(
        { error: 'Unauthorized: Invalid Proxy Secret' },
        { status: 401 }
      );
    }
    
    // Simular procesamiento de backend ML
    console.log(`[RAPIDAPI GATEWAY] Peticion autorizada desde el usuario de RapidAPI: ${rapidApiUser || 'anonimo'}`);
    console.log(`[RAPIDAPI GATEWAY] Registrando metricas de rate limit y devolviendo datos cacheados...`);
    
    const payload = {
      status: 'success',
      data: {
        flight_delay_probability: 0.15,
        cache_hit: true
      },
      message: 'Datos obtenidos exitosamente'
    };
    
    return NextResponse.json(payload, { status: 200 });
  } catch (error) {
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}
