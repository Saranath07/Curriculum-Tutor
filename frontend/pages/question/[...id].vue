<template>
    <div>
        Hello {{ $route.params.id }}
        <article class="prose prose-md mx-auto flex flex-col gap-4">
          
            <ContentDoc path="/question" />
            <button
                class="px-2 py-4 w-24 transition duration-500 ease-in-out transform hover:-translate-y-1 bg-rose-600 text-white uppercase text-xs rounded-md">Submit</button>
           
        </article>
    </div>
</template>

<script setup>




</script>


