<template>
    <nav class="bg-blue-500 p-4">
      <div class="container mx-auto flex items-center justify-between">
        <!-- Profile Picture Placeholder -->
        <div class="flex items-center space-x-4">
          <div class="w-12 h-12 bg-gray-300 rounded-full"></div>
          <div class="text-white font-semibold">User Name</div>
        </div>
  
        <!-- Navigation Links -->
        <ul class="flex items-center space-x-8 text-white">
          <li><router-link to="/home">Home</router-link></li>
          <li><router-link to="/questions">Topics</router-link></li>
          <li><router-link to="/performance">Your Performance</router-link></li>
          <li><a href="#">Logout</a></li>
        </ul>
      </div>
    </nav>
  </template>
  
  <script>
  export default {
    name: 'Navbar',
  };
  </script>