import { defineStore } from "pinia";
import type { Company } from "@/types/company";
import { getCompanies, deleteCompany } from "@/services/companyApi";

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
    setSelectedCompany(companyId: number | undefined): void {
      /* TODO: check if id exists in companies */
      this.selectedCompany = companyId;
    },
    async disposeStore(): Promise<void> {
      this.$reset();
      this.$dispose();
    },
    async deleteCompany(companyId: number): Promise<boolean> {
      /* TODO: check if id exists in gardens */
      if (await deleteCompany(companyId)) {
        for (let index = 0; index < this.companies.length; index++) {
          if (this.companies[index].id == companyId) {
            this.companies.splice(index, 1);

            if (this.companies.length <= 0) {
              this.selectedCompany = undefined;
              return true;
            }

            this.selectedCompany = this.companies[0].id;
            return true;
          }
        }
      }
      return false;
    },
  },
});
