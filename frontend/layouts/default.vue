<template>
    <div class="min-h-screen">
        <NavBar v-if="route.path !== `/login` && route.path !== `/register`" />
        <main class=""><slot></slot></main>
    </div>
</template>
<script setup lang="ts">
const route = useRoute()
console.log(route.path)
</script>