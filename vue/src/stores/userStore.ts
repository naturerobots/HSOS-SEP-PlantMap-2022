import { defineStore } from "pinia";
import type { StoreOption } from "@/types/widgetOption";

// TODO: move to types/store
interface userStore {
  options: StoreOption[];
}

export const userStore = defineStore({
  id: "userStore",
  state: (): userStore => ({
    options: ["weather", "garden", "soil-parameter"], //TODO: delete later
  }),
  getters: {
    getOptions(state: userStore): StoreOption[] {
      return state.options;
    },
  },
  actions: {
    async updateOptions(): Promise<void> {
      //TODO: send options to API
    },
  },
});
