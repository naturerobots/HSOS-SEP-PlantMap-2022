import { defineStore } from "pinia";
import type { Bed } from "@/types/bed";
import { loadBeds } from "@/services/bedApi";
import type { Plants } from "@/types/plants";
import type { Beds } from "@/types/beds";

export const bedStore = defineStore({
  id: "bedStore",
  state: () => ({
    beds: {
      beds: [] as Bed[],
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
      state.beds.beds.forEach(function (bed) {
        //console.log("Bed Id for: " + bed.id);
        //console.log(bed.id == state.selectedBed);
        if (bed.id == state.selectedBed) {
          //console.log("for");
          bedTmp = bed;
          return bed;
        }
      });
      //console.log("bedtmp " + bedtmp.id);
      return bedTmp;
    },
    getIsLoading(state): boolean | undefined {
      return state.isLoading;
    },
  },
  actions: {
    async loadDataFromApi(): Promise<void> {
      // const bedData = localStorage.getItem("beds");
      this.isLoading = true;
      this.beds.beds = [];
      //The data is loaded from the local memory if it exists there.
      //To refresh the data, the local memory must be deleted.

      //   if (bedData) {
      //     this.beds = JSON.parse(bedData);
      //   } else {
      //     this.beds = await getBeds();
      //     console.log("Beds: " + this.beds);
      //     localStorage.setItem("beds", JSON.stringify(this.beds));
      //   }

      this.isLoading = await loadBeds();
      //console.log("Beds: " + this.beds);
    },
    setSelectedBedId(bedId: number): void {
      /* TODO: check if id exists in beds */
      this.selectedBed = bedId;
    },
    setBed(bed: Bed) {
      this.beds.beds.push(bed);
    },
  },
});
