'use client';

import React from 'react';

interface EndpointData {
  name: string;
  uptime: number;
  traffic: number;
  errors_5xx: number;
}

interface Props {
  endpoints: EndpointData[];
}

export const EndpointHealthTable: React.FC<Props> = ({ endpoints }) => {
  return (
    <div className="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden">
      <div className="px-6 py-4 border-b border-gray-200">
        <h3 className="text-lg font-bold text-gray-800">Desglose por Endpoint (API Gateway)</h3>
      </div>
      <div className="overflow-x-auto">
        <table className="w-full text-left text-sm">
          <thead className="bg-gray-50 text-gray-600">
            <tr>
              <th className="px-6 py-3 font-semibold">Endpoint / Servicio</th>
              <th className="px-6 py-3 font-semibold">Uptime (%)</th>
              <th className="px-6 py-3 font-semibold">Tráfico (Reqs)</th>
              <th className="px-6 py-3 font-semibold">Errores (5xx)</th>
              {/* Esta columna se ocultará al imprimir gracias a la clase internal-infra añadida en @media print global */}
              <th className="px-6 py-3 font-semibold internal-infra">Internal Pod IP (Oculto en PDF)</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200">
            {endpoints.map((ep, idx) => (
              <tr key={idx} className="hover:bg-gray-50">
                <td className="px-6 py-4 font-medium text-gray-900">{ep.name}</td>
                <td className="px-6 py-4">
                  <span className={`px-2 py-1 rounded-full text-xs font-bold ${ep.uptime < 99.0 ? 'bg-red-100 text-red-700' : 'bg-green-100 text-green-700'}`}>
                    {ep.uptime}%
                  </span>
                </td>
                <td className="px-6 py-4 text-gray-600">{ep.traffic.toLocaleString()}</td>
                <td className="px-6 py-4 text-gray-600">
                  <span className={ep.errors_5xx > (ep.traffic * 0.01) ? 'text-red-600 font-bold' : ''}>
                    {ep.errors_5xx.toLocaleString()}
                  </span>
                </td>
                <td className="px-6 py-4 text-gray-400 font-mono text-xs internal-infra">
                  10.0.{Math.floor(Math.random() * 255)}.{Math.floor(Math.random() * 255)}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
