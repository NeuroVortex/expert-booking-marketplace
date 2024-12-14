export interface Service {
  id: number;
  name: string;
  duration: number;
  price: number;
  selected: boolean;
}

export interface UserInfo {
  name: string;
  email: string;
  phone: string;
}

export interface TimeSlot {
  time: string;
  available: boolean;
}

export interface AppointmentDateTime {
  date: string;
  time: string;
}