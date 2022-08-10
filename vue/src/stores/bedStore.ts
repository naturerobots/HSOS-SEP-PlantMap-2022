import { defineStore } from "pinia";
import type { Bed } from "@/types/bed";
import { getBeds } from "@/services/bedApi";
import type { Plants } from "@/types/plants";
import type { Beds } from "@/types/beds";

export const bedStore = defineStore({
  id: "bedStore",
  state: () => ({
    beds: {} as Beds,
  }),
  getters: {
    getBeds: (state) => state.beds,
  },
  actions: {
    async loadDataFromApi(): Promise<void> {
      const bedData = localStorage.getItem("beds");

      //The data is loaded from the local memory if it exists there.
      //To refresh the data, the local memory must be deleted.
      if (bedData) {
        this.beds = JSON.parse(bedData);
      } else {
        this.beds = await getBeds();
        console.log("Beds: " + this.beds);
        localStorage.setItem("beds", JSON.stringify(this.beds));
      }
    },
  },
});
