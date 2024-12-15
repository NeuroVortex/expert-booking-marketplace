import type { Service } from '../types';


export const availableServices: Service[] = [
  { id: 1, name: 'HVAC', duration: 30, description: 'HVAC', price: 30, selected: false },
  { id: 2, name: 'Bathroom Maintenance', duration: 120, description: 'Bathroom Maintenance', price: 100, selected: false },
  { id: 3, name: 'Plumbing', duration: 45, description: 'Plumbing', price: 35, selected: false },
  { id: 4, name: 'Replace Windows', duration: 60, description: 'Replace Windows', price: 45, selected: false },
  { id: 5, name: 'Landscaping', duration: 60, description: 'Landscaping', price: 70, selected: false },
  { id: 6, name: 'Clean dryer exhaust duct', duration: 60, description: 'Clean dryer exhaust duct', price: 70, selected: false },
];

export const fetchServices = async (): Promise<Service[]> => {
  try {
    const response = await fetch('http://localhost:8000/services'); // Update with your FastAPI URL
    if (!response.ok) {
      throw new Error('Failed to fetch services');
    }
    const services: Service[] = await response.json();
    return services;
  } catch (error) {
    console.error('Error fetching services:', error);
    return [];
  }
};
