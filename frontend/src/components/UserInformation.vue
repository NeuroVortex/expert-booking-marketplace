<script setup lang="ts">
import { ref, computed } from 'vue';
import {UserInfo} from '../types';

const emit = defineEmits(['next', 'back', 'updateUserInfo']);

const userInfo = ref<UserInfo>({
  personalInfo: {
    firstName: "",
    lastName: "",
    email: "",
    phone: "",
    identityNumber: ""
},
  address: {
    province: "",
    city: "",
    homeNumber: "",
    firstAddressLine: "",
    secondAddressLine: null,
    zipCode: ""
}
});

const isFormValid = computed(() => {
  return userInfo.value.personalInfo.firstName &&
         userInfo.value.personalInfo.lastName &&
         userInfo.value.personalInfo.email &&
         userInfo.value.personalInfo.phone;
});

const handleNext = () => {
  if (isFormValid.value) {
    emit('updateUserInfo', userInfo.value);
    emit('next');
  }
};
</script>

<template>
  <div class="user-information-container">
    <div class="personal-information">
    <h2>Personal Information</h2>
    <form @submit.prevent="handleNext" class="info-form">
      <div class="profile-container">
        <input
          id="first-name"
          v-model="userInfo.personalInfo.firstName"
          type="text"
          required
          placeholder="First name"
        >
        <input
          id="last-name"
          v-model="userInfo.personalInfo.lastName"
          type="text"
          required
          placeholder="Last name"
        >
      </div>
      <div class="email-phone-container">
        <input
          id="email"
          v-model="userInfo.personalInfo.email"
          type="email"
          required
          placeholder="Email"
        >
        <input
          id="phone"
          v-model="userInfo.personalInfo.phone"
          type="tel"
          required
          placeholder="Phone number"
        >
      </div>
      <div class="form-group">
        <input
          id="user_id"
          v-model="userInfo.personalInfo.identityNumber"
          type="text"
          required
          placeholder="Id number"
        >
      </div>
      <h2>Address</h2>
      <div class="address-container">
        <div class = "State-city-container">
            <input
            id="state/province"
            v-model="userInfo.address.province"
            type="text"
            required
            placeholder="State/Province"
          >
          <input
            id="city"
            v-model="userInfo.address.city"
            type="text"
            required
            placeholder="City"
          >
        </div>
        <div class="form-group">
          <input
            id="first-address"
            v-model="userInfo.address.firstAddressLine"
            type="text"
            required
            placeholder="Address Line No. 1"
          >
          <input
            id="second-address"
            v-model="userInfo.address.secondAddressLine"
            type="text"
            placeholder="Address Line No. 2"
          >
          </div>
        <div class="home-container">
          <input
            id="Number"
            v-model="userInfo.address.homeNumber"
            type="text"
            required
            placeholder="Home/Number"
          >
          <input
            id="zip_code"
            v-model="userInfo.address.zipCode"
            type="text"
            required
            placeholder="Zip code"
          >
        </div>
    </div>

      <div class="button-container">
        <button type="button" class="back-button" @click="emit('back')">
          Back
        </button>
        <button type="submit" class="next-button" :disabled="!isFormValid">
          Book a reservation
        </button>
      </div>
    </form>
  </div>
  </div>
</template>

<style scoped>

.user-information-container {
  display: flex;
  padding: 20px;
  max-width: 500px;
  margin: 0 auto;
}

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

.profile-container {
  display: flex;
  flex-direction: row;
  gap: 20px;
}

.email-phone-container {
  display: flex;
  flex-direction: row;
  gap: 20px;
}

.address-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.State-city-container {
  display: flex;
  flex-direction: row;
  gap: 20px;
}

.home-container {
  display: flex;
  flex-direction: row;
  gap: 20px;
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