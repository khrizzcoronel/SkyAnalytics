import Link from "next/link";
import { ArrowRight, Plane, Activity, LineChart } from "lucide-react";

export default function Home() {
  return (
    <div className="animate-in delay-1" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '80vh', textAlign: 'center' }}>
      <div style={{ padding: '1.5rem', background: 'rgba(255,255,255,0.03)', border: '1px solid var(--border)', borderRadius: '50%', marginBottom: '2rem', boxShadow: '0 0 40px rgba(59, 130, 246, 0.1)' }}>
        <Plane size={48} color="var(--primary)" />
      </div>
      
      <h1 className="page-title" style={{ fontSize: '4rem', marginBottom: '1rem', lineHeight: 1.1 }}>SkyAnalytics<br/>Data Platform</h1>
      <p className="page-subtitle" style={{ maxWidth: '600px', margin: '0 auto 3rem auto', fontSize: '1.25rem' }}>
        Plataforma analítica y operativa de última generación para la optimización de vuelos, rentabilidad y predicción de retrasos.
      </p>
      
      <div style={{ display: 'flex', gap: '1.5rem', justifyContent: 'center' }}>
        <Link 
          href="/estrategico" 
          style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', padding: '1rem 2rem', background: 'var(--foreground)', color: 'var(--background)', borderRadius: '99px', fontWeight: 600, textDecoration: 'none', transition: 'transform 0.2s ease', boxShadow: '0 4px 14px rgba(255,255,255,0.2)' }} 
        >
          <LineChart size={20} />
          Módulo Estratégico
        </Link>
        <Link 
          href="/tactico" 
          style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', padding: '1rem 2rem', background: 'rgba(255,255,255,0.05)', color: 'var(--foreground)', border: '1px solid var(--border)', borderRadius: '99px', fontWeight: 600, textDecoration: 'none', transition: 'all 0.2s ease' }} 
        >
          <Activity size={20} />
          Módulo Táctico
        </Link>
      </div>
    </div>
  );
}
