<template>
  <div class="card h-full w-full shadow-sm bg-[#fdfff9]">
    <div class="card-body p-5">
      <h2 class="text-xl text-center text-primary-focus">Weather</h2>
      <div class="card card-side">
        <div class="card-body">
          <div class="grid grid-cols-3 gap-4">
            <button
              class="btn btn-sm btn-ghost link"
              @click="changeChartType('rainPop')"
            >
              RainPop
            </button>
            <button
              class="btn btn-sm btn-ghost link"
              @click="changeChartType('temp')"
            >
              Temp
            </button>
            <button
              class="btn btn-sm btn-ghost link"
              @click="changeChartType('wind')"
            >
              Wind
            </button>
          </div>
          <LineChart
            :chart-data="chartData"
            :chart-options="chartOptions"
          ></LineChart>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
export type ChartType = "rainPop" | "temp" | "wind";

import type { ChartData, ChartDataset, ChartOptions } from "chart.js";
import type { Hourly } from "@/types/weatherData";
import {
  ref,
  watch,
  onMounted,
  type Ref,
  type ToRefs,
  type PropType,
} from "vue";
import { storeToRefs } from "pinia";
import { weatherDataStore } from "@/stores/weatherDataStore";
import LineChart from "@/components/Weather/LineChart.vue";

import {
  getChartDataRainPop,
  getChartDataTemp,
  getChartDataWind,
  getChartOptionsRainPop,
  getChartOptionsTemp,
  getChartOptionsWind,
} from "@/components/Weather/ChartSettings";

const props = defineProps({
  chartType: {
    type: String as PropType<ChartType>,
    default: "rainPop",
  },
});

const useWeatherDataStore: ToRefs<any> = storeToRefs(weatherDataStore());
const hourly: Ref<Hourly> = useWeatherDataStore.getHourly;
let currChartType = ref(props.chartType);

const data = {
  labels: useWeatherDataStore.getTimeLabels as Ref<string[]>,
  rainPop: useWeatherDataStore.getHourlyRainPop as Ref<string[]>,
  temp: useWeatherDataStore.getHourlyTemp as Ref<string[]>,
  wind: useWeatherDataStore.getHourlyWind as Ref<string[]>,
};

const chartOptions = ref<ChartOptions<"line">>({});

const chartData = ref<ChartData<"line">>({
  labels: data.labels.value,
  datasets: [] as ChartDataset<"line">[],
});

const updateData = {
  rainPop: () =>
    (chartData.value = {
      ...{ labels: data.labels.value },
      ...getChartDataRainPop(data.rainPop),
    }),
  temp: () =>
    (chartData.value = {
      ...{ labels: data.labels.value },
      ...getChartDataTemp(data.temp),
    }),
  wind: () =>
    (chartData.value = {
      ...{ labels: data.labels.value },
      ...getChartDataWind(data.wind),
    }),
};

const updateOptions = {
  rainPop: () => (chartOptions.value = getChartOptionsRainPop()),
  temp: () => (chartOptions.value = getChartOptionsTemp()),
  wind: () => (chartOptions.value = getChartOptionsWind(data.wind)),
};

onMounted(() => {
  updateOptions[currChartType.value]();
  updateData[currChartType.value]();
});

watch(hourly.value, () => {
  updateData[currChartType.value]();
});

function changeChartType(chartType: ChartType) {
  currChartType.value = chartType;
  updateOptions[currChartType.value]();
  updateData[currChartType.value]();
}
</script>
