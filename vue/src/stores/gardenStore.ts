import { defineStore } from "pinia";
import type { Garden } from "@/types/garden";
import { getGardenImg, getGardens, postGardenImg } from "@/services/gardenApi";
import type { GardenImage } from "@/types/gardenImage";

// TODO: move to types/store
interface gardenStore {
  gardens: Garden[];
  selectedGarden: number | undefined;
  gardenImage: {
    image: GardenImage | undefined;
  };
}

export const gardenStore = defineStore({
  id: "gardenStore",
  state: (): gardenStore => ({
    gardens: [] as Garden[],
    selectedGarden: undefined,
    gardenImage: {
      image: undefined,
    },
  }),
  getters: {
    getGardens(state: gardenStore): Garden[] {
      return state.gardens;
    },
    getSelectedGarden(state: gardenStore): number | undefined {
      return state.selectedGarden;
    },
    getGardenImage(state: gardenStore): { image: GardenImage | undefined } {
      //GardenImage | undefined {//
      return state.gardenImage;
    },
  },
  actions: {
    async loadDataFromApi(companyId: number): Promise<void> {
      const response = await getGardens(companyId);
      if (response) {
        this.gardens = response;
      }
    },
    setSelectedGarden(gardenId: number): void {
      /* TODO: check if id exists in gardens */
      this.selectedGarden = gardenId;
    },
    async loadSelectedGardenImg(companyId: number): Promise<void> {
      if (!this.selectedGarden) {
        Promise.reject("Selected Garden is undefined");
      }

      const currentGarden: Garden | undefined = this.gardens.find(
        (garden) => garden.id === this.selectedGarden
      );

      if (!currentGarden) {
        Promise.reject("Garden does not exist");
      }

      if (!currentGarden?.image_path) {
        return;
      }

      const responseImg = await getGardenImg(
        this.gardens.find((garden) => garden.id === this.selectedGarden)!
          .company,
        this.selectedGarden as number
      );

      // const responseImg = await getGardenImg(
      //   companyId,
      //   this.selectedGarden as number
      // );

      if (responseImg) {
        this.gardenImage.image = responseImg;
      }
    },
    async setSelectedGardenImg(
      companyId: number,
      gardenImage: GardenImage
    ): Promise<void> {
      if (!this.selectedGarden) {
        Promise.reject("Selected Garden is undefined");
      }

      const currentGarden: Garden | undefined = this.gardens.find(
        (garden) => garden.id === this.selectedGarden
      );

      if (!currentGarden) {
        Promise.reject("Garden does not exist");
      }

      const responseImg = await postGardenImg(
        currentGarden!.company,
        this.selectedGarden as number,
        gardenImage
      );

      if (responseImg && this.gardenImage) {
        this.gardenImage.image = gardenImage;
      }
    },
  },
});
