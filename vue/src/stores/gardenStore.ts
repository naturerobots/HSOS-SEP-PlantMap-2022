import { defineStore } from "pinia";
import type { Garden } from "@/types/garden";
import { deleteGarden, getGardens } from "@/services/gardenApi";

// TODO: move to types/store
interface gardenStore {
  gardens: Garden[];
  selectedGarden: number | undefined;
}

export const gardenStore = defineStore({
  id: "gardenStore",
  state: (): gardenStore => ({
    gardens: [] as Garden[],
    selectedGarden: undefined,
  }),
  getters: {
    getGardens(state: gardenStore): Garden[] {
      return state.gardens;
    },
    getSelectedGarden(state: gardenStore): number | undefined {
      return state.selectedGarden;
    },
  },
  actions: {
    async loadDataFromApi(companyId: number): Promise<void> {
      const response = await getGardens(companyId);
      if (response) {
        this.gardens = response;
      }
    },
    async loadGardens(companyId: number): Promise<Garden[] | undefined> {
      const response = await getGardens(companyId);
      if (response) {
        return response;
      }
    },
    setSelectedGarden(gardenId: number | undefined): void {
      /* TODO: check if id exists in gardens */
      this.selectedGarden = gardenId;
    },
    async disposeStore(): Promise<void> {
      this.$dispose();
    },
    async resetStore(): Promise<void> {
      this.$reset();
    },
    async deleteGarden(companyId: number, gardenId: number): Promise<boolean> {
      /* TODO: check if id exists in gardens */
      if (await deleteGarden(companyId, gardenId)) {
        for (let index = 0; index < this.gardens.length; index++) {
          if (this.gardens[index].id == gardenId) {
            this.gardens.splice(index, 1);

            if (this.gardens.length <= 0) {
              this.selectedGarden = undefined;
              break;
            }

            this.selectedGarden = this.gardens[0].id;
            break;
          }
        }
      }
      return false;
    },
  },
});
