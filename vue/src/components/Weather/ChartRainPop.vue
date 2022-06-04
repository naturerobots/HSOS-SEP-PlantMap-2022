<template>
  <div v-if="weather.current" class="card h-full w-full shadow-sm bg-[#fdfff9]">
    <div class="card-body p-5">
      <h2 class="text-xl text-center text-primary-focus">Rain pop</h2>
      <div class="card card-side">
        <div class="card-body">
          <Line
            :chart-options="chartOptions"
            :chart-data="chartData"
            :chart-id="chartId"
            :width="width"
            :height="height"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { TChartData } from "vue-chartjs/dist/types";
import { storeToRefs } from "pinia";
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
import ChartJsPluginDataLabelsfrom from "chartjs-plugin-datalabels";

import { weatherStore } from "@/stores/weatherStore";

//const lineChart = ref<InstanceType<typeof Line>>();
const { weather } = storeToRefs(weatherStore());

ChartJS.register(
  Title,
  Tooltip,
  Filler,
  ChartJsPluginDataLabelsfrom,
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
});

let data = [23, 29, 58, 75, 33, 100, 73, 49];
let labels = [
  "Now",
  "11:00",
  "12:00",
  "13:00",
  "14:00",
  "15:00",
  "16:00",
  "17:00",
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
  ],
} as TChartData<"line">;

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  events: [],
  layout: {
    padding: {
      top: 20,
    },
  },
  scales: {
    y: {
      ticks: {
        display: false,
        stepSize: 10,
      },
      grid: {
        display: false,
        drawBorder: false,
      },
      min: 0,
      //max: 100,
    },
    x: {
      grid: {
        display: false,
      },
      position: "bottom",
      ticks: {
        /*callback: (index: number) => {
          return labels[index].split(";")[1];
        },*/
      },
    },
  },
  plugins: {
    datalabels: {
      anchor: "end",
      align: "top",
      offset: "-2",
      color: "black",
      //textAlign: "left",
      font: {
        size: 10,
      },
      formatter: function (value: string) {
        // context: Object
        return value + "%"; //return context.chart.data.labels[context.dataIndex]; -> gibt die label namen zurück
      },
    },
  },
} as any; //don't know the right type
</script>
