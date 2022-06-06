<template>
  <div v-if="forecast" class="card h-full w-full shadow-sm bg-[#fdfff9]">
    <div class="card-body p-5">
      <h2 class="text-xl text-center text-primary-focus">Hourly Temperature</h2>
      <div class="card card-side">
        <div class="card-body">
          <Line
            ref="lineChart"
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
import { ref, watch, onMounted } from "vue";
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
  type ChartData,
  type ChartDataset,
  type ChartOptions,
} from "chart.js";
import ChartJsPluginDataLabelsfrom from "chartjs-plugin-datalabels";

import { weatherDataStore } from "@/stores/weatherDataStore";

const lineChart = ref<InstanceType<typeof Line>>();
const { forecast } = storeToRefs(weatherDataStore());

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

const props = defineProps({
  /*data: {
    type: Array as PropType<number[]>,
    default: [] as number[],
  },*/
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

let data = storeToRefs(weatherDataStore()).getHourlyTemp;

const chartData = ref<ChartData<"line">>({
  datasets: [] as ChartDataset<"line">[],
});

watch(data, () => {
  setChartData();
});

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

function setChartData(): void {
  const updatedChartData = {
    labels: labels,
    datasets: [
      {
        label: "Forecast",
        data: data.value,
        fill: true,
        pointBackgroundColor: "rgba(235,195,81,1)",
        pointBorderColor: "rgba(235,195,81,1)",
        backgroundColor: "rgba(240,210,125,1)",
        tension: 0.3,
      },
    ],
  } as ChartData<"line">;

  chartData.value = { ...updatedChartData };
}

const chartOptions = {
  animation: false,
  events: [],
  maintainAspectRatio: false,
  responsive: true,
  layout: {
    padding: {
      top: 25,
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
      //max: 110,
    },
    x: {
      grid: {
        display: false,
      },
      position: "bottom",
    },
  },
  plugins: {
    datalabels: {
      anchor: "end",
      align: "top",
      offset: -2,
      color: "black",
      //textAlign: "left",
      font: {
        size: 14,
      },
      formatter: function (value: string) {
        // context: Object
        return value + "%"; //return context.chart.data.labels[context.dataIndex]; -> gibt die label namen zurück
      },
    },
  },
} as ChartOptions<"line">;

onMounted(() => {
  setChartData();
});
</script>
