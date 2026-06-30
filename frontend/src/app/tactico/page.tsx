import { AlertTriangle, Database, Activity, MapPin } from "lucide-react";

export default function TacticoPage() {
  return (
    <div className="animate-in delay-1">
      <h1 className="page-title">Centro de Control Táctico</h1>
      <p className="page-subtitle">Operaciones en Vivo, Calidad de Datos y Predicciones de ML</p>
      
      <div className="grid-cards animate-in delay-2">
        <div className="glass-card">
          <div className="card-title">
            <Database size={16} color="var(--primary)" /> Sync MonetDB / PocketBase
          </div>
          <p className="card-value">Saludable</p>
          <p className="card-trend trend-neutral">Último checkpoint: hace 14 min</p>
        </div>
        
        <div className="glass-card">
          <div className="card-title">
            <AlertTriangle size={16} color="var(--warning)" /> Data Drift (Índice PSI)
          </div>
          <p className="card-value" style={{ color: 'var(--warning)' }}>0.082</p>
          <p className="card-trend trend-neutral">Moderado - Requiere atención en 24h</p>
        </div>
        
        <div className="glass-card">
          <div className="card-title">
            <Activity size={16} color="var(--accent)" /> Exactitud XGBoost (MAPE)
          </div>
          <p className="card-value">12.4%</p>
          <p className="card-trend trend-up">Modelo en producción operando normal</p>
        </div>
      </div>
      
      <div className="glass-card animate-in delay-3" style={{ padding: 0, overflow: 'hidden' }}>
        <div style={{ padding: '1.5rem', borderBottom: '1px solid var(--border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div className="card-title" style={{ margin: 0 }}>
            <MapPin size={16} color="var(--foreground)" /> Despacho de Vuelos
          </div>
          <span className="badge badge-success" style={{ display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
            <span style={{ width: '6px', height: '6px', borderRadius: '50%', background: 'var(--accent)', boxShadow: '0 0 10px var(--accent)' }}></span>
            LIVE
          </span>
        </div>
        <div className="data-table-container" style={{ border: 'none', borderRadius: 0 }}>
          <table className="data-table">
            <thead>
              <tr>
                <th>Identificador</th>
                <th>Aerolínea</th>
                <th>Ruta (Origen → Destino)</th>
                <th>Hora Salida</th>
                <th>Estado Actual</th>
                <th>Alerta ML (Predicción)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style={{ fontWeight: 600, color: 'var(--foreground)' }}>AA1045</td>
                <td>American Airlines</td>
                <td>JFK → LAX</td>
                <td>10:45 AM</td>
                <td><span className="badge badge-success">A Tiempo</span></td>
                <td style={{ color: 'var(--accent)' }}>+0 min</td>
              </tr>
              <tr>
                <td style={{ fontWeight: 600, color: 'var(--foreground)' }}>DL2910</td>
                <td>Delta Air Lines</td>
                <td>ATL → ORD</td>
                <td>11:20 AM</td>
                <td><span className="badge badge-warning">Retrasado</span></td>
                <td style={{ color: 'var(--warning)', fontWeight: 500 }}>+18 min delay</td>
              </tr>
              <tr>
                <td style={{ fontWeight: 600, color: 'var(--foreground)' }}>UA882</td>
                <td>United Airlines</td>
                <td>SFO → EWR</td>
                <td>12:05 PM</td>
                <td><span className="badge badge-danger">Crítico</span></td>
                <td style={{ color: 'var(--danger)', fontWeight: 600 }}>+145 min delay</td>
              </tr>
              <tr>
                <td style={{ fontWeight: 600, color: 'var(--foreground)' }}>SW4421</td>
                <td>Southwest Airlines</td>
                <td>DAL → HOU</td>
                <td>12:30 PM</td>
                <td><span className="badge badge-success">A Tiempo</span></td>
                <td style={{ color: 'var(--accent)' }}>-2 min</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
