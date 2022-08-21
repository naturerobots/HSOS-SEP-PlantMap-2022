import type { Crops } from "@/types/crops";
import axios from "axios";
import { storeToRefs } from "pinia";
import { userStore } from "@/stores/userStore";
import type { Ref } from "vue";
import { companyStore } from "@/stores/companyStore";
import { gardenStore } from "@/stores/gardenStore";
import { cropsStore } from "@/stores/cropsStore";

export async function getCrops(url: string): Promise<Crops> {
  return await axios
    .get<Crops>(url, {
      headers: {
        Authorization: "Token " + storeToRefs(userStore()).getToken.value.token,
      },
    })
    .then(function (response): Crops {
      cropsStore().setCrops(response.data.plants);
      return response.data;
    });
}
