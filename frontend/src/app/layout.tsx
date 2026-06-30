import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import Link from "next/link";
import { LayoutDashboard, Activity, Home, BarChart3, TrendingUp, Cpu } from "lucide-react";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "SkyAnalytics Platform",
  description: "Premium Analytics Dashboard for Flight Operations",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`${geistSans.variable} ${geistMono.variable}`}>
      <body>
        <div className="app-container">
          <aside className="sidebar">
            <div style={{ marginBottom: '3rem', padding: '0.5rem' }}>
              <h2 style={{ fontSize: '1.5rem', fontWeight: 700, margin: 0, letterSpacing: '-0.03em' }}>
                <span style={{ color: 'var(--primary)' }}>Sky</span>Analytics
              </h2>
            </div>
            
            <div style={{ marginBottom: '1rem', paddingLeft: '0.5rem', fontSize: '0.75rem', fontWeight: 600, color: '#555', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
              Módulos
            </div>
            
            <nav className="sidebar-nav">
              <Link href="/" className="sidebar-link">
                <Home size={18} />
                Inicio
              </Link>
              <Link href="/dashboard/bsc" className="sidebar-link">
                <LayoutDashboard size={18} />
                BSC Estratégico
              </Link>
              <Link href="/dashboard/finance" className="sidebar-link">
                <TrendingUp size={18} />
                Finanzas
              </Link>
              <Link href="/dashboard/engineering" className="sidebar-link">
                <Cpu size={18} />
                SRE / Ingeniería
              </Link>
              <Link href="/estrategico" className="sidebar-link">
                <BarChart3 size={18} />
                Resumen Estratégico
              </Link>
              <Link href="/tactico" className="sidebar-link">
                <Activity size={18} />
                Centro Táctico
              </Link>
            </nav>
            
            <div style={{ position: 'absolute', bottom: '2rem', left: '2rem', right: '2rem' }}>
              <div style={{ padding: '1rem', background: 'rgba(59, 130, 246, 0.1)', border: '1px solid rgba(59, 130, 246, 0.2)', borderRadius: '12px' }}>
                <p style={{ margin: '0 0 0.5rem 0', fontSize: '0.8rem', fontWeight: 600, color: 'var(--primary)' }}>Estado del Sistema</p>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', fontSize: '0.8rem', color: '#a1a1aa' }}>
                  <div style={{ width: '8px', height: '8px', borderRadius: '50%', background: 'var(--accent)', boxShadow: '0 0 8px var(--accent)' }}></div>
                  Todos los servicios OK
                </div>
              </div>
            </div>
          </aside>
          
          <main className="main-content">
            <div className="bg-glow"></div>
            {children}
          </main>
        </div>
      </body>
    </html>
  );
}
