<!--DO NOT DELETE-->
<template>
  <div v-if="forecast" class="card h-full w-full shadow-sm bg-[#fdfff9]">
    <div class="card-body p-5">
      <h2 class="text-xl text-center text-primary-focus">
        Hourly Wind deg/speed
      </h2>
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
import { ref, watch, onMounted, type Ref } from "vue";
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
import type { ChartData, ChartDataset, ChartOptions } from "chart.js";
import ChartJsPluginDataLabelsfrom, {
  type Context,
} from "chartjs-plugin-datalabels";

import { weatherDataStore } from "@/stores/weatherDataStore";
import type { TChartData } from "vue-chartjs/dist/types";

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

withDefaults(
  defineProps<{
    chartId: string;
    width: number;
    height: number;
  }>(),
  {
    chartId: "line-chart",
    width: 400,
    height: 100,
  }
);

let data: Ref<string[]> = storeToRefs(weatherDataStore()).getHourlyWind;
let labels: Ref<string[]> = storeToRefs(weatherDataStore()).getTimeLabels;

const chartData = ref<ChartData<"line">>({
  datasets: [] as ChartDataset<"line">[],
});

watch(data, () => {
  setChartData();
});

function setChartData(): void {
  const updatedChartData = {
    labels: labels?.value,
    datasets: [
      {
        label: "Forecast",
        data: data.value?.map((value) => 50),
        //fill: true,
        pointBackgroundColor: "rgba(0, 0, 0, 0)",
        pointBorderColor: "rgba(0, 0, 0, 0)",
        backgroundColor: "rgba(0, 0, 0, 0)",
        showLine: false,
      },
      {
        label: "ForecastTest",
        xAxisID: "xTwo",
      },
    ],
  } as TChartData<"line">;

  chartData.value = { ...updatedChartData };
}

const chartOptions = {
  animation: false,
  events: [],
  maintainAspectRatio: false,
  responsive: true,
  layout: {
    padding: {
      //top: 30,
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
      max: 100,
    },
    x: {
      grid: {
        display: false,
        drawBorder: false,
      },
      position: "bottom",
    },
    xTwo: {
      position: "top",
      grid: {
        display: false,
        drawBorder: false,
      },
      ticks: {
        callback: (index: number) => {
          if (!data.value[index]) return;

          return data.value[index].split(";")[1] + " km/h";
        },
      },
    },
  },
  plugins: {
    datalabels: {
      color: "rgba(112,112,112,1)",
      font: {
        size: 50,
        weight: "bold",
      },
      formatter: function (value: string): string {
        return "\u279e";
      },
      rotation: function (ctx: Context): number {
        return (
          Number(ctx.dataset.data[ctx.dataIndex]) *
          Number(data.value[ctx.dataIndex].split(";")[0])
        );
      },
    },
  },
} as ChartOptions<"line">;

onMounted(() => {
  setChartData();
});
</script>
