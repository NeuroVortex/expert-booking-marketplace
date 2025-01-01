<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { fetchSchedules, getCurrentDate } from '../utils/timeUtils';
import type { TimeSlot } from '../types';

const emit = defineEmits(['back', 'submit']);

const selectedDate = ref(getCurrentDate());
const selectedTime = ref('');
const timeSlots = ref<TimeSlot[]>([]);

const updateTimeSlots = async () => {
  console.log("Selected Date", selectedDate.value.toString())
  timeSlots.value = await fetchSchedules(selectedDate.value.toString());
};

onMounted(() => {
  updateTimeSlots();
});

const handleDateChange = () => {
  selectedTime.value = '';
  updateTimeSlots();
};

const handleSubmit = () => {
  if (selectedDate.value && selectedTime.value) {
    emit('submit', {
      date: selectedDate.value,
      time: selectedTime.value
    });
  }
};
</script>

<template>
  <div class="datetime-selection">
    <h2>Select Date & Time</h2>
    
    <div class="date-picker">
      <label for="date">Select Date:</label>
      <input
        type="date"
        id="date"
        v-model="selectedDate"
        :min="getCurrentDate()"
        @change="handleDateChange"
      >
    </div>

    <div class="time-slots">
      <h3>Available Time Slots</h3>
      <div class="slots-grid">
        <button
          v-for="slot in timeSlots"
          :key="slot.time"
          :class="{
            'time-slot': true,
            'available': slot.available,
            'unavailable': !slot.available,
            'selected': selectedTime === slot.time
          }"
          :disabled="!slot.available"
          @click="selectedTime = slot.time"
        >
          {{ slot.time }}
        </button>
      </div>
    </div>

    <div class="button-container">
      <button class="back-button" @click="emit('back')">
        Back
      </button>
      <button
        class="submit-button"
        :disabled="!selectedDate || !selectedTime"
        @click="handleSubmit"
      >
        Submit AppointmentModel
      </button>
    </div>
  </div>
</template>

<style scoped>
.datetime-selection {
  padding: 20px;
}

.date-picker {
  margin: 20px 0;
}

.slots-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
  gap: 10px;
  margin: 20px 0;
}

.time-slot {
  padding: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.time-slot.available {
  background-color: #42b883;
  color: white;
}

.time-slot.unavailable {
  background-color: #ff4444;
  color: white;
  cursor: not-allowed;
}

.time-slot.selected {
  transform: scale(1.05);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.button-container {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.back-button {
  background-color: #666;
  color: white;
}

.submit-button {
  background-color: #42b883;
  color: white;
}

button {
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style>