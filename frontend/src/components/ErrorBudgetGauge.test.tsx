import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import { ErrorBudgetGauge } from './ErrorBudgetGauge';

describe('ErrorBudgetGauge', () => {
  it('renders consumed percentage and remaining seconds', () => {
    render(<ErrorBudgetGauge consumedPercentage={45.5} remainingSeconds={14112} />);
    expect(screen.getByText('45.5%')).toBeInTheDocument();
    expect(screen.getByText(/14112\.0/)).toBeInTheDocument();
  });

  it('shows danger warning when consumed percentage >= 80', () => {
    render(<ErrorBudgetGauge consumedPercentage={82} remainingSeconds={1000} />);
    expect(screen.getByText(/PELIGRO/)).toBeInTheDocument();
  });
});
