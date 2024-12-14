import type { Service } from '../types';

export const availableServices: Service[] = [
  { id: 1, name: 'Haircut', duration: 30, price: 30, selected: false },
  { id: 2, name: 'Hair Coloring', duration: 120, price: 100, selected: false },
  { id: 3, name: 'Manicure', duration: 45, price: 35, selected: false },
  { id: 4, name: 'Pedicure', duration: 60, price: 45, selected: false },
  { id: 5, name: 'Facial', duration: 60, price: 70, selected: false },
];