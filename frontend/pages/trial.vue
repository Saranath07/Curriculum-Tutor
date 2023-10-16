<template>
    <div>
      {{ msg }}
      <button @click="increment">Count is: {{ count }}</button>
      <div>
        {{ passwordMismatch }}
      </div>
    </div>
  </template>
  
  <script setup lang="ts" >
  
  import { ref, onMounted, watch } from 'vue';
  
  const msg: String = "Hello";
  
  const count = ref(0);
  function increment(): void {
    count.value += 1;
    console.log(count.value);
  }


  const password = ref('');
  const confirmPassword = ref('');
  const passwordMismatch = ref(false);

const validatePasswords = (newPassword: String, newConfirmPassword: String) => {
    if (password !== confirmPassword) {
        passwordMismatch.value = true;
      } else {
        passwordMismatch.value = false;
      }
  
};


watch([password, confirmPassword], ([newPassword, newConfirmPassword]: [string, string]) => {
  validatePasswords(newPassword, newConfirmPassword);
});



  onMounted(() => {
    
    console.log(`The initial count is ${count}.`);
  })
  
  
  
  
  </script>
  