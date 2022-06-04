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
import type { ChartOptions, Plugin } from "chart.js";
import type { TChartData } from "vue-chartjs/dist/types";
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

let data = [23, 29, 58, 75, 33, 30, 73, 49];
let labels = [
  "23%;Now",
  "29%;11:00",
  "58%;12:00",
  "75%;13:00",
  "33%;14:00",
  "30%;15:00",
  "73%;16:00",
  "49%;17:00",
];

const chartData = {
  labels: labels,
  datasets: [
    {
      label: "Forecast",
      data: data,
      fill: true,
      backgroundColor: "rgba(71, 183,132,.5)",
      tension: 0.3,
    },
    {
      label: "ForecastTest",
      xAxisID: "xTwo",
    },
  ],
} as TChartData<"line">;

//https://stackoverflow.com/questions/28716464/hiding-labels-on-y-axis-in-chart-js --> Answer Merouane T.
const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  events: [],
  scales: {
    y: {
      ticks: {
        display: false,
        stepSize: 10,
      },
      grid: {
        display: false,
      },
      min: 0,
      max: 100,
    },
    x: {
      grid: {
        display: true,
      },
      position: "bottom",
      ticks: {
        callback: (index: number) => {
          return labels[index].split(";")[0];
        },
      },
    },
    xTwo: {
      position: "top",
      grid: {
        display: true,
      },
      ticks: {
        callback: (index: number) => {
          return labels[index].split(";")[1];
        },
      },
    },
  },
} as ChartOptions<"line">;
</script>
