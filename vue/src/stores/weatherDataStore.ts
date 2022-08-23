import type {
  WeatherDataForecast,
  WeatherDataCurrent,
  Hourly,
} from "@/types/weatherData";
import { defineStore } from "pinia";

import {
  getWeatherDataCurrent,
  getWeatherDataForecast,
} from "@/services/weatherDataAPI";

//import { getGeoData } from "@/services/geoDataAPI";
import type { GeoData, GeoDataArray } from "@/types/geoData";
import { gardenStore } from "./gardenStore";
import type { Coordinate } from "@/types/gardenImage";

interface weatherDataStore {
  initialized: boolean;
  geo: GeoData[];
  current: WeatherDataCurrent | undefined;
  forecast: WeatherDataForecast | undefined;
}

export const weatherDataStore = defineStore({
  id: "weatherDataStore",
  state: () => ({
    initialized: false,
    geo: [],
    current: undefined,
    forecast: undefined,
  }),
  getters: {
    //Getter not necessary
    getWeatherData(state: any) {
      return state;
    },
    getCurrent(state: any): WeatherDataCurrent | undefined {
      return state.current;
    },
    getForecast(state: any): WeatherDataForecast | undefined {
      return state.forecast;
    },
    getHourly(state: any): Hourly {
      return state.forecast.hourly;
    },
    getTimeLabels(state: any): string[] {
      return state.forecast.hourly
        .slice(0, 8)
        .map((value: Hourly, index: any) => {
          /*if (index === 0) {
            return "Now";
          }*/

          return new Date(value.dt * 1000).toLocaleString("de-DE", {
            hour: "numeric",
            minute: "numeric",
          });
        });
    },
    getHourlyRainPop(state: any): number[] {
      return state.forecast.hourly
        .slice(0, 8)
        .map((value: Hourly) => Math.round(value.pop * 100));
    },
    getHourlyTemp(state: any): number[] {
      return state.forecast.hourly
        .slice(0, 8)
        .map((value: Hourly) => Math.round(value.temp));
    },
    getHourlyWind(state: any): string[] {
      return state.forecast.hourly
        .slice(0, 8)
        .map(
          (value: Hourly) => value.wind_deg + ";" + Math.round(value.wind_speed)
        );
    },
  },
  actions: {
    async loadWeatherData(): Promise<void> {
      const coord = gardenStore().getGardenImage.image?.coordinates[0];

      if (coord) {
        this.current = await getWeatherDataCurrent(
          coord?.latitude as number,
          coord?.longitude as number
        );
        this.forecast = await getWeatherDataForecast(
          coord?.latitude as number,
          coord?.longitude as number
        );
      } else {
        this.current = await getWeatherDataCurrent(52.2799, 8.0471788);
        this.forecast = await getWeatherDataForecast(52.2799, 8.0471788);
      }
    },

    async initWeatherData(): Promise<void> {
      if (this.initialized)
        throw Error("WeatherDataStore: already initialized");

      console.log("WeatherDataStore: initialization started");

      const weatherDataCurrent = localStorage.getItem("WeatherDataCurrent");
      const weatherDataForecast = localStorage.getItem("WeatherDataForecast");

      if (weatherDataCurrent) {
        this.current = JSON.parse(weatherDataCurrent);
        console.log(
          "WeatherDataStore: weatherDataCurrent loaded from localStorage"
        );
      } else {
        this.current = await getWeatherDataCurrent(52.2799, 8.0471788);
        localStorage.setItem(
          "WeatherDataCurrent",
          JSON.stringify(this.current)
        );
        console.log("WeatherDataStore: weatherDataCurrent loaded from API");
      }

      if (weatherDataForecast) {
        this.forecast = JSON.parse(weatherDataForecast);
        console.log(
          "WeatherDataStore: weatherDataForecast loaded from localStorage"
        );
      } else {
        this.forecast = await getWeatherDataForecast(52.2799, 8.0471788);
        localStorage.setItem(
          "WeatherDataForecast",
          JSON.stringify(this.forecast)
        );
        console.log("WeatherDataStore: weatherDataForecast loaded from API");
      }

      console.log("WeatherDataStore: initialisation done");

      this.initialised = true;
    },
  },
});

/*
setInterval(() => {
  //getWeatherDataCurrent(52.2799, 8.0471788);
  console.log("Update current weather data [60 secs]");
}, 60 * 1000);


setInterval(() => {
  //getWeatherDataCurrent(52.2799, 8.0471788);
  console.log("Update current weather data [5 secs]");
}, 5 * 1000);
*/

/*FIXME: replacer and reviver needed because weather stores Date Object so it has not to be builded after retrieving
 **       if not in local storage dt retrieves a millisec number, but after persist we would retrieve a date object
 **       could be reversed again, so that "dt" is number, cuz this solution smeels a bit for a simple Date
 **       maybe there is a completly different solution for this problem
 **       https://stackoverflow.com/questions/31096130/how-to-json-stringify-a-javascript-date-and-preserve-timezone
 */
/*
function replacer(this: any, key: string, value: any) {
  if (this[key] instanceof Date) {
    return (this[key] as Date).getTime() / 1000;
  }

  return value;
}

function reviver(this: any, key: string, value: any) {
  if (key === "dt") {
    return new Date(value * 1000);
  }

  return value;
}
*/
