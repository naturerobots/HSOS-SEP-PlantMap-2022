import { defineStore } from "pinia";
import type { Weather } from "@/types/weather";
import { getWeatherInformation } from "@/services/openWeatherApi";

export const weatherStore = defineStore({
  id: "weatherStore",
  state: () => ({
    weather: {} as Weather,
  }),
  getters: {
    getWeather: (state) => state.weather,
  },
  actions: {
    async loadDataFromApi(): Promise<void> {
      const weatherData = localStorage.getItem("weather");

      //The data is loaded from the local memory if it exists there.
      //The data should have a timestamp so that the data can be updated after a certain time.
      //For now, it is sufficient if the data is in the local memory and the API is not always called.
      //To refresh the data, the local memory must be deleted.
      if (weatherData) {
        this.weather = JSON.parse(weatherData, reviver);
      } else {
        this.weather = await getWeatherInformation(52.2799, 8.0471788);
        localStorage.setItem("weather", JSON.stringify(this.weather, replacer));
      }
    },
  },
});

/*FIXME: replacer and reviver needed because weather stores Date Object so it has not to be builded after retrieving
 **       if not in local storage dt retrieves a millisec number, but after persist we would retrieve a date object
 **       could be reversed again, so that "dt" is number, cuz this solution smeels a bit for a simple Date
 **       maybe there is a completly different solution for this problem
 **       https://stackoverflow.com/questions/31096130/how-to-json-stringify-a-javascript-date-and-preserve-timezone
 */

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
