import { defineStore } from "pinia";
import type { Garden } from "@/types/garden";
import { getGardens } from "@/services/gardenApi";

// TODO: move to types/store
interface gardenStore {
  gardens: Garden[];
}

export const gardenStore = defineStore({
  id: "gardenStore",
  state: (): gardenStore => ({
    gardens: [] as Garden[],
  }),
  getters: {
    getGardens(state: gardenStore): Garden[] {
      return state.gardens;
    },
  },
  actions: {
    async loadDataFromApi(companyId: number): Promise<void> {
      const response = await getGardens(companyId);
      if (response) {
        this.gardens = response;
      }
    },
  },
});
