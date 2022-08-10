import axios from "axios";
import { userStore } from "@/stores/userStore";
import { storeToRefs } from "pinia";
import type { Company } from "@/types/company";

const baseURL = "http://127.0.0.1:8000";

export async function createCompany(name: string): Promise<number | undefined> {
  return await axios
    .post<{ id: number }>(
      baseURL + "/companies",
      { name: name },
      {
        headers: {
          Authorization:
            "Token " + storeToRefs(userStore()).getToken.value.token,
        },
      }
    )
    .then(function (response): number {
      return response.data.id;
    })
    .catch(function (): undefined {
      //console.log(error.response);
      return undefined;
    });
}

export async function getCompanies(): Promise<Company[] | undefined> {
  return await axios
    .get<Company[]>(baseURL + "/companies", {
      headers: {
        Authorization: "Token " + storeToRefs(userStore()).getToken.value.token,
      },
    })
    .then(function (response): Company[] {
      return response.data;
    })
    .catch(function (): undefined {
      return undefined;
    });
}

export async function deleteCompany(companyId: number): Promise<boolean> {
  return true;
  /* return await axios
    .delete(baseURL + "/companies/" + companyId, {
      headers: {
        Authorization: "Token " + storeToRefs(userStore()).getToken.value.token,
      },
    })
    .then(function (): boolean {
      return true;
    })
    .catch(function (): boolean {
      return false;
    }); */
}
