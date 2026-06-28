import { NextResponse } from 'next/server';

function calculateLeadScore(email: string, baseScore: number): number {
  const targetKeywords = ['airlines', 'cargo', 'logistics'];
  const emailLower = email.toLowerCase();
  
  const hasKeyword = targetKeywords.some(kw => emailLower.includes(kw));
  
  if (hasKeyword) {
    console.log(`[LEAD SCORING] Keyword estrategico detectado en ${email}. Multiplicador x2 aplicado.`);
    return baseScore * 2;
  }
  
  return baseScore;
}

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const email = body.email || '';
    const baseScore = body.base_score || 10;
    
    // Regla RN-T01-001
    const finalScore = calculateLeadScore(email, baseScore);
    
    // Simular Regla RN-T01-002: CAC
    const campaignSpent = body.campaign_spent || 500;
    const tenantsActivated = body.tenants_activated || 25;
    const cac = tenantsActivated > 0 ? (campaignSpent / tenantsActivated).toFixed(2) : 0;
    
    const payload = {
      event: 'ACCOUNT_CREATED',
      email: email,
      lead_score: finalScore,
      campaign_cac: cac,
      status: 'SYNCED_TO_HUBSPOT'
    };
    
    console.log(`[HUBSPOT SYNC] Sincronizando lead ${email} asincronamente. Score final: ${finalScore}. CAC de campana: $${cac}`);
    
    return NextResponse.json(payload, { status: 200 });
  } catch (error) {
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}
