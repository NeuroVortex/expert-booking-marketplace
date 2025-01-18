<script setup lang="ts">
import { ref } from 'vue';
import ServiceSelection from './components/ServiceSelection.vue';
import UserInformation from './components/UserInformation.vue';
import DateTimeSelection from './components/DateTimeSelection.vue';
import { Service, TimeSlot, UserInfo } from './types';

const currentTab = ref(1);
const selectedServices = ref();
const userInfo = ref({});
const appointmentDateTime = ref();

const handleServiceUpdate = (services: Service) => {
  selectedServices.value = services;
};

const handleUserInfoUpdate = (info: UserInfo) => {
  userInfo.value = info;
};

const sendData = () => {
  const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        "client": userInfo.value,
        "timeSlot": appointmentDateTime.value,
        "userInfo": userInfo.value,
        "services": selectedServices.value
      })
  };
  fetch('http://127.0.0.1:8000/v1/appointments/add', requestOptions).
    then(() => alert('Appointment scheduled successfully!')).
    catch(() => alert('Appointment scheduled Unsuccessfully!'))
};

// "client": {
//     "name": "string",
//     "family_name": "string",
//     "email": "string",
//     "phone": "string",
//     "address": "string",
//     "zip_code": "string",
//     "national_code": "string"
//   },
//   "datetime": "2025-01-05T13:15:48.426Z",
//   "selectedServices": [
//     0
//   ],
//   "description": "string"
const handleAppointmentSubmit = (dateTime: TimeSlot) => {
  appointmentDateTime.value = dateTime;
  sendData();
};

const switchTab = (tabNumber: number) => {
  currentTab.value = tabNumber;
};

const nextTab = () => {
  if (currentTab.value < 3) {
    currentTab.value++;
  }
};

const previousTab = () => {
  if (currentTab.value > 1) {
    currentTab.value--;
  }
};
</script>

<template>
  <div class="reservation-app">
    <div class="tabs-container">
      <div class="tabs">
        <button
          v-for="tab in 3"
          :key="tab"
          class="tab-button"
          :class="{ active: tab === currentTab }"
          @click="switchTab(tab)"
        >
          {{ tab === 1 ? 'Services' : tab === 2 ? 'Information' : 'Schedule' }}
        </button>
      </div>

      <div class="tab-content">
        <div v-show="currentTab === 1">
          <ServiceSelection
            @next="nextTab"
            @update-services="handleServiceUpdate"
          />
        </div>
        
        <div v-show="currentTab === 2">
          <UserInformation
            @next="nextTab"
            @back="previousTab"
            @update-user-info="handleUserInfoUpdate"
          />
        </div>
        
        <div v-show="currentTab === 3">
          <DateTimeSelection
            @back="previousTab"
            @submit="handleAppointmentSubmit"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<style>
:root {
  color-scheme: light;
  color: #000000;
  background-color: #ffffff;
}

body {
  margin: 0;
  min-height: 100vh;
  background-color: #f5f5f5;
}

.reservation-app {
  max-width: 1200px;
  margin: 40px auto;
  padding: 20px;
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  color: #000000;
}

.tabs-container {
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.tabs {
  display: flex;
  background-color: #f8f8f8;
  border-bottom: 1px solid #eaeaea;
}

.tab-button {
  flex: 1;
  padding: 16px;
  background: none;
  border: none;
  border-bottom: 3px solid transparent;
  font-size: 16px;
  font-weight: 600;
  color: #666;
  cursor: pointer;
  transition: all 0.3s ease;
}

.tab-button:hover {
  background-color: #f0f0f0;
  color: #42b883;
}

.tab-button.active {
  color: #42b883;
  border-bottom-color: #42b883;
  background-color: white;
}

.tab-content {
  min-height: 400px;
}

/* Override any light/dark mode styles */
h1, h2, h3, h4, h5, h6, p, label, input, button {
  color: #000000;
}

input {
  background-color: white;
  border: 1px solid #ddd;
  color: #000000;
}

button {
  font-weight: 600;
}

.service-card {
  background-color: white;
  color: #000000;
}

.service-card h3 {
  color: #000000;
}

.service-card p {
  color: #333333;
}
</style>