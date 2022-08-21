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
    selectedCropId: {} as number,
    isLoading: false,
  }),
  getters: {
    getCrops: (state) => state.crops,
    getSelectedCropId(state): string | undefined {
      return state.selectedCropId;
    },
    getIsLoading(state): boolean | undefined {
      return state.isLoading;
    },
  },
  actions: {
    async loadDataFromApi(plantsUrl: string): Promise<void> {
      this.isLoading = true;
      this.crops.plants = (await getCrops(plantsUrl)).plants;
      if (this.crops.plants.length > 0) {
        this.isLoading = false;
      }
    },
    setCrops(crops: Crop[]) {
      this.crops.plants = crops;
    },
    setSelectedCropId(cropId: string) {
      this.selectedCropId = cropId;
    },
    resetCrops() {
      this.crops.plants.length = 0;
      this.crops.plants = [];
    },
  },
});
