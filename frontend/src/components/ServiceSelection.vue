<script setup lang="ts">
import { ref } from 'vue';
import { availableServices } from '../data/services';
import type { Service } from '../types';

const emit = defineEmits(['next', 'updateServices']);

const services = ref<Service[]>(availableServices);

const toggleService = (service: Service) => {
  service.selected = !service.selected;
  emit('updateServices', services.value.filter(s => s.selected));
};

const handleNext = () => {
  if (services.value.some(service => service.selected)) {
    emit('next');
  }
};
</script>

<template>
  <div class="service-selection">
    <h2>Select Services</h2>
    <div class="services-grid">
      <div
        v-for="service in services"
        :key="service.id"
        class="service-card"
        :class="{ selected: service.selected }"
        @click="toggleService(service)"
      >
        <h3>{{ service.name }}</h3>
        <p>Duration: {{ service.duration }} min</p>
        <p>Price: ${{ service.price }}</p>
      </div>
    </div>
    <div class="button-container">
      <button
        @click="handleNext"
        :disabled="!services.some(service => service.selected)"
        class="next-button"
      >
        Next
      </button>
    </div>
  </div>
</template>

<style scoped>
.service-selection {
  padding: 20px;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
  margin: 20px 0;
}

.service-card {
  border: 2px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.service-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.service-card.selected {
  border-color: #42b883;
  background-color: rgba(66, 184, 131, 0.1);
}

.button-container {
  margin-top: 20px;
  text-align: right;
}

.next-button {
  background-color: #42b883;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
}

.next-button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style>