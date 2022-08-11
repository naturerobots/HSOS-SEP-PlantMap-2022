import type { Crop } from "@/types/crop";
import type { Plants } from "@/types/plants";
import axios from "axios";
import { storeToRefs } from "pinia";
import { userStore } from "@/stores/userStore";
import type { Ref } from "vue";
import { companyStore } from "@/stores/companyStore";
import { gardenStore } from "@/stores/gardenStore";
import type { Garden } from "@/types/garden";
import { cropsStore } from "@/stores/cropsStore";

const baseURL = "http://127.0.0.1:8000";

export async function getCrops(plantsUrl: string): Promise<Plants> {
  // const companyId: Ref<number | undefined> = storeToRefs(
  //   companyStore()
  // ).getSelectedCompany;
  // const gardenId: Ref<number | undefined> = storeToRefs(
  //   gardenStore()
  // ).getSelectedGarden;
  // console.log("Company: " + companyId.value);
  // console.log("Garden: " + gardenId.value);
  return await axios
    .get<Plants>(
      // baseURL +
      //   "/companies/1/gardens/1/beds/1/plants",
      plantsUrl,
      {
        headers: {
          Authorization:
            "Token " + storeToRefs(userStore()).getToken.value.token,
        },
      }
    )
    .then(function (response): Plants {
      console.log(response.data.plants[0].plant);
      cropsStore().setCrops(response.data.plants);
      return response.data;
    });

  //static demo data
  // const crops: Crop[] = [];

  // const crop1: Crop = {
  //   id: 1,
  //   bed_id: 1,
  //   plant: "Beans",
  //   variety: "Cauliflower",
  //   // location: 1,
  //   soilHumidity: "65%",
  //   health: [
  //     {
  //       type: "Nutrient Deficiency",
  //       loglevel: 2,
  //       shortcut: "N",
  //     },
  //     {
  //       type: "Watering",
  //       loglevel: 0,
  //       shortcut: "W",
  //     },
  //     {
  //       type: "Disease Detection",
  //       loglevel: 2,
  //       shortcut: "D",
  //     },
  //   ],
  //   // status: "vegetating",
  //   harvest: "3 months",
  //   yield: "N/A",
  // };
  // const crop2: Crop = {
  //   id: 2,
  //   bed_id: 1,
  //   plant: "Beetroot",
  //   variety: "Carrot",
  //   // location: 2,
  //   soilHumidity: "5%",
  //   health: [
  //     {
  //       type: "Nutrient Deficiency",
  //       loglevel: 1,
  //       shortcut: "N",
  //     },
  //     {
  //       type: "Watering",
  //       loglevel: 1,
  //       shortcut: "W",
  //     },
  //     {
  //       type: "Disease Detection",
  //       loglevel: 2,
  //       shortcut: "D",
  //     },
  //   ],
  //   // status: "ripening",
  //   harvest: "12 months",
  //   yield: "N/A",
  // };
  // const crop3: Crop = {
  //   id: 3,
  //   bed_id: 1,
  //   plant: "Broccoli",
  //   variety: "Chicory",
  //   // location: 3,
  //   soilHumidity: "45%",
  //   health: [
  //     {
  //       type: "Nutrient Deficiency",
  //       loglevel: 1,
  //       shortcut: "N",
  //     },
  //     {
  //       type: "Watering",
  //       loglevel: 3,
  //       shortcut: "W",
  //     },
  //     {
  //       type: "Disease Detection",
  //       loglevel: 2,
  //       shortcut: "D",
  //     },
  //   ],
  //   // status: "budding",
  //   harvest: "4 weeks",
  //   yield: "N/A",
  // };
  // const crop4: Crop = {
  //   id: 4,
  //   bed_id: 1,
  //   plant: "Carrot",
  //   variety: "Courgette",
  //   // location: 1,
  //   soilHumidity: "15%",
  //   health: [
  //     {
  //       type: "Nutrient Deficiency",
  //       loglevel: 3,
  //       shortcut: "N",
  //     },
  //     {
  //       type: "Watering",
  //       loglevel: 1,
  //       shortcut: "W",
  //     },
  //     {
  //       type: "Disease Detection",
  //       loglevel: 2,
  //       shortcut: "D",
  //     },
  //   ],
  //   // status: "flowering",
  //   harvest: "5 weeks",
  //   yield: "N/A",
  // };
  // const crop5: Crop = {
  //   id: 5,
  //   bed_id: 1,
  //   plant: "Chicory",
  //   variety: "Courgette",
  //   // location: 1,
  //   soilHumidity: "61%",
  //   health: [
  //     {
  //       type: "Nutrient Deficiency",
  //       loglevel: 2,
  //       shortcut: "N",
  //     },
  //     {
  //       type: "Watering",
  //       loglevel: 3,
  //       shortcut: "W",
  //     },
  //     {
  //       type: "Disease Detection",
  //       loglevel: 2,
  //       shortcut: "D",
  //     },
  //   ],
  //   // status: "budding",
  //   harvest: "1 month",
  //   yield: "N/A",
  // };
  // const crop6: Crop = {
  //   id: 6,
  //   bed_id: 1,
  //   plant: "Pepper",
  //   variety: "Radish",
  //   // location: 4,
  //   soilHumidity: "37%",
  //   health: [
  //     {
  //       type: "Nutrient Deficiency",
  //       loglevel: 3,
  //       shortcut: "N",
  //     },
  //     {
  //       type: "Watering",
  //       loglevel: 2,
  //       shortcut: "W",
  //     },
  //     {
  //       type: "Disease Detection",
  //       loglevel: 1,
  //       shortcut: "D",
  //     },
  //   ],
  //   // status: "budding",
  //   harvest: "2 months",
  //   yield: "N/A",
  // };

  // crops.push(crop3);
  // crops.push(crop4);
  // crops.push(crop1);
  // crops.push(crop2);
  // crops.push(crop5);
  // crops.push(crop6);

  // return crops;
}
