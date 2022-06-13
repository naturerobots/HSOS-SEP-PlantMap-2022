<template>
  <Line
    ref="lineChart"
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="'weather-chart'"
    :width="width"
    :height="height"
  />
</template>

<script setup lang="ts">
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
  type DefaultDataPoint,
} from "chart.js";
import type { ChartData, ChartOptions } from "chart.js";
import ChartJsPluginDataLabelsfrom from "chartjs-plugin-datalabels";

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
    chartData: ChartData<"line", DefaultDataPoint<"line">, unknown>;
    chartOptions: ChartOptions<"line">;
    width: number;
    height: number;
  }>(),
  {
    width: 400,
    height: 100,
  }
);
</script>
