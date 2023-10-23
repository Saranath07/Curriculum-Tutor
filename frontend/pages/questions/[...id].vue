<template>
    <div>
      <article class="prose prose-md mx-auto flex flex-col gap-4">
        <MDC :value="question" tag="article" />
  
        <div class="flex gap-4" v-for="option in options">
          <input type="radio" :id="option" name="option" :value="option">
          <label :for="option">
            <MDC :value="option" tag="span" />
          </label>
        </div>
  
        <div>
          <button
            class="px-2 py-4 w-24 transition duration-500 ease-in-out transform hover:-translate-y-1 bg-rose-600 text-white uppercase text-xs rounded-md"
          >
            Submit
          </button>
  
          <button
            class="px-2 py-4 w-24 transition duration-500 ease-in-out transform hover:-translate-y-1 bg-blue-600 text-white uppercase text-xs rounded-md"
            @click="showNumberLine" style="margin-left: 50px;"
          >
            Number Line
          </button>

          <button
                    class="px-2 py-4 w-24 transition duration-500 ease-in-out transform hover:-translate-y-1 bg-green-600 text-white uppercase text-xs rounded-md"
                    style="margin-left: 300px;">Next</button>
            
        </div>
      </article>
  
      <div v-if="show">
        <div class="overlay">
          <button class="close-button" @click="closeNumberLine">Close</button>
          <NumberLine :min="0" :max="25" :step="1" :highlightedNumber="10" />
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from "vue";
  import { useRoute } from "vue-router";
  
  const question = ref("");
  const route = useRoute();
  const q_no = ref(route.params.id);
  const show = ref(false);
  
  function showNumberLine() {
    show.value = true;
  }
  
  function closeNumberLine() {
    show.value = false;
  }
  
  question.value = `# Question ${q_no.value} 
  What is the decimal value of $0.5?$`;
  
  const options = ref(["$\\dfrac{1}{2}$", "$\\dfrac{1}{4}$"]);
  </script>
  
  <style scoped>
  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 999;
  }
  
  .close-button {
    position: absolute;
    top: 10px;
    right: 10px;
    background: white;
    border: 1px solid #ccc;
    padding: 5px 10px;
    cursor: pointer;
  }
  </style>
  