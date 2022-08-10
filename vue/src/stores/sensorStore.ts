import { defineStore } from "pinia";
import { getSensorInformation } from "@/services/sensorApi";
import type { Sensor } from "@/types/sensor";

export const sensorStore = defineStore({
  id: "sensorStore",
  state: () => ({
    sensors: [] as Sensor[],
  }),
  getters: {
    getSensors: (state) => state.sensors,
  },
  actions: {
    async loadDataFromApi(): Promise<void> {
      this.sensors = await getSensorInformation();
    },
    async disposeStore(): Promise<void> {
      this.$dispose();
    },
  },
});
