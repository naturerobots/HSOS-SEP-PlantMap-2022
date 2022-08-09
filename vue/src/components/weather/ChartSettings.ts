import type { ChartData, ChartOptions } from "chart.js";
import type { Context } from "chartjs-plugin-datalabels/types/context";
import type { Ref } from "vue";

//###############
//### RainPop ###
//###############

export function getChartDataRainPop(data: Ref<string[]>): ChartData<"line"> {
  const updatedChartData = {
    datasets: [
      {
        label: "HourlyRainPopTime",
        data: data.value as any,
        fill: true,
        pointBackgroundColor: "rgba(41,166,183,1)",
        pointBorderColor: "rgba(41,166,183,1)",
        backgroundColor: "rgba(101,191,203,1)",
        tension: 0.3,
      },
    ],
  };

  return updatedChartData;
}

export function getChartOptionsRainPop(): ChartOptions<"line"> {
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
        ticks: {
          font: {
            size: 14,
            weight: "bold",
          },
        },
      },
    },
    plugins: {
      datalabels: {
        anchor: "end",
        align: "top",
        offset: -2,
        color: "rgba(112,112,112,1)",
        font: {
          size: 15,
          weight: "bold",
        },
        formatter: (value: string) => {
          return value + "%";
        },
      },
    },
  } as ChartOptions<"line">;

  return updatedChartOptions;
}

//############
//### Temp ###
//############

export function getChartDataTemp(data: Ref<string[]>): ChartData<"line"> {
  const updatedChartData = {
    datasets: [
      {
        label: "HourlyTempTime",
        data: data.value as any,
        fill: true,
        pointBackgroundColor: "rgba(235,195,81,1)",
        pointBorderColor: "rgba(235,195,81,1)",
        backgroundColor: "rgba(240,210,125,1)",
        tension: 0.3,
      },
    ],
  } as ChartData<"line">;

  return updatedChartData;
}

export function getChartOptionsTemp(): ChartOptions<"line"> {
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
        ticks: {
          font: {
            size: 14,
            weight: "bold",
          },
        },
      },
    },
    plugins: {
      datalabels: {
        anchor: "end",
        align: "top",
        offset: -2,
        color: "rgba(112,112,112,1)",
        font: {
          size: 15,
          weight: "bold",
        },
        formatter: function (value: string) {
          return value + "°";
        },
      },
    },
  } as ChartOptions<"line">;

  return updatedChartOptions;
}

//############
//### Wind ###
//############

export function getChartDataWind(data: Ref<string[]>): ChartData<"line"> {
  const updatedChartData = {
    datasets: [
      {
        label: "HourlyWindTime",
        data: data.value.map(() => 50),
        pointBackgroundColor: "rgba(0, 0, 0, 0)",
        pointBorderColor: "rgba(0, 0, 0, 0)",
        backgroundColor: "rgba(0, 0, 0, 0)",
        showLine: false,
      },
    ],
  } as ChartData<"line">;

  return updatedChartData;
}

export function getChartOptionsWind(data: Ref<string[]>): ChartOptions<"line"> {
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
        ticks: {
          font: {
            size: 14,
            weight: "bold",
          },
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
            formatter: function () {
              return "\u27A2";
            },
            rotation: function (ctx: Context): number {
              return (
                Number(ctx.dataset.data[ctx.dataIndex]) *
                Number(data.value[ctx.dataIndex].split(";")[0])
              );
            },
          },
          values: {
            anchor: "start",
            align: "top",
            offset: 25,
            color: "rgba(112,112,112,1)",
            font: {
              size: 15,
              weight: "bold",
            },
            formatter: function (value: number, ctx: Context) {
              if (!data.value[ctx.dataIndex]) return;
              return data.value[ctx.dataIndex].split(";")[1] + " km/h";
            },
          },
        },
      },
    },
  } as ChartOptions<"line">;

  return updatedChartOptions;
}
