'use client';

import React, { useEffect, useState } from 'react';
import { ErrorBudgetGauge } from '@/components/ErrorBudgetGauge';
import { EndpointHealthTable } from '@/components/EndpointHealthTable';
import { PrintSlaReportButton } from '@/components/PrintSlaReportButton';
import { AlertTriangle, CheckCircle } from 'lucide-react';

export default function EngineeringDashboardPage() {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [lastUpdated, setLastUpdated] = useState<Date>(new Date());

  const fetchHealthData = async () => {
    try {
      const res = await fetch('/api/v1/estrategico/engineering/health');
      if (res.status === 401 || res.status === 403) {
        throw new Error('No tienes permisos de ingeniería.');
      }
      const json = await res.json();
      if (json.success) {
        setData(json.data);
        setLastUpdated(new Date());
      } else {
        throw new Error('Error de conexión a MonetDB.');
      }
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    // Initial fetch
    fetchHealthData();

    // Polling cada 30 segundos (30000 ms)
    const intervalId = setInterval(fetchHealthData, 30000);
    return () => clearInterval(intervalId);
  }, []);

  return (
    <div className="p-8 max-w-7xl mx-auto">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-8 gap-4">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Salud del Sistema (SRE)</h1>
          <p className="text-gray-500 mt-1 flex items-center gap-2">
            Métricas de SLA global. <span className="text-xs bg-gray-200 px-2 py-1 rounded text-gray-700">Actualizado: {lastUpdated.toLocaleTimeString()}</span>
          </p>
        </div>
        <PrintSlaReportButton customerName="Acme Corp - Enterprise Plan" />
      </div>

      {loading && !data && <p className="text-gray-500">Cargando telemetría...</p>}
      
      {error && (
        <div className="bg-red-50 text-red-700 p-4 rounded-md border border-red-200 mb-6">
          <p className="font-semibold flex items-center gap-2">
            <AlertTriangle size={18} /> Error de Conexión
          </p>
          <p>{error}</p>
        </div>
      )}

      {data && (
        <div className="space-y-8">
          
          {/* Top Panel: Uptime & Budget */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            
            {/* Global Uptime Status */}
            <div className={`md:col-span-2 p-8 rounded-xl border shadow-sm flex flex-col justify-center ${data.global_uptime >= 99.0 ? 'bg-white border-green-200' : 'bg-red-50 border-red-300'}`}>
              <h2 className="text-xl font-bold text-gray-800 mb-2">Uptime Global (Últimos 30 días)</h2>
              <div className="flex items-center gap-4">
                <span className={`text-6xl font-black ${data.global_uptime >= 99.0 ? 'text-green-600' : 'text-red-600'}`}>
                  {data.global_uptime.toFixed(3)}%
                </span>
                {data.global_uptime >= 99.0 ? (
                  <CheckCircle className="text-green-500" size={48} />
                ) : (
                  <AlertTriangle className="text-red-500" size={48} />
                )}
              </div>
              <p className="text-gray-500 mt-2 text-sm">Objetivo SLA Garantizado: 99.0%</p>
            </div>

            {/* Error Budget Gauge */}
            <div className="flex justify-center">
              <ErrorBudgetGauge 
                consumedPercentage={data.error_budget_consumed_percentage} 
                remainingSeconds={data.error_budget_remaining_seconds} 
              />
            </div>
          </div>

          {/* Table */}
          <EndpointHealthTable endpoints={data.endpoints} />
          
        </div>
      )}
    </div>
  );
}
