<script setup lang="ts">
import { ref, computed } from 'vue';
import type { UserInfo } from '../types';

const emit = defineEmits(['next', 'back', 'updateUserInfo']);

const userInfo = ref<UserInfo>({
  name: '',
  email: '',
  phone: '',
});

const isFormValid = computed(() => {
  return userInfo.value.name && 
         userInfo.value.email && 
         userInfo.value.phone;
});

const handleNext = () => {
  if (isFormValid.value) {
    emit('updateUserInfo', userInfo.value);
    emit('next');
  }
};
</script>

<template>
  <div class="user-information">
    <h2>Personal Information</h2>
    <form @submit.prevent="handleNext" class="info-form">
      <div class="form-group">
        <label for="name">Full Name</label>
        <input
          id="name"
          v-model="userInfo.name"
          type="text"
          required
          placeholder="Enter your full name"
        >
      </div>
      
      <div class="form-group">
        <label for="email">Email</label>
        <input
          id="email"
          v-model="userInfo.email"
          type="email"
          required
          placeholder="Enter your email"
        >
      </div>
      
      <div class="form-group">
        <label for="phone">Phone Number</label>
        <input
          id="phone"
          v-model="userInfo.phone"
          type="tel"
          required
          placeholder="Enter your phone number"
        >
      </div>

      <div class="form-group">
        <label for="user_id">Id Number</label>
        <input
          id="user_id"
          v-model="userInfo.email"
          type="text"
          required
          placeholder="Enter your email"
        >
      </div>

      <div class="button-container">
        <button type="button" class="back-button" @click="emit('back')">
          Back
        </button>
        <button type="submit" class="next-button" :disabled="!isFormValid">
          Next
        </button>
      </div>
    </form>
  </div>
</template>

<style scoped>
.user-information {
  padding: 20px;
  max-width: 500px;
  margin: 0 auto;
}

.info-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

label {
  font-weight: 500;
}

input {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

.button-container {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.back-button {
  background-color: #666;
}

.next-button {
  background-color: #42b883;
}

button {
  color: white;
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