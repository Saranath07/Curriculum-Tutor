<template>
  <div>

    <div class="fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 flex items-center justify-center" v-if="error">
      <div class="bg-white p-8 rounded-md">
      <h1 style="color: black;">{{ error }} Try contacting the administrator.</h1>
    </div>
  </div>

  <div v-if="attempted">
    <article class="prose prose-md mx-auto flex flex-col gap-4">
        <MDC :value="question" tag="article" />
        <img v-if="showImg" :src="imgPath" class="question-image" alt="Question Picture" >
        <div class="flex gap-4" v-for="option in options" :key="option">
          <input
            type="radio"
            :id="option"
            name="option"
            :value="option"
            v-model="selectedOption"
            :class="{ 'correct-option': isCorrectOption(option), 'incorrect-option': isIncorrectOption(option) }"
            :disabled="attempted"
          />
          <label :for="option">
            <MDC :value="option" tag="span" />
          </label>
        </div>

        <!-- Display messages based on attempted status -->
        <div v-if="attempted">
          <p v-if="status" style="color: green;">You got it right!. The correct answer is <MDC :value="correctOption"  /></p>
          <p v-else-if="!status" style="color: red;">You missed it. The correct answer is  <MDC :value="correctOption" /></p>
        </div>
        <div style="margin-bottom: 100px;">
        <button
            class="px-2 py-4 w-24 transition duration-500 ease-in-out transform hover:-translate-y-1 bg-yellow-600 text-white uppercase text-xs rounded-md" 
            @click="previousPage">
           Previous

          </button>
        <button
                    class="px-2 py-4 w-24 transition duration-500 ease-in-out transform hover:-translate-y-1 bg-green-600 text-white uppercase text-xs rounded-md"
                    style="margin-left: 50px;" @click="nextpage">Next</button>
                  </div>
          <!-- <button
            class="px-2 py-4 w-24 transition duration-500 ease-in-out transform hover:-translate-y-1 bg-rose-600 text-white uppercase text-xs rounded-md"
            style="margin-left: 300px;"
            @click="submit"
            :disabled="attempted"
          >
            Submit
          </button> -->
        
      </article>
  </div>
  
    <div v-else class="page-container">
      <article class="prose prose-md mx-auto flex flex-col gap-4">
        <MDC :value="question" tag="article" />
        <img v-if="showImg" :src="imgPath" class="question-image" alt="Question Picture" >
        <div class="flex gap-4" v-for="option in options">
          <input type="radio" :id="option" name="option" :value="option" v-model="selectedOption">
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
          
          

          <!-- <button
            class="px-2 py-4 w-24 transition duration-500 ease-in-out transform hover:-translate-y-1 bg-rose-600 text-white uppercase text-xs rounded-md"
            style="margin-left: 300px;">
            Submit
          </button>
          
   -->
   <button
            class="px-2 py-4 w-24 transition duration-500 ease-in-out transform hover:-translate-y-1 bg-rose-600 text-white uppercase text-xs rounded-md"
            style="margin-left: 100px;" @click="submit">
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
          <div class="box">
          <button class="close-button" @click="closeNumberLine">Close</button>
          <NumberLine :min="0" :max="25" :step="1" :highlightedNumber="10" />
        </div>
      </div>
      </div>
    </div>
  </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
import axios from 'axios';

 
  
axios.defaults.baseURL = 'http://localhost:5000';

const topics = ref([]);
const expandedTopics = ref([]);
const userString = localStorage.getItem('user');
  const user = JSON.parse(userString);
  const question = ref("");
  const route = useRoute();
  const q_no = ref(route.params.id);
  const show = ref(false);
  const router = useRouter()
  const imgPath = ref("")
  const error = ref(0)
  const selectedOption = ref("")
  const correctOption = ref("")
  const showImg = ref(false);
  
  // Access the access token property from the user object
  const token = user.access_token;
  let ques = '';
  let opt = '';
  const attempted = ref(false);
  const status = ref(false);
console.log(`Token : ${token}`)

if (!token){
  router.push("/login")
}


  try{
  const response = await axios.get(`/api/questions/${Number(q_no.value)}`,  {
        headers: {
          'Authorization': `Bearer ${token}`
        },
        
      })
      console.log(`Response Data : ${response.data.ques_img}`)

      ques = response.data.question
      opt = response.data.options
      if (response.data.ques_img){
        imgPath.value = `http://localhost:5000${response.data.ques_img}`
        showImg.value = true
      }
      attempted.value = response.data.attempted
      console.log(response.data.att)
      if (attempted.value){
        status.value = response.data.status
        correctOption.value = response.data.correct_option
      }
      
    }catch(e){
      error.value = e
      console.log(e)
    }



// onMounted(() => {
//   // This code will be executed when the component is mounted
//   console.log('Component is mounted!');
//   getQuestions();
// });

  
  
  // imgPath.value = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQttuTvK6dGgaC7yHWk1bPmCTtuo-6-b0kB-SPRz1EFPUFhZaqZRrV_LJNKaf8c8-cnxY&usqp=CAU"

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

  function isCorrectOption(option) {
    console.log(option, selectedOption.value)
  return attempted && status && option === selectedOption.value;
}

function isIncorrectOption(option) {
  return attempted && !status && option === selectedOption.value;
}

  async function submit(){
    console.log('submitting...')
    console.log(selectedOption.value)
    
    try{
  const response = await axios.post(`/api/evaluate/${Number(q_no.value)}`,  {
    'studentOption' : selectedOption.value
  },
  {
        headers: {
          'Authorization': `Bearer ${token}`
        },
        
      })
      console.log(response.data)
      location.reload()
      
    }catch(e){
      error.value = 1
      console.log(e)
    }

  }
  let ops = opt.split(',')
  console.log(ops)
  question.value = `# Question ${q_no.value} \
  
  ${ques}`;
  
  const options = ref(ops);
  </script>
  
  <style scoped>
  .overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); 
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999; 
}
  .correct-option {
  background-color: green;
}

.incorrect-option {
  background-color: red;
}

.correct-option-label {
  color: white; /* Set text color for correct options */
}

.incorrect-option-label {
  color: white; /* Set text color for incorrect options */
}
.box {
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  text-align: center;
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

.overlay {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7); /* Adjust the transparency as needed */
  z-index: 1000; /* Ensure the overlay appears on top of other content */
}
  </style>
  