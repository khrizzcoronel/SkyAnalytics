import { DollarSign, Plane, Clock, TrendingUp } from "lucide-react";

export default function EstrategicoPage() {
  return (
    <div className="animate-in delay-1">
      <h1 className="page-title">Dashboard Estratégico</h1>
      <p className="page-subtitle">Balanced Scorecard & Indicadores Financieros de Nivel C</p>
      
      <div className="grid-cards animate-in delay-2">
        <div className="glass-card">
          <div className="card-title">
            <DollarSign size={16} color="var(--primary)" /> Ingresos (ARR)
          </div>
          <p className="card-value">$14.2M</p>
          <p className="card-trend trend-up">↑ +12.5% vs mes anterior</p>
        </div>
        
        <div className="glass-card">
          <div className="card-title">
            <TrendingUp size={16} color="var(--accent)" /> Margen Operativo
          </div>
          <p className="card-value">22.4%</p>
          <p className="card-trend trend-up">↑ +2.1% (Objetivo superado)</p>
        </div>
        
        <div className="glass-card">
          <div className="card-title">
            <Clock size={16} color="var(--danger)" /> Retrasos Globales
          </div>
          <p className="card-value">18.2%</p>
          <p className="card-trend trend-down">↓ -1.5% vs mes anterior (Mejora)</p>
        </div>
        
        <div className="glass-card">
          <div className="card-title">
            <Plane size={16} color="var(--primary)" /> Vuelos Completados
          </div>
          <p className="card-value">12,450</p>
          <p className="card-trend trend-neutral">→ 99.8% Tasa de completitud</p>
        </div>
      </div>
      
      <div className="grid-cards animate-in delay-3" style={{ gridTemplateColumns: '1fr 1fr' }}>
        <div className="glass-card" style={{ height: '300px', display: 'flex', flexDirection: 'column' }}>
          <div className="card-title">Evolución de Ingresos y Retrasos (2026)</div>
          <div style={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center', border: '1px dashed var(--border)', borderRadius: '8px', marginTop: '1rem', background: 'rgba(0,0,0,0.2)' }}>
            <span style={{ color: '#a1a1aa', fontSize: '0.875rem' }}>[Componente de Gráfico de Área interactivo]</span>
          </div>
        </div>
        
        <div className="glass-card" style={{ height: '300px', display: 'flex', flexDirection: 'column' }}>
          <div className="card-title">Cumplimiento BSC por Perspectiva</div>
          <div style={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center', border: '1px dashed var(--border)', borderRadius: '8px', marginTop: '1rem', background: 'rgba(0,0,0,0.2)' }}>
            <span style={{ color: '#a1a1aa', fontSize: '0.875rem' }}>[Componente de Gráfico Radial interactivo]</span>
          </div>
        </div>
      </div>
    </div>
  );
}
