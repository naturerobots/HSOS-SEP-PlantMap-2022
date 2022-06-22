<template>
  <div class="inline-flex my-2 pl-3 text-xl space-x-3">
    <button
      class="rounded hover text-left"
      :class="isActive('rainPop')"
      @click="changeChartType('rainPop')"
    >
      Rain
      <div
        id="underline"
        class="rainbg h-1 rounded-md"
        :class="isActive('rainPop')"
      ></div>
    </button>
    <button
      class="rounded hover text-left"
      :class="isActive('temp')"
      @click="changeChartType('temp')"
    >
      Temperature
      <div
        id="underline"
        class="tempbg h-1 rounded-md"
        :class="isActive('temp')"
      ></div>
    </button>
    <button
      class="rounded hover text-left"
      :class="isActive('wind')"
      @click="changeChartType('wind')"
    >
      Wind
      <div
        id="underline"
        class="windbg h-1 rounded-md"
        :class="isActive('wind')"
      ></div>
    </button>
  </div>
  <LineChart :chart-data="chartData" :chart-options="chartOptions"></LineChart>
</template>

<script setup lang="ts">
export type ChartType = "rainPop" | "temp" | "wind";

import type { ChartData, ChartDataset, ChartOptions } from "chart.js";
import type { Hourly } from "@/types/weatherData";
import { ref, watch, onMounted, type Ref, type ToRefs } from "vue";
import { storeToRefs } from "pinia";
import { weatherDataStore } from "@/stores/weatherDataStore";
import LineChart from "@/components/weather/LineChart.vue";

import {
  getChartDataRainPop,
  getChartDataTemp,
  getChartDataWind,
  getChartOptionsRainPop,
  getChartOptionsTemp,
  getChartOptionsWind,
} from "@/components/weather/ChartSettings";

const props = withDefaults(
  defineProps<{
    chartType?: ChartType;
  }>(),
  {
    chartType: "rainPop",
  }
);

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

function changeChartType(chartType: ChartType): void {
  currChartType.value = chartType;
  updateOptions[currChartType.value]();
  updateData[currChartType.value]();
}

function isActive(type: ChartType): string {
  return currChartType.value === type ? "isActive" : "notActive";
}
</script>

<!--TODO: has to be refactored, but works-->
<style lang="scss">
.isActive {
  @apply text-black;
}

.notActive {
  @apply text-slate-400;
}

.notActive#underline {
  @apply bg-slate-300;
}

.isActive.rainbg {
  background-color: #29a6b7;
}

.isActive.tempbg {
  background-color: #ebc351;
}

.isActive.windbg {
  background-color: #29a6b7;
}
</style>
