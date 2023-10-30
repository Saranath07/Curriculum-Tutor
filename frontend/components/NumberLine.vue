<template>
  <div>
    <h1>Number Line Chart</h1>

    <div>
      <label for="numerator">Numerator:</label>
      <input type="number" v-model="numerator" min="0" step="10">
      <label for="denominator">Denominator:</label>
      <input type="number" v-model="denominator" min="1" step="10">
    </div>

    <canvas id="number-line-chart" ref="numberLineCanvas" width="400" height="100"></canvas>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watchEffect } from 'vue';
import {Chart, LinearScale, LineController, PointElement, LineElement} from 'chart.js';

    Chart.register(LinearScale, LineController, PointElement, LineElement)
    const numerator = ref(0);
    const denominator = ref(10);
    const numberLineCanvas = ref<HTMLCanvasElement | null>(null)

    let numberLineChart: Chart | null = null

    const updateNumberLine = () => {
      const selectedNumerator = numerator.value;
      const selectedDenominator = denominator.value;

      const dataPoints = [];
      const scale = Math.max(selectedNumerator, selectedDenominator);
      const maxScale = scale + 1;

      for (let i = 0; i <= maxScale; i++) {
        const x = i;
        dataPoints.push({ x, y: 0, highlighted: i === selectedNumerator || i === selectedDenominator });
      }

      if (numberLineChart) {
        numberLineChart.data.datasets[0].data = dataPoints;
        //@ts-ignore x
        numberLineChart.options.scales.x.max = maxScale;
        numberLineChart.update();
      } 
    };

    onMounted(() => {
      nextTick(() => {
        const selectedNumerator = numerator.value;
      const selectedDenominator = denominator.value;

      const dataPoints = [];
      const scale = Math.max(selectedNumerator, selectedDenominator);
      const maxScale = scale + 1;

      for (let i = 0; i <= maxScale; i++) {
        const x = i;
        dataPoints.push({ x, y: 0, highlighted: i === selectedNumerator || i === selectedDenominator });
      }
        numberLineChart = new Chart(numberLineCanvas.value as HTMLCanvasElement, {
          type: 'line',
          data: {
            datasets: [
              {
                data: dataPoints,
                borderColor: 'black',
                borderWidth: 2,
                pointRadius: 5,
                pointBackgroundColor: (ctx) => ctx.raw.highlighted ? 'red' : 'blue',
              },
            ],
          },
          options: {
            scales: {
              x: {
                type: 'linear',
                position: 'bottom',
                min: 0,
                max: maxScale,
              },
              y: {
                display: false,
              },
            },
          },
        });
      })
    });

    // Watch for changes in numerator and denominator
    watchEffect(updateNumberLine);

</script>

<style>
/* Add your CSS styles here */
#number-line-chart {
  margin-top: 20px;
}

.highlighted-point {
  background-color: yellow;
  radius: 8;
}
</style>
