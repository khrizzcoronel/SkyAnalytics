'use client';

import React, { useEffect, useState } from 'react';
import { WatermarkedPdfButton } from '@/components/WatermarkedPdfButton';

export default function FinanceDashboardPage() {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await fetch('/api/v1/estrategico/finance/metrics');
        if (res.status === 401 || res.status === 403) {
          throw new Error('No tienes permisos para ver este tablero (se requiere BOARD_MEMBER).');
        }
        
        const json = await res.json();
        if (json.success) {
          setData(json.data);
        } else {
          throw new Error('Error al cargar datos financieros');
        }
      } catch (err: any) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="p-8 max-w-7xl mx-auto">
      <div className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Métricas Financieras y Rentabilidad</h1>
          <p className="text-gray-500 mt-1">Análisis de LTV, CAC, ARR y Margen Bruto.</p>
        </div>
        {/* Usamos el botón con marca de agua y mockeamos el usuario actual */}
        <WatermarkedPdfButton userEmail="founder@skyanalytics.com" />
      </div>

      {loading && <p className="text-gray-500">Cargando analítica desde MonetDB...</p>}
      
      {error && (
        <div className="bg-red-50 text-red-700 p-4 rounded-md border border-red-200">
          <p className="font-semibold">Acceso Denegado</p>
          <p>{error}</p>
        </div>
      )}

      {!loading && !error && data && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          
          <div className="p-6 rounded-xl border border-gray-200 shadow-sm bg-white">
            <h3 className="text-gray-500 text-sm font-medium uppercase">ARR Consolidado</h3>
            <p className="text-3xl font-bold text-gray-900 mt-2">
              ${data.arr_total.toLocaleString()}
            </p>
          </div>

          <div className="p-6 rounded-xl border border-gray-200 shadow-sm bg-white">
            <h3 className="text-gray-500 text-sm font-medium uppercase">Ratio LTV / CAC</h3>
            <p className="text-3xl font-bold text-gray-900 mt-2">
              {data.ltv_cac_ratio}x
            </p>
          </div>

          <div className="p-6 rounded-xl border border-gray-200 shadow-sm bg-white">
            <h3 className="text-gray-500 text-sm font-medium uppercase">Gross Margin</h3>
            <p className="text-3xl font-bold text-green-600 mt-2">
              {data.gross_margin}%
            </p>
          </div>

          <div className={`p-6 rounded-xl border shadow-sm ${data.nrr < 100 ? 'border-red-300 bg-red-50' : 'border-gray-200 bg-white'}`}>
            <h3 className={`text-sm font-medium uppercase ${data.nrr < 100 ? 'text-red-700' : 'text-gray-500'}`}>
              Net Revenue Retention (NRR)
            </h3>
            <div className="flex items-center gap-2 mt-2">
              <p className={`text-3xl font-bold ${data.nrr < 100 ? 'text-red-700' : 'text-gray-900'}`}>
                {data.nrr}%
              </p>
              {data.nrr < 100 && (
                <span className="text-xs font-bold text-red-700 bg-red-200 px-2 py-1 rounded-full uppercase">
                  Alerta Churn
                </span>
              )}
            </div>
          </div>

        </div>
      )}
    </div>
  );
}
