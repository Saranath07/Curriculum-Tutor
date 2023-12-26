<template>
    <nav class="bg-blue-500 p-4">
      <div class="container mx-auto flex items-center justify-between">
        <!-- Profile Picture Placeholder -->
        <div class="flex items-center space-x-4">
          <div>
             <AvatarRoot class="bg-blackA3 inline-flex h-[45px] w-[45px] select-none items-center justify-center overflow-hidden rounded-full align-middle">
      <AvatarImage
        class="h-full w-full rounded-[inherit] object-cover"
        :src="imgURL"
        alt="Colm Tuite"
      />
      
    </AvatarRoot></div>
          <div class="text-white font-semibold">{{ username }}</div>
        </div>
        <div class = "lg:hidden">
          <button @click="toggleNav"><svg width="24" height="24" viewBox="0 0 24 24" class="stroke-white stroke-2"><path class="transition-all duration-500 ease-in-out" :d="navOpen ? `M 1 1 L 23 23 M 1 23 L 23 1 M 1 23 L 23 1` : `M 1 2 L 23 2 M 1 12 L 23 12 M 1 22 L 23 22`"></path></svg></button>
        </div>
        <!-- Navigation Links -->
        <ul :class="`flex flex-col lg:flex-row items-center gap-8 bg-zinc-200 lg:bg-transparent text-black uppercase font-semibold text-sm absolute lg:translate-x-0 lg:static top-20 p-4 right-0 transition-all transform duration-500 ease-in-out ${navOpen ?  `translate-x-0` : `translate-x-[200rem]`}`">
          <li><a href="/home">Home</a></li>
          <li><a href="/topics">Topics</a></li>
          <li><a href="/performance">Your Performance</a></li>
          <li><button @click="logout">LOGOUT</button></li>
        </ul>
      </div>
    </nav>
  </template>
  
  <script setup lang="ts">
  import { AvatarFallback, AvatarImage, AvatarRoot } from 'radix-vue';
  import { ref } from "vue";
  import { useRoute, useRouter } from "vue-router";
  const navOpen = ref(false)
  const router = useRouter()
  const toggleNav = () => {navOpen.value = !navOpen.value}
  // Assuming you want to retrieve an item with the key 'user'



const username = ref('');
const imgURL = ref('')

// Check if the item exists
const userString = localStorage.getItem('user');
if (userString) {
  // If it exists, parse the JSON string into an object
  const user = JSON.parse(userString);
  
  // Update the value of the username ref
  username.value = user.username;
  imgURL.value = `http://localhost:5000${user.imgUrl}`
  console.log(imgURL)
  
  console.log('User:', user);
} else {
  console.log('User information not found in localStorage');
}

  function logout(){
    localStorage.clear();
    router.push("/login")
  }
  </script>