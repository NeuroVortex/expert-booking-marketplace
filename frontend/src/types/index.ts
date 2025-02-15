export interface Service {
  id: number;
  name: string;
  duration: number;
  price: number;
  description: string;
  selected: boolean;
}

export interface User{
  firstName: string;
  lastName: string;
  email: string;
  phone: string;
  identityNumber: string;
}
export interface Address {
  province: string;
  city: string;
  firstAddressLine: string;
  secondAddressLine: string | null;
  homeNumber: string;
  zipCode: string;
}
export interface UserInfo {
  personalInfo: User;
  address: Address;
}

export interface TimeSlot {
  time: string;
  available: boolean;
}

export interface AppointmentDateTime {
  date: string;
  time: string;
}

export interface UserDescription {
  description: string;
}