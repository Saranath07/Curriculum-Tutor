<template>
    <div class="bg-gray-100 flex items-center justify-center h-screen">
      <div class="bg-white p-8 rounded-lg shadow-md w-1/3">
        <h1 class="text-2xl font-bold mb-4">Registration</h1>
        <form>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="name">Name</label>
            <input class="border rounded w-full py-2 px-3" type="text" id="name" name="name" placeholder="Name" />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="email">Email</label>
            <input class="border rounded w-full py-2 px-3" type="email" id="email" name="email" placeholder="Email" />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="school">School Name</label>
            <input class="border rounded w-full py-2 px-3" type="text" id="school" name="school" placeholder="School Name" />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="password">Password</label>
            <input class="border rounded w-full py-2 px-3" type="password" id="password" name="password" placeholder="Enter Password" />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="confirm-password">Confirm Password</label>
            <input class="border rounded w-full py-2 px-3" type="confirm-password" id="confirm-password" name="confirm-password" placeholder="Confirm Password" />
          </div>
          <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" type="submit">Register</button>
        </form>
        <p class="mt-4 text-gray-600">
          Already have an account? <router-link to="/login" class="text-blue-500 hover:underline">Login</router-link>
        </p>
      </div>
    </div>
  </template>
  