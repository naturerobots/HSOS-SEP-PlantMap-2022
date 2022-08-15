import type { Plants } from "@/types/plants";
import axios from "axios";
import { storeToRefs } from "pinia";
import { userStore } from "@/stores/userStore";
import type { Ref } from "vue";
import { companyStore } from "@/stores/companyStore";
import { gardenStore } from "@/stores/gardenStore";
import { cropsStore } from "@/stores/cropsStore";

export async function getCrops(plantsUrl: string): Promise<Plants> {
  return await axios
    .get<Plants>(plantsUrl, {
      headers: {
        Authorization: "Token " + storeToRefs(userStore()).getToken.value.token,
      },
    })
    .then(function (response): Plants {
      cropsStore().setCrops(response.data.plants);
      return response.data;
    });
}
