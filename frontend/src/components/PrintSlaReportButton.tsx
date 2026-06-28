'use client';

import React from 'react';
import { Printer } from 'lucide-react';

interface Props {
  customerName?: string;
}

export const PrintSlaReportButton: React.FC<Props> = ({ customerName = 'Enterprise Client' }) => {
  const handlePrint = () => {
    window.print();
  };

  const reportDate = new Date().toLocaleDateString('es-ES', { month: 'long', year: 'numeric' });

  return (
    <>
      <button
        onClick={handlePrint}
        className="print-hide inline-flex items-center gap-2 px-4 py-2 bg-indigo-600 text-white text-sm font-medium rounded-lg hover:bg-indigo-700 transition-colors shadow-sm"
      >
        <Printer size={16} />
        Generar Reporte SLA
      </button>

      {/* Header oficial del reporte, solo visible al imprimir */}
      <div className="hidden print-watermark w-full border-b-2 border-indigo-600 pb-4 mb-8">
        <h1 className="text-2xl font-bold text-gray-900">Certificado de Nivel de Servicio (SLA)</h1>
        <p className="text-gray-600">Cliente: {customerName}</p>
        <p className="text-gray-600">Período de Evaluación: {reportDate}</p>
        <p className="text-xs text-gray-400 mt-2">Documento generado automáticamente por SkyAnalytics SRE Portal.</p>
      </div>
    </>
  );
};
