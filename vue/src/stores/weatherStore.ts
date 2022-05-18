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
        this.weather = JSON.parse(weatherData);
      } else {
        this.weather = await getWeatherInformation(52.2799, 8.0471788);
        localStorage.setItem("weather", JSON.stringify(this.weather));
      }
    },
  },
});
