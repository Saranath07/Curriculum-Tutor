<template>
    <div class="number-line">
      <div
        v-for="number in range"
        :key="number"
        :class="{ 'highlighted': number == highLighted }"
        class="tick"
      >
     <!-- <div :value="1"></div> -->
      <MDC :value="number" tag="span" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      min: Number,
      max: Number,
      step: Number,
      highlightedNumber: Number,
    },
    data(){
        highLighted : '' 
    },
    computed: {
      range() {
        const range = [];
        this.highLighted = `$\\dfrac{${this.highlightedNumber}}{${this.max}}$`
        // `$\\dfrac{${this.highlightedNumber}{${this.max}}}$`
        range.push(`$0$`)
        for (let i = this.min+1; i <= this.max-1; i += this.step) {
          
          range.push(`$\\dfrac{${i}}{${this.max}}$`);
        }
        range.push(`$1$`)
        return range;
      },
    },
  };
  </script>
  
  <style scoped>
  .number-line {
    display: flex;
    justify-content: space-between;
    border: 2px solid #00CCAA;
   
    background: linear-gradient(#00CCAA);
    padding: 10px;
  }
  
  .tick {
    flex: 1;
    text-align: center;
    transition: background-color 0.3s;
    background-color: #FFF;
    color: #333;
    font-family: 'Arial', sans-serif;
    font-size: 16px;
    padding: 10px 0;
  }
  
  .highlighted {
    background-color: #00CCAA;
    color: #333;
    font-weight: bold;
  }
  </style>
  

 
