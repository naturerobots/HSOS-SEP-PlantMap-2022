<template>
  <Bar
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="chartId"
    :dataset-id-key="datasetIdKey"
    :plugins="plugins"
    :css-classes="cssClasses"
    :styles="styles"
    :width="width"
    :height="height"
  />
</template>

<script setup lang="ts">
import type { PropType } from "vue";
import { Bar } from "vue-chartjs";
import type { Plugin } from "chart.js";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";

ChartJS.register(Title, Tooltip, BarElement, CategoryScale, LinearScale);

defineProps({
  chartId: {
    type: String,
    default: "bar-chart",
  },
  datasetIdKey: {
    type: String,
    default: "label",
  },
  width: {
    type: Number,
    default: 200,
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
    type: Array as PropType<Plugin<"bar", any>[]>,
    default: [] as Plugin<"bar", any>[],
  },
});

const chartData = {
  labels: ["January", "February", "March"],
  datasets: [
    {
      data: [25, 20, 12],
    },
  ],
};

const chartOptions = {
  responsive: true,
};
</script>
