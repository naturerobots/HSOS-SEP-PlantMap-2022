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
import type { Context } from "chartjs-plugin-datalabels/types/context";
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
  datasets: [] as ChartDataset<"line">[],
});

const updateData = {
  rainPop: () => setChartDataRainPop(),
  temp: () => setChartDataTemp(),
  wind: () => setChartDataWind(),
};

const updateOptions = {
  rainPop: () => setChartOptionsRainPop(),
  temp: () => setChartOptionsTemp(),
  wind: () => setChartOptionsWind(),
};

onMounted(() => {
  updateData[currChartType.value]();
  updateOptions[currChartType.value]();
});

watch(hourly.value, () => {
  updateData[currChartType.value]();
});

function changeChartType(chartType: ChartType) {
  currChartType.value = chartType;
  updateOptions[currChartType.value]();
  updateData[currChartType.value]();
}

/**
 * ### CHART DATA
 */

function setChartDataRainPop(): void {
  const updatedChartData = {
    labels: data.labels?.value,
    datasets: [
      {
        label: "HourlyRainPopTime",
        data: data.rainPop.value as any,
        fill: true,
        pointBackgroundColor: "rgba(41,166,183,1)",
        pointBorderColor: "rgba(41,166,183,1)",
        backgroundColor: "rgba(101,191,203,1)",
        tension: 0.3,
      },
    ],
  } as ChartData<"line">;

  chartData.value = updatedChartData;
}

function setChartDataTemp(): void {
  const updatedChartData = {
    labels: data.labels?.value,
    datasets: [
      {
        label: "HourlyTempTime",
        data: data.temp.value as any,
        fill: true,
        pointBackgroundColor: "rgba(235,195,81,1)",
        pointBorderColor: "rgba(235,195,81,1)",
        backgroundColor: "rgba(240,210,125,1)",
        tension: 0.3,
      },
    ],
  } as ChartData<"line">;

  chartData.value = updatedChartData;
}

function setChartDataWind(): void {
  const updatedChartData = {
    labels: data.labels?.value,
    datasets: [
      {
        label: "HourlyWindTime",
        data: data.wind.value.map(() => 50),
        pointBackgroundColor: "rgba(0, 0, 0, 0)",
        pointBorderColor: "rgba(0, 0, 0, 0)",
        backgroundColor: "rgba(0, 0, 0, 0)",
        showLine: false,
      },
    ],
  } as ChartData<"line">;

  chartData.value = updatedChartData;
}

/**
 * ### CHART OPTIONS
 */
function setChartOptionsRainPop() {
  const updatedChartOptions = {
    animation: false,
    events: [],
    maintainAspectRatio: false,
    responsive: true,
    layout: {
      padding: {
        top: 25,
        left: 25,
        right: 25,
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
        color: "rgba(112,112,112,1)",
        font: {
          size: 14,
          weight: "bold",
        },
        formatter: (value: string) => {
          return value + "%";
        },
      },
    },
  } as ChartOptions<"line">;

  chartOptions.value = updatedChartOptions;
}

function setChartOptionsTemp() {
  const updatedChartOptions = {
    animation: false,
    events: [],
    maintainAspectRatio: false,
    responsive: true,
    layout: {
      padding: {
        top: 25,
        left: 25,
        right: 25,
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
        color: "rgba(112,112,112,1)",
        font: {
          size: 14,
          weight: "bold",
        },
        formatter: function (value: string) {
          return value + "°";
        },
      },
    },
  } as ChartOptions<"line">;

  chartOptions.value = updatedChartOptions;
}

function setChartOptionsWind() {
  const updatedChartOptions = {
    animation: false,
    events: [],
    maintainAspectRatio: false,
    responsive: true,
    layout: {
      padding: {
        top: 25,
        left: 25,
        right: 25,
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
        position: "bottom",
        grid: {
          display: false,
          drawBorder: false,
        },
      },
    },
    plugins: {
      datalabels: {
        labels: {
          arrows: {
            color: "rgba(112,112,112,1)",
            font: {
              size: 40,
              weight: "bold",
            },
            formatter: function (value: string) {
              return "\u27A2";
            },
            rotation: function (ctx: Context): number {
              return (
                Number(ctx.dataset.data[ctx.dataIndex]) *
                Number(data.wind.value[ctx.dataIndex].split(";")[0])
              );
            },
          },
          values: {
            anchor: "start",
            align: "top",
            offset: 25,
            color: "rgba(112,112,112,1)",
            font: {
              size: 14,
              weight: "bold",
            },
            formatter: function (value: number, ctx: Context) {
              if (!data.wind.value[ctx.dataIndex]) return;
              return data.wind.value[ctx.dataIndex].split(";")[1] + " km/h";
            },
          },
        },
      },
    },
  } as ChartOptions<"line">;

  chartOptions.value = updatedChartOptions;
}
</script>
