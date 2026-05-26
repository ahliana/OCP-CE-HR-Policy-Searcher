import { render, screen } from '@testing-library/react';
import App from './App';

test('renders app heading', () => {
  render(<App />);
  const linkElement = screen.getByRole('heading', { level: 1, name: /Policy Pulse/i });
  expect(linkElement).toBeInTheDocument();
});
