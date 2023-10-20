<template>
    <div>
        <!-- Hello {{ $route.params.id }} -->
        <article class="prose prose-md mx-auto flex flex-col gap-4">

           
          
            <ContentDoc path="/question" />
        
            <div v-for="option in options">
            <input type="radio" id="option" name="option" value="HTML">
<label for="html">option</label><br>
</div>
            <button
                class="px-2 py-4 w-24 transition duration-500 ease-in-out transform hover:-translate-y-1 bg-rose-600 text-white uppercase text-xs rounded-md">Submit</button>
           
        </article>
    </div>
</template>

<script setup>

const q_no = ref("")
const fs = require('fs') 
const question = ref("")
const route = useRoute()
q_no.value = route.params.id

question.value = `


# Question ${q_no.value}
What is the decimal value of $\\dfrac{1}{3}?$ 
`


      
     
      fs.writeFile('content/question.md', question.value, (err) => { 
            
      
          if (err) throw err; 
      }) 
    
   const options = ref([
    'Option 1',
    'Option 2',
    'Option 3',
    'Option 4'
   ])



</script>


