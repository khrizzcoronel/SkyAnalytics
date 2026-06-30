import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { KpiTrafficLightWidget } from './KpiTrafficLightWidget';

describe('KpiTrafficLightWidget', () => {
  it('renders title, current value and target', () => {
    render(
      <KpiTrafficLightWidget
        title="Finance ARR"
        currentValue={950000}
        targetValue={1000000}
        status="yellow"
      />
    );

    expect(screen.getByText('Finance ARR')).toBeInTheDocument();
    expect(screen.getByText('950.000')).toBeInTheDocument();
    expect(screen.getByText(/Meta: 1.000.000/)).toBeInTheDocument();
  });

  it('calls onClick when clicked', () => {
    const handleClick = vi.fn();
    render(
      <KpiTrafficLightWidget
        title="CSAT"
        currentValue={98}
        targetValue={95}
        status="green"
        onClick={handleClick}
      />
    );

    fireEvent.click(screen.getByText('CSAT').closest('div')!);
    expect(handleClick).toHaveBeenCalledOnce();
  });
});
