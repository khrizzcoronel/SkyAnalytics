'use client';

import React from 'react';

interface Props {
  consumedPercentage: number;
  remainingSeconds: number;
}

export const ErrorBudgetGauge: React.FC<Props> = ({ consumedPercentage, remainingSeconds }) => {
  const isDanger = consumedPercentage >= 80;
  
  // Calculate dash array for SVG circle (circumference = 2 * PI * r)
  const radius = 60;
  const circumference = 2 * Math.PI * radius;
  const strokeDashoffset = circumference - (consumedPercentage / 100) * circumference;

  return (
    <div className="flex flex-col items-center p-6 bg-white rounded-xl border border-gray-200 shadow-sm relative">
      <h3 className="text-gray-500 text-sm font-medium uppercase mb-4">Error Budget Consumido</h3>
      
      <div className="relative flex items-center justify-center w-40 h-40">
        {/* Background Circle */}
        <svg className="absolute inset-0 w-full h-full transform -rotate-90">
          <circle
            cx="80"
            cy="80"
            r={radius}
            stroke="#e5e7eb"
            strokeWidth="12"
            fill="transparent"
          />
          {/* Progress Circle */}
          <circle
            cx="80"
            cy="80"
            r={radius}
            stroke={isDanger ? '#ef4444' : '#3b82f6'}
            strokeWidth="12"
            fill="transparent"
            strokeDasharray={circumference}
            strokeDashoffset={strokeDashoffset}
            className="transition-all duration-1000 ease-out"
          />
        </svg>
        
        {/* Center Text */}
        <div className="absolute flex flex-col items-center justify-center">
          <span className={`text-3xl font-bold ${isDanger ? 'text-red-500' : 'text-blue-500'}`}>
            {consumedPercentage.toFixed(1)}%
          </span>
        </div>
      </div>
      
      <p className="mt-4 text-sm font-medium text-gray-700">
        Quedan <span className="font-bold">{remainingSeconds.toFixed(1)} s</span> este mes
      </p>
      
      {isDanger && (
        <span className="mt-2 text-xs font-bold text-red-700 bg-red-100 px-3 py-1 rounded-full uppercase text-center">
          PELIGRO: Congelar despliegues
        </span>
      )}
    </div>
  );
};
