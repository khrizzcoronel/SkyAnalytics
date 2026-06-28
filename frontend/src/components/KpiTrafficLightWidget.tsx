import React from 'react';

interface Props {
  title: string;
  currentValue: number;
  targetValue: number;
  status: 'green' | 'yellow' | 'red';
  onClick?: () => void;
}

export const KpiTrafficLightWidget: React.FC<Props> = ({ title, currentValue, targetValue, status, onClick }) => {
  const statusColors = {
    green: 'bg-green-500',
    yellow: 'bg-yellow-400',
    red: 'bg-red-500',
  };

  return (
    <div 
      onClick={onClick}
      className="p-4 rounded-xl border border-gray-200 shadow-sm bg-white hover:shadow-md transition-shadow cursor-pointer flex flex-col md:flex-row items-center justify-between"
    >
      <div className="flex flex-col">
        <h3 className="text-gray-500 text-sm font-medium uppercase">{title}</h3>
        <p className="text-2xl font-bold text-gray-900 mt-1">
          {currentValue.toLocaleString()}
        </p>
        <p className="text-xs text-gray-400 mt-1">
          Meta: {targetValue.toLocaleString()}
        </p>
      </div>
      
      <div className="mt-4 md:mt-0 flex items-center justify-center h-12 w-12 rounded-full bg-gray-50">
        <div className={`h-6 w-6 rounded-full ${statusColors[status]} shadow-inner`} />
      </div>
    </div>
  );
};
