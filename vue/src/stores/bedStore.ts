import { defineStore } from "pinia";
import type { Bed } from "@/types/bed";
import { loadBeds } from "@/services/bedApi";
import type { Beds } from "@/types/beds";

export const bedStore = defineStore({
  id: "bedStore",
  state: () => ({
    beds: {
      bedList: [] as Bed[],
    } as Beds,
    selectedBed: {} as number,
    isLoading: false,
  }),
  getters: {
    getBeds: (state) => state.beds,
    getSelectedBedId(state): number | undefined {
      return state.selectedBed;
    },
    getSelectedBed(state): Bed | undefined {
      let bedTmp = {} as Bed;
      state.beds.bedList.forEach(function (bed) {
        if (bed.id == state.selectedBed) {
          bedTmp = bed;
          return bed;
        }
      });
      return bedTmp;
    },
    getIsLoading(state): boolean | undefined {
      return state.isLoading;
    },
  },
  actions: {
    async loadDataFromApi(): Promise<void> {
      this.isLoading = true;
      this.beds.bedList = [];
      this.isLoading = await loadBeds();
    },
    setSelectedBedId(bedId: number): void {
      this.selectedBed = bedId;
    },
    setBed(bed: Bed) {
      console.log(bed);
      this.beds.bedList.push(bed);
    },
  },
});
