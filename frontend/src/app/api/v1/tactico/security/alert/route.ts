import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const eventType = body.event_type || 'auth_failure';
    const sourceIp = body.source_ip || '192.168.1.1';
    const failureCount = body.failure_count || 0;
    
    console.log(`[WAF SECURITY] Analizando evento entrante desde IP: ${sourceIp}...`);
    
    // Regla RN-T06-001: Clasificacion Sev1
    if (eventType === 'crypto_mining' || eventType === 'mass_exfiltration') {
      console.log(`[WAF SECURITY] [ROJO] ALERTA SEV1 CRITICA: Deteccion de ${eventType}.`);
      console.log(`[SLACK/PAGERDUTY] [SMS DISPARADO] Despertando al SRE (On-Call)...`);
      return NextResponse.json({
        severity: 'Sev1',
        action: 'SMS_SENT',
        message: 'Critical security breach detected.'
      }, { status: 200 });
    }
    
    // Regla RN-T06-001: Clasificacion Sev2 (Fuerza Bruta)
    if (eventType === 'auth_failure' && failureCount > 100) {
      console.log(`[WAF SECURITY] [NARANJA] ALERTA SEV2: Ataque de fuerza bruta detectado (${failureCount} intentos).`);
      console.log(`[AUTO-REMEDIACION] Bloqueando IP ${sourceIp} en el WAF por 24 horas.`);
      console.log(`[SLACK] Notificando silenciosamente al canal #security-alerts.`);
      return NextResponse.json({
        severity: 'Sev2',
        action: 'IP_BLOCKED',
        message: 'Brute force detected. IP blocked.'
      }, { status: 200 });
    }
    
    // Sev3 Default
    console.log(`[WAF SECURITY] [AMARILLO] ALERTA SEV3: Anomalia menor detectada.`);
    return NextResponse.json({
      severity: 'Sev3',
      action: 'LOGGED_ONLY',
      message: 'Minor anomaly logged.'
    }, { status: 200 });
    
  } catch (error) {
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}
