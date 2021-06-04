<template>
  <canvas ref="myChart"></canvas>
</template>

<script>
import Chart from "chart.js";
export default {
  props: {
    info: {
      type: String
    },
    label: {
      type: Array,
    },
    chartData: {
      type: Array,
    },
  },
  mounted() {
    new Chart(this.$refs.myChart, {
      type: "bar",
      data: {
        labels: [
          "Jan",
          "Feb",
          "Mar",
          "Apr",
          "Mei",
          "Jun",
          "Jul",
          "Agu",
          "Sep",
          "Okt",
          "Nov",
          "Des",
        ],
        datasets: [
          {
            label: this.info,
            borderColor: "#F2994A",
            backgroundColor: 'rgba(144,238,144 , 0.9 )',
            data: this.chartData,
          },
        ],
      },
      options: {
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
              },
            },
          ],
        },
      },
    });
  },
};
</script>