import { defineStore } from "pinia";
import type { Crop } from "@/types/crop";
import { getCrops } from "@/services/cropsApi";
import type { Plants } from "@/types/plants";

export const cropsStore = defineStore({
  id: "cropsStore",
  state: () => ({
    crops: {
      plants: [] as Crop[],
    } as Plants,
    isLoading: false,
  }),
  getters: {
    getCrops: (state) => state.crops,
    getIsLoading(state): boolean | undefined {
      return state.isLoading;
    },
  },
  actions: {
    async loadDataFromApi(plantsUrl: string): Promise<void> {
      // const cropsData = localStorage.getItem("crops");
      this.isLoading = true;
      this.crops.plants = [];

      //The data is loaded from the local memory if it exists there.
      //To refresh the data, the local memory must be deleted.

      // if (cropsData) {
      //   this.crops = JSON.parse(cropsData);
      // } else {
      //   this.crops = await getCrops(plantsUrl);
      //   localStorage.setItem("crops", JSON.stringify(this.crops));
      // }

      this.crops = await getCrops(plantsUrl);
      if (this.crops) {
        this.isLoading = false;
      }
      // localStorage.setItem("crops", JSON.stringify(this.crops));
    },
    setCrops(crops: Crop[]) {
      this.crops.crops = crops;
    },
  },
});
