import type { TimeSlot } from '../types';

export const getCurrentDate = () => {
  return new Date().toISOString().split('T')[0];
};


export const fetchSchedules = async (current_time: string = getCurrentDate()): Promise<TimeSlot[]> => {
  try {
    const response = await fetch('http://127.0.0.1:8000/v1/appointments?current_datetime='+current_time);
    if (!response.ok) {
      throw new Error('Failed to fetch services');
    }

    // Transform the data to match the expected format of the frontend
    const data = await response.json();
    const schedules: TimeSlot[] = data.schedules.map((appointment: any) => ({
      time: appointment.time,
      available: appointment.available
    }));
    console.log('Schedules before shown', schedules)
    return schedules;
  } catch (error) {
    console.error('Error fetching schedules:', error);
    return [];
  }
};

