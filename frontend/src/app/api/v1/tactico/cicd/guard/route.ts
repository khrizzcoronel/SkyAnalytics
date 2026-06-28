import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const prId = body.pr_id || 'PR-001';
    const terraformCode = body.terraform_code || '';
    
    console.log(`[IAC GUARD] Analizando Pull Request ${prId} con tfsec (simulado)...`);
    
    // Regla RN-T03-002: Bloqueo de buckets públicos
    if (terraformCode.includes('acl = "public-read"') || terraformCode.includes('acl="public-read"')) {
      console.log(`[IAC GUARD] [ROJO] Vulnerabilidad critica detectada: S3 Bucket con acceso publico (Violacion SOC2).`);
      console.log(`[IAC GUARD] [ROJO] Bloqueando Merge. Pipeline abortado.`);
      
      return NextResponse.json({
        status: 'blocked',
        reason: 'S3 bucket exposed to public-read. SOC 2 violation.',
        severity: 'CRITICAL'
      }, { status: 403 });
    }
    
    console.log(`[IAC GUARD] [VERDE] Analisis exitoso. No se detectaron vulnerabilidades de infraestructura.`);
    return NextResponse.json({
      status: 'approved',
      message: 'Infrastructure changes passed security checks.'
    }, { status: 200 });
    
  } catch (error) {
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}
