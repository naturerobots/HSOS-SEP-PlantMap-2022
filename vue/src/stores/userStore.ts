import { defineStore } from "pinia";
import type { Token, User, Settings } from "@/types/user";
import type { StoreOption } from "@/types/widgetOption";
import { getUser, loginUser, registerUser, editUser } from "@/services/userApi";
import { postWidgets, getWidgets } from "@/services/widgetApi";

// TODO: move to types/store
interface userStore {
  user: User;
  settings: Settings;
  token: Token;
}

export const userStore = defineStore({
  id: "userStore",
  state: (): userStore => ({
    user: {} as User,
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
  }),
  getters: {
    getUser(state: userStore): User {
      return state.user;
    },
    getOptions(state: userStore): StoreOption[] {
      return state.settings.widgetOptions;
    },
    isAuthenticated(state: userStore): boolean {
      /* TODO: the token must be checked here */
      if (state.token.token) return true;

      return false;
    },
    getToken(state: userStore): Token {
      return state.token;
    },
  },
  actions: {
    addOption(storeOption: StoreOption): void {
      this.settings.widgetOptions.push(storeOption);
      this.updateOptions();
    },
    removeOption(storeOption: StoreOption): void {
      const index = this.settings.widgetOptions.indexOf(storeOption, 0);
      if (index > -1) {
        this.settings.widgetOptions.splice(index, 1);
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
          this.token = token;

          const user: User | undefined = await getUser();

          if (user) {
            this.user = user;
            const widgetOptions: StoreOption[] | undefined = await getWidgets();
            if (widgetOptions) this.settings.widgetOptions = widgetOptions;
            return true;
          }

          return false;
        }
      }
      return false;
    },
    async registerUser(
      username: string | undefined,
      password: string | undefined,
      firstName: string | undefined,
      lastName: string | undefined
    ): Promise<boolean> {
      if (username && password && firstName && lastName) {
        const token: Token | undefined = await registerUser(
          username,
          password,
          firstName,
          lastName
        );
        if (token) {
          this.token = token;

          const user: User | undefined = await getUser();

          if (user) {
            this.user = user;
            return true;
          }

          return false;
        }
      }
      return false;
    },
    async editUser(
      firstName?: string | undefined,
      lastName?: string | undefined,
      username?: string | undefined,
      password?: string | undefined
    ): Promise<boolean> {
      await editUser(firstName, lastName, username, password);
      return true;
    },
    async saveWidgets(): Promise<boolean> {
      return await postWidgets(this.settings.widgetOptions);
    },
    async disposeStore(): Promise<void> {
      this.$dispose();
    },
  },
});
