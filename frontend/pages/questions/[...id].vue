<template>
    <div>
        <article class="prose prose-md mx-auto flex flex-col gap-4">
            
            <MDC :value="question" tag="article" />
            
            <div class="flex gap-4" v-for="option in options">
                <input type="radio" id="option" name="option" value="HTML">
                <label for="html">
                    <MDC :value="option" tag="span" />
        </label><br>
            </div>
            
            <div>
                <button
                    class="px-2 py-4 w-24 transition duration-500 ease-in-out transform hover:-translate-y-1 bg-rose-600 text-white uppercase text-xs rounded-md">Submit</button>

                <button
                    class="px-2 py-4 w-24 transition duration-500 ease-in-out transform hover:-translate-y-1 bg-green-600 text-white uppercase text-xs rounded-md"
                    style="margin-left: 300px;">Next</button>
            </div>
        </article>
    </div>
</template>

<script setup>



const question = ref("")
const route = useRoute()
const q_no = ref(route.params.id)


question.value = `


# Question ${q_no.value} 
What is the decimal value of $0.5?$ 
`


     
    //   const formula = ref('$$x = {-b \\pm \\sqrt{b^2-4ac} \\over 2a}.$$');


   const options = ref([
    ` $\\dfrac{1}{2}$`,
    ` $\\dfrac{1}{4}$`,
   ])

</script>