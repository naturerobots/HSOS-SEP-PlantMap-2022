import { defineStore } from "pinia";
import type { Weather } from "@/types/weather";
import { getWeatherInformation } from "@/services/openWeatherApi";

export const weatherStore = defineStore({
  id: "weather",
  state: () => ({
    weather: {} as Weather,
  }),
  getters: {
    getWeather: (state) => state.weather,
  },
  actions: {
    async loadDataFromApi() {
      //this.weather = localStorage.getItem("weather");
      //console.log(this.weather);

      this.weather = await getWeatherInformation(1, 1); //.then(value => this.weather = value);
    },
  },
});
