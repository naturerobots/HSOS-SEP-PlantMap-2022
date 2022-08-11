import { defineStore } from "pinia";
import type { Token, User, Settings } from "@/types/user";
import type { StoreOption } from "@/types/widgetOption";
import {
  getUser,
  loginUser,
  registerUser,
  editUser,
  addPermissionToCompany,
  addPermissionToGarden,
  removePermissionFromCompany,
  removePermissionFromGarden,
} from "@/services/userApi";
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
      widgetOptions: [] as StoreOption[],
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
            if (!widgetOptions) {
              this.settings.widgetOptions = [];
              return true;
            }

            this.settings.widgetOptions = widgetOptions;
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
      if (!(await editUser(firstName, lastName, username, password)))
        return false;

      this.user.first_name = firstName ? firstName : this.user.first_name;
      this.user.last_name = lastName ? lastName : this.user.last_name;
      this.user.username = username ? username : this.user.username;
      return true;
    },
    async saveWidgets(): Promise<boolean> {
      return await postWidgets(this.settings.widgetOptions);
    },
    async disposeStore(): Promise<void> {
      this.$reset();
      this.$dispose();
    },
    async addPermissionToCompany(
      username: string,
      admin: boolean,
      companyId: number
    ): Promise<boolean> {
      if (await addPermissionToCompany(username, admin, companyId)) return true;
      return false;
    },
    async removePermissionFromCompany(
      username: string,
      companyId: number
    ): Promise<boolean> {
      if (await removePermissionFromCompany(username, companyId)) return true;
      return false;
    },
    async addPermissionToGarden(
      username: string,
      admin: boolean,
      companyId: number,
      gardenId: number
    ): Promise<boolean> {
      if (await addPermissionToGarden(username, admin, companyId, gardenId))
        return true;
      return false;
    },
    async removePermissionFromGarden(
      username: string,
      companyId: number,
      gardenId: number
    ): Promise<boolean> {
      if (await removePermissionFromGarden(username, companyId, gardenId))
        return true;
      return false;
    },
  },
});
