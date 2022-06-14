import { defineStore } from "pinia";
import type { Crop } from "@/types/crop";
import { getCrops } from "@/services/cropsApi";

export const cropsStore = defineStore({
  id: "cropsStore",
  state: () => ({
    crops: [] as Crop[],
  }),
  getters: {
    getCrops: (state) => state.crops,
  },
  actions: {
    async loadDataFromApi(): Promise<void> {
      const cropsData = localStorage.getItem("crops");

      //The data is loaded from the local memory if it exists there.
      //To refresh the data, the local memory must be deleted.
      if (cropsData) {
        this.crops = JSON.parse(cropsData);
      } else {
        this.crops = await getCrops();
        localStorage.setItem("crops", JSON.stringify(this.crops));
      }
    },
  },
});
