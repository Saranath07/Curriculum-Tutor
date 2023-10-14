<template>
    <div class="bg-gray-100 flex items-center justify-center h-screen">
      <div class="bg-white p-8 rounded-lg shadow-md w-1/3">
        <h1 class="text-2xl font-bold mb-4">Login</h1>
        <form>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="username">Username</label>
            <input class="border rounded w-full py-2 px-3" type="text" id="username" name="username" placeholder="Username" />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="password">Password</label>
            <input class="border rounded w-full py-2 px-3" type="password" id="password" name="password" placeholder="Password" />
          </div>
          <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" type="submit">Login</button>
  
        </form>
      </div>
    </div>
  </template>
  