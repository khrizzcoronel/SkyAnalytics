'use client';

import React, { useEffect, useState } from 'react';
import { Printer } from 'lucide-react';

interface Props {
  userEmail: string;
}

export const WatermarkedPdfButton: React.FC<Props> = ({ userEmail }) => {
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  const handlePrint = () => {
    window.print();
  };

  const watermarkText = mounted
    ? `Confidencial - Exportado por ${userEmail} - ${new Date().toLocaleString('es-ES')}`
    : `Confidencial - Exportado por ${userEmail}`;

  return (
    <>
      <button
        onClick={handlePrint}
        className="print-hide inline-flex items-center gap-2 px-4 py-2 bg-slate-800 text-white text-sm font-medium rounded-lg hover:bg-slate-900 transition-colors shadow-sm"
      >
        <Printer size={16} />
        Exportar con Marca de Agua
      </button>

      {/* Marca de agua: Oculta en pantalla, visible al imprimir mediante CSS */}
      <div className="hidden print-watermark fixed inset-0 flex items-center justify-center z-50 pointer-events-none opacity-20">
        <div className="transform -rotate-45 text-4xl font-bold text-gray-800 whitespace-nowrap text-center">
          <p>{watermarkText}</p>
          <p className="mt-8">{watermarkText}</p>
          <p className="mt-8">{watermarkText}</p>
        </div>
      </div>
    </>
  );
};
