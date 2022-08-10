import { defineStore } from "pinia";
import type { Company } from "@/types/company";
import { getCompanies } from "@/services/companyApi";

// TODO: move to types/store
interface companyStore {
  companies: Company[];
  selectedCompany: number | undefined;
}

export const companyStore = defineStore({
  id: "companyStore",
  state: (): companyStore => ({
    companies: [] as Company[],
    selectedCompany: undefined,
  }),
  getters: {
    getCompanies(state: companyStore): Company[] {
      return state.companies;
    },
    getSelectedCompany(state: companyStore): number | undefined {
      return state.selectedCompany;
    },
  },
  actions: {
    async loadDataFromApi(): Promise<void> {
      const response = await getCompanies();
      if (response) {
        this.companies = response;
      }
    },
    setSelectedCompany(companyId: number): void {
      /* TODO: check if id exists in companies */
      this.selectedCompany = companyId;
    },
    async disposeStore(): Promise<void> {
      this.$dispose();
    },
  },
});
