<template>
  <div class="bg-gray-100 flex items-center justify-center h-screen">
    <div class="bg-white p-8 rounded-lg shadow-md w-1/3">
      <h1 class="text-2xl font-bold mb-4">Login</h1>
      <form  @submit.prevent="login">
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="username">Email</label>
          <input class="border rounded w-full py-2 px-3" type="text" id="username" v-model="email" name="email" placeholder="Username" />
        </div>
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="password">Password</label>
          <input class="border rounded w-full py-2 px-3" type="password" id="password" v-model="password" name="password" placeholder="Password" />
        </div>
        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"  @click="login">Login</button>
      </form>
      <p class="mt-4 text-gray-600">
        Don't have an account? <router-link to="/register" class="text-blue-500 hover:underline">Register</router-link>
      </p>
    </div>
  
  </div>
</template>
  
  <script setup>

  import axios from 'axios';
  
   
    
    axios.defaults.baseURL = 'http://localhost:5000';
    import { ref } from "vue";
    import { useRoute, useRouter } from "vue-router";
    
    const email = ref("");
    const password = ref("");
    const route = useRoute();
    const error = ref("");
    const admin = ref(false);
    const router = useRouter()
    const access_token = ref("");
  
    async function login(){
        
        console.log(`${username.value}`);
        try {
            const response = await axios.post('/login', {
              email: email.value,
              password: password.value
            });
            
            // localStorage.setItem('access_token', response.data.access_token);
            if(response.data.role == "admin"){
              admin.value = true
            }
            console.log(response.data)
            const user = {
              username : response.data.username,
              role : response.data.role,
              admin : false,
              access_token : response.data.access_token
            }
            console.log(user)
            
            localStorage.setItem('user', JSON.stringify(user));
            router.push('/home')
    
  } catch (error) {
            error = error.response.data.error;
            console.log(error)
            alert(error)
           
          }
        }
  
  </script>