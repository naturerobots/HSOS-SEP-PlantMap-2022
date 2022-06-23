import { defineStore } from "pinia";
import type { User } from "@/types/user";
import type { StoreOption } from "@/types/widgetOption";

// TODO: move to types/store
interface userStore {
  user: User;
}

export const userStore = defineStore({
  id: "userStore",
  state: (): userStore => ({
    user: {
      settings: {
        widgetOptions: [
          "weather",
          "garden-map",
          "soil-parameter",
          "crops-table",
          "crops-map",
          "3d-table",
          "3d-map",
        ], //TODO: delete later
      },
    },
  }),
  getters: {
    getOptions(state: userStore): StoreOption[] {
      return state.user.settings.widgetOptions;
    },
  },
  actions: {
    addOption(storeOption: StoreOption): void {
      this.user.settings.widgetOptions.push(storeOption);
      this.updateOptions();
    },
    removeOption(storeOption: StoreOption): void {
      const index = this.user.settings.widgetOptions.indexOf(storeOption, 0);
      if (index > -1) {
        this.user.settings.widgetOptions.splice(index, 1);
      }
      this.updateOptions();
    },
    async updateOptions(): Promise<void> {
      //TODO: send options to API
    },
  },
});
