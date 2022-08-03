import { defineStore } from "pinia";
import type { Token, User } from "@/types/user";
import type { StoreOption } from "@/types/widgetOption";
import { loginUser, registerUser } from "@/services/userApi";

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
      token: {} as Token,
    },
  }),
  getters: {
    getOptions(state: userStore): StoreOption[] {
      return state.user.settings.widgetOptions;
    },
    isAuthenticated(state: userStore): boolean {
      /* TODO: the token must be checked here */
      if (state.user.token.token) return true;

      return false;
    },
    getToken(state: userStore): Token {
      return state.user.token;
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
    async loginUser(
      username: string | undefined,
      password: string | undefined
    ): Promise<boolean> {
      if (username && password) {
        const token: Token | undefined = await loginUser(username, password);
        if (token) {
          this.user.token = token;
          return true;
        }
      }
      return false;
    },
    async registerUser(
      username: string | undefined,
      password: string | undefined,
      firstname: string | undefined,
      lastname: string | undefined
    ): Promise<boolean> {
      if (username && password && firstname && lastname) {
        const token: Token | undefined = await registerUser(
          username,
          password,
          firstname,
          lastname
        );
        if (token) {
          this.user.token = token;
          return true;
        }
      }
      return false;
    },
    async resetStore(): Promise<void> {
      this.$reset();
    },
  },
});
