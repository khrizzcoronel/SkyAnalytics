import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import { EndpointHealthTable } from './EndpointHealthTable';

describe('EndpointHealthTable', () => {
  const endpoints = [
    { name: '/api/v1/auth', uptime: 99.99, traffic: 150000, errors_5xx: 12 },
    { name: '/graphql', uptime: 98.5, traffic: 35000, errors_5xx: 520 },
  ];

  it('renders endpoint names and uptime badges', () => {
    render(<EndpointHealthTable endpoints={endpoints} />);
    expect(screen.getByText('/api/v1/auth')).toBeInTheDocument();
    expect(screen.getByText('/graphql')).toBeInTheDocument();
    expect(screen.getAllByText(/99.99%|98.5%/).length).toBe(2);
  });

  it('highlights endpoints below 99% uptime', () => {
    render(<EndpointHealthTable endpoints={endpoints} />);
    const graphqlBadge = screen.getByText('98.5%');
    expect(graphqlBadge.className).toContain('bg-red-100');
  });
});
