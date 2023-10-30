<template>
    <nav class="bg-blue-500 p-4">
      <div class="container mx-auto flex items-center justify-between">
        <!-- Profile Picture Placeholder -->
        <div class="flex items-center space-x-4">
          <div>
             <AvatarRoot class="bg-blackA3 inline-flex h-[45px] w-[45px] select-none items-center justify-center overflow-hidden rounded-full align-middle">
      <AvatarImage
        class="h-full w-full rounded-[inherit] object-cover"
        src="https://images.unsplash.com/photo-1492633423870-43d1cd2775eb?&w=128&h=128&dpr=2&q=80"
        alt="Colm Tuite"
      />
      
    </AvatarRoot></div>
          <div class="text-white font-semibold">User Name</div>
        </div>
        <div class = "lg:hidden">
          <button @click="toggleNav"><svg width="24" height="24" viewBox="0 0 24 24" class="stroke-white stroke-2"><path class="transition-all duration-500 ease-in-out" :d="navOpen ? `M 1 1 L 23 23 M 1 23 L 23 1 M 1 23 L 23 1` : `M 1 2 L 23 2 M 1 12 L 23 12 M 1 22 L 23 22`"></path></svg></button>
        </div>
        <!-- Navigation Links -->
        <ul :class="`flex flex-col lg:flex-row items-center gap-8 bg-zinc-200 lg:bg-transparent text-black uppercase font-semibold text-sm absolute lg:translate-x-0 lg:static top-20 p-4 right-0 transition-all transform duration-500 ease-in-out ${navOpen ?  `translate-x-0` : `translate-x-[200rem]`}`">
          <li><a href="/home">Home</a></li>
          <li><a href="/topics">Topics</a></li>
          <li><a href="/performance">Your Performance</a></li>
          <li><a href="#">Logout</a></li>
        </ul>
      </div>
    </nav>
  </template>
  
  <script setup lang="ts">
  import { AvatarFallback, AvatarImage, AvatarRoot } from 'radix-vue'
  const navOpen = ref(false)
  const toggleNav = () => {navOpen.value = !navOpen.value}
  </script>