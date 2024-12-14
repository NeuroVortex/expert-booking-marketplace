export const generateTimeSlots = () => {
  const slots = [];
  for (let hour = 9; hour < 17; hour++) {
    for (let minute = 0; minute < 60; minute += 30) {
      const time = `${hour.toString().padStart(2, '0')}:${minute.toString().padStart(2, '0')}`;
      slots.push({
        time,
        available: Math.random() > 0.3 // Randomly set availability
      });
    }
  }
  return slots;
};

export const getCurrentDate = () => {
  return new Date().toISOString().split('T')[0];
};