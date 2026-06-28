'use client';

import React, { useEffect, useState } from 'react';
import { KpiTrafficLightWidget } from '@/components/KpiTrafficLightWidget';
import { HistoricalChartModal } from '@/components/HistoricalChartModal';
import { PrintToPdfButton } from '@/components/PrintToPdfButton';

export default function BscDashboardPage() {
  const [data, setData] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  
  const [selectedKpi, setSelectedKpi] = useState<string | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      try {
        // En la vida real, enviaríamos el JWT en los headers (o Next.js middleware lo toma de la cookie)
        const res = await fetch('/api/v1/estrategico/bsc/summary');
        
        if (res.status === 401 || res.status === 403) {
          throw new Error('No tienes permisos para ver este tablero.');
        }
        
        const json = await res.json();
        if (json.success) {
          setData(json.data);
        } else {
          throw new Error('Error al cargar datos');
        }
      } catch (err: any) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const handleKpiClick = (kpiName: string) => {
    setSelectedKpi(kpiName);
    setIsModalOpen(true);
  };

  // Datos mock para el gráfico LTM
  const mockHistoricalData = Array.from({ length: 12 }).map((_, i) => {
    const date = new Date();
    date.setMonth(date.getMonth() - (11 - i));
    return {
      date: date.toLocaleDateString('es-ES', { month: 'short', year: 'numeric' }),
      value: Math.floor(Math.random() * (1000000 - 800000) + 800000),
    };
  });

  return (
    <div className="p-8 max-w-7xl mx-auto">
      <div className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Balanced Scorecard</h1>
          <p className="text-gray-500 mt-1">Visión consolidada de los 4 pilares estratégicos.</p>
        </div>
        <PrintToPdfButton />
      </div>

      {loading && <p className="text-gray-500">Cargando indicadores (LTM)...</p>}
      
      {error && (
        <div className="bg-red-50 text-red-700 p-4 rounded-md border border-red-200">
          <p className="font-semibold">Acceso Denegado / Error</p>
          <p>{error}</p>
        </div>
      )}

      {!loading && !error && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {data.map((kpi) => (
            <KpiTrafficLightWidget
              key={kpi.kpi_name}
              title={kpi.kpi_name.replace('_', ' ')}
              currentValue={kpi.current_value}
              targetValue={kpi.target_value}
              status={kpi.status}
              onClick={() => handleKpiClick(kpi.kpi_name)}
            />
          ))}
        </div>
      )}

      <HistoricalChartModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        title={selectedKpi?.replace('_', ' ').toUpperCase() || ''}
        data={mockHistoricalData}
      />
    </div>
  );
}
