import type { Service } from '../types';

export const fetchServices = async (): Promise<Service[]> => {
  try {
    const response = await fetch('http://127.0.0.1:8000/v1/services'); // FastAPI service URL
    if (!response.ok) {
      throw new Error('Failed to fetch services');
    }

    // Transform the data to match the expected format of the frontend
    const data = await response.json();
    const services: Service[] = data.services.map((service: any) => ({
      id: service.id,
      name: service.title,
      description: service.description,
      duration: Number(service.duration),
      price: Number(service.price),
      selected: service.selected,
    }));
    console.log('services before shown', services)
    return services;
  } catch (error) {
    console.error('Error fetching services:', error);
    return [];
  }
};