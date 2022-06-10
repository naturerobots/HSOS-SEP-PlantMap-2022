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
import type { PropType } from "vue";
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

defineProps({
  chartData: {
    type: Object as PropType<
      ChartData<"line", DefaultDataPoint<"line">, unknown>
    >,
    required: true,
  },
  chartOptions: {
    type: Object as PropType<ChartOptions<"line">>,
    required: true,
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
</script>
