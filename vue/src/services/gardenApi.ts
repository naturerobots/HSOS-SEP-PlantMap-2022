import axios from "axios";
import { userStore } from "@/stores/userStore";
import { storeToRefs } from "pinia";
import type { Garden } from "@/types/garden";
import type { GardenImage } from "@/types/gardenImage";

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

export async function getGardenImg(
  companyId: number,
  gardenId: number
): Promise<GardenImage | undefined> {
  return await axios
    .get<GardenImage>(
      baseURL + "/companies/" + companyId + "/gardens/" + gardenId + "/image",
      {
        headers: {
          Authorization:
            "Token " + storeToRefs(userStore()).getToken.value.token,
        },
      }
    )
    .then(function (response): GardenImage | undefined {
      if (response.status != 200) return undefined;

      return response.data;
    })
    .catch(function (): undefined {
      return undefined;
    });
}

export async function postGardenImg(
  companyId: number,
  gardenId: number,
  gardenImage: GardenImage
): Promise<boolean> {
  return await axios
    .post<GardenImage>(
      baseURL + "/companies/" + companyId + "/gardens/" + gardenId + "/image",
      gardenImage,
      {
        headers: {
          Authorization:
            "Token " + storeToRefs(userStore()).getToken.value.token,
        },
      }
    )
    .then(function (response): boolean {
      if (response.status != 201) return false;

      return true;
    })
    .catch(function (reason): boolean {
      return false;
    });
}

export async function deleteGarden(
  companyId: number,
  gardenId: number
): Promise<boolean> {
  return true;
  /* return await axios
    .delete(baseURL + "/companies/" + companyId + "/gardens/" + gardenId, {
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
