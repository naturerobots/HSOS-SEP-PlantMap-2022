<template>
  <Line
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="chartId"
    :plugins="plugins"
    :css-classes="cssClasses"
    :styles="styles"
    :width="width"
    :height="height"
  />
</template>

<script setup lang="ts">
import type { PropType } from "vue";
import type { Plugin } from "chart.js";
import { Line } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  LineElement,
  LinearScale,
  PointElement,
  CategoryScale,
  Filler,
} from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  Filler,
  LineElement,
  LinearScale,
  PointElement,
  CategoryScale
);

defineProps({
  chartId: {
    type: String,
    default: "line-chart",
  },
  width: {
    type: Number,
    default: 400,
  },
  height: {
    type: Number,
    default: 100,
  },
  cssClasses: {
    type: String,
    default: "",
  },
  styles: {
    type: Object as PropType<Partial<CSSStyleDeclaration>>,
    default: {} as Partial<CSSStyleDeclaration>,
  },
  plugins: {
    type: Array as PropType<Plugin<"line">[]>,
    default: [] as Plugin<"line">[],
  },
});

const chartData = {
  labels: ["January", "February", "March", "April", "May", "June", "July"],
  datasets: [
    {
      label: "Data One",
      data: [40, 39, 10, 40, 39, 80, 40],
      fill: true,
      backgroundColor: "rgba(71, 183,132,.5)",
      tension: 0.3,
    },
  ],
};

//https://stackoverflow.com/questions/28716464/hiding-labels-on-y-axis-in-chart-js --> Answer Merouane T.
const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: {
      ticks: {
        display: false,
      },
      grid: {
        display: false,
      },
    },
    /*x: {
            grid: {
                display: false
            }
        },*/
  },
};
</script>
