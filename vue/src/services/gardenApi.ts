import axios from "axios";
import { userStore } from "@/stores/userStore";
import { storeToRefs } from "pinia";
import type { Garden } from "@/types/garden";

const baseURL = "http://127.0.0.1:8000";

export async function createGarden(
  companyId: number,
  name: string
): Promise<number | undefined> {
  return await axios
    .post<{ id: number }>(
      baseURL + "/companies/" + companyId + "/gardens",
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

export async function getGardens(
  companyId: number
): Promise<Garden[] | undefined> {
  return await axios
    .get<Garden[]>(baseURL + "/companies/" + companyId + "/gardens", {
      headers: {
        Authorization: "Token " + storeToRefs(userStore()).getToken.value.token,
      },
    })
    .then(function (response): Garden[] {
      return response.data;
    })
    .catch(function (): undefined {
      return undefined;
    });
}
