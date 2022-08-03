import { defineStore } from "pinia";
import type { Company } from "@/types/company";
import { getCompanies } from "@/services/companyApi";

// TODO: move to types/store
interface companyStore {
  companies: Company[];
}

export const companyStore = defineStore({
  id: "companyStore",
  state: (): companyStore => ({
    companies: [] as Company[],
  }),
  getters: {
    getCompanies(state: companyStore): Company[] {
      return state.companies;
    },
  },
  actions: {
    async loadDataFromApi(): Promise<void> {
      const response = await getCompanies();
      if (response) {
        this.companies = response;
      }
    },
  },
});
