<template>
    <div class="page-container">
      <h1 style="text-align: center; font-weight: bold;">Your Performance</h1>
      <table class="performance-table">
        <thead>
          <tr>
            <th>Topic Name</th>
            <th>Number of Questions Solved</th>
            <th>Mastered</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(topic, index) in performanceData" :key="index">
            <td>{{ topic.name }}</td>
            <td>{{ topic.questionsSolved }}</td>
            <td :class="{ mastered: topic.mastered }">{{ topic.mastered ? 'Yes' : 'No' }}</td>
          </tr>
        </tbody>
      </table>
      <div class="bar-chart-container">
        <canvas id="barChart" width="10px" height="20px"></canvas>
      </div>
    </div>
    
  </template>
  
  <script setup>
  import { ref, onMounted, watch } from "vue";
  import { Chart, registerables } from 'chart.js';

  import axios from 'axios';

  const userString = localStorage.getItem('user');
  const user = JSON.parse(userString);
  axios.defaults.baseURL = 'http://localhost:5000';
  const token = user.access_token;
 
console.log(`Token : ${token}`)

const performanceData = ref([]);

if (!token){
  router.push("/login")
}
  Chart.register(...registerables);
  
  async function getPerformance(){
      try{
        
        const response = await  axios.get(`/api/performance`,  {
        headers: {
          'Authorization': `Bearer ${token}`
        },
        
      })
      performanceData.value = response.data
      console.log(response.data)

      }catch(e){
        error.data = e;
      }
  }
console.log(performanceData)
  
  let barChart;
  
  onMounted(() => {
    getPerformance();
  });

  watch(performanceData, () => {
  createBarChart();
});
  
  function createBarChart() {
    const canvas = document.getElementById('barChart');
    const ctx = canvas.getContext("2d");
  
    const chartData = {
      labels: performanceData.value.map(topic => topic.name),
      datasets: [{
        label: 'Number of Questions Solved',
        data: performanceData.value.map(topic => topic.questionsSolved),
        backgroundColor: performanceData.value.map(topic => topic.mastered ? 'rgba(0, 255, 0, 0.5)' : 'rgba(255, 0, 0, 0.5)'),
        borderColor: performanceData.value.map(topic => topic.mastered ? 'rgba(0, 255, 0, 1)' : 'rgba(255, 0, 0, 1)'),
        borderWidth: 1
      }]
    };
    console.log("chart data")
    console.log(chartData)
  
    const chartOptions = {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    };
  
    barChart = new Chart(ctx, {
      type: 'bar',
      data: chartData,
      options: chartOptions
    });
  }
  </script>

  <style scoped>
 .performance-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.performance-table th, .performance-table td {
  border: 1px solid #ddd;
  padding: 10px;
  text-align: left;
}

.performance-table th {
  background-color: #f2f2f2;
}

.performance-table td:nth-child(3).mastered {
  color: green;     /* Color for mastered topics */
  font-weight: bold;
}

.performance-table td:nth-child(3):not(.mastered) {
  color: red;       /* Color for non-mastered topics */
  font-weight: bold;
}

  .page-container{
    margin-top: 10px;
    margin-bottom: 50px;
    margin-left: 30px;
    margin-right: 30px;
}
.bar-chart-container {
  width: 40%; /* Adjust the width as needed */
  margin-top: 50px;
  margin-left: 450px;
  height: 50%;
  text-align: center;
  justify-content: center;
}
  /* Add more styles as needed */
  </style>