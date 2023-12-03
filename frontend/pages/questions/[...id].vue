<template>
    <div class="page-container">
      <article class="prose prose-md mx-auto flex flex-col gap-4">
        <MDC :value="question" tag="article" />
        <img :src="imgPath" class="question-image" alt="Question Picture" >
        <div class="flex gap-4" v-for="option in options">
          <input type="radio" :id="option" name="option" :value="option">
          <label :for="option">
            <MDC :value="option" tag="span" />
          </label>
        </div>
  
        <div>
          <button
            class="px-2 py-4 w-24 transition duration-500 ease-in-out transform hover:-translate-y-1 bg-yellow-600 text-white uppercase text-xs rounded-md" 
            @click="previousPage">
           Previous

          </button>
          
          <button
                    class="px-2 py-4 w-24 transition duration-500 ease-in-out transform hover:-translate-y-1 bg-green-600 text-white uppercase text-xs rounded-md"
                    style="margin-left: 50px;" @click="nextpage">Next</button>

          <button
            class="px-2 py-4 w-24 transition duration-500 ease-in-out transform hover:-translate-y-1 bg-rose-600 text-white uppercase text-xs rounded-md"
            style="margin-left: 300px;">
            Submit
          </button>
  
          <!-- <button
            class="px-2 py-4 w-24 transition duration-500 ease-in-out transform hover:-translate-y-1 bg-blue-600 text-white uppercase text-xs rounded-md"
            @click="showNumberLine" style="margin-left: 50px;"
          >
            Number Line

          </button> -->
          

         
            
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
  import { useRoute, useRouter } from "vue-router";
  
  const question = ref("");
  const route = useRoute();
  const q_no = ref(route.params.id);
  const show = ref(false);
  const router = useRouter()
  const imgPath = ref("")
  imgPath.value = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQttuTvK6dGgaC7yHWk1bPmCTtuo-6-b0kB-SPRz1EFPUFhZaqZRrV_LJNKaf8c8-cnxY&usqp=CAU"

  console.log("Question:", q_no.value);
  
  function showNumberLine() {
    show.value = true;
  }
  
  function closeNumberLine() {
    show.value = false;
  }

  function nextpage(){
    
    const newUrl = `/questions/${Number(q_no.value) + 1}`;
    console.log(newUrl)
    router.push(newUrl);
  }
  function previousPage(){
    const qNo = Number(q_no.value) - 1;
    if (qNo > 0){
      const newUrl = `/questions/${qNo}`;
      console.log(newUrl)
      router.push(newUrl);
    }else{
      console.log('No questions behind')
      alert('No questions behind');
    }
  }
  
  question.value = `# Question ${q_no.value} \
  
  What does this fraction represent?`;
  
  const options = ref(["$\\dfrac{1}{2}$", "$\\dfrac{1}{4}$", "$\\dfrac{2}{5}$"]);
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
  .question-image {
  max-width: 40%; /* Ensure the image doesn't exceed its container */
  height: 200px;    /* Maintain the aspect ratio of the image */
  border: 1px solid #ddd; /* Add a border for better visibility */
  border-radius: 5px; /* Add border radius for rounded corners */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add a subtle box shadow */
  margin-bottom: 10px; /* Add some space below the image */
}
.page-container{
  margin-top: 10px;
  margin-bottom: 50px;
}
  </style>
  