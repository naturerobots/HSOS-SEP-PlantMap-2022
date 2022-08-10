import axios, { type responseEncoding } from "axios";
import { userStore } from "@/stores/userStore";
import { storeToRefs } from "pinia";
import type { StoreOption } from "@/types/WidgetOption";

const baseURL = "http://127.0.0.1:8000";

export async function postWidgets(widgets: StoreOption[]): Promise<boolean> {
  return await axios
    .post<boolean>(
      baseURL + "/user-info/widgets",
      { widgets: widgets },
      {
        headers: {
          Authorization:
            "Token " + storeToRefs(userStore()).getToken.value.token,
        },
      }
    )
    .then(function (): boolean {
      return true;
    })
    .catch(function (): boolean {
      return false;
    });
}

export async function getWidgets(): Promise<StoreOption[] | undefined> {
  return await axios
    .get<StoreOption[]>(baseURL + "/user-info/widgets", {
      headers: {
        Authorization: "Token " + storeToRefs(userStore()).getToken.value.token,
      },
    })
    .then(function (response): StoreOption[] {
      return response.data;
    })
    .catch(function (): undefined {
      return undefined;
    });
}
