export interface Service {
  id: number;
  name: string;
  duration: number;
  price: number;
  description: string;
  selected: boolean;
}

export interface UserInfo {
  name: string;
  familyName: string;
  email: string;
  phone: string;
  address: Text;
  nationalCode: string;
  zipCode: string;
}

export interface TimeSlot {
  time: string;
  available: boolean;
}

export interface AppointmentDateTime {
  date: string;
  time: string;
}