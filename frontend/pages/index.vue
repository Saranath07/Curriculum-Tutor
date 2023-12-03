<template>
    <div>
      {{ msg }}
      <button @click="increment">Count is: {{ count }}</button>
    </div>
  </template>
  
  <script setup lang="ts" >
  
//   import { ref, onMounted } from 'vue';
  
  const msg: String = "Hello";
  
  const count = ref(0);
  function increment(): void {
    count.value += 1;
    console.log(count.value);
  }
  
  onMounted(() => {
    
    console.log(`The initial count is ${count}.`);
  })
  
  
  
  
  </script>
  
