import { userStore } from "@/stores/userStore";
import type { Bed } from "@/types/bed";
import type { Beds } from "@/types/beds";
import axios from "axios";
import { storeToRefs } from "pinia";
import type { Stream } from "stream";

const baseURL = "http://127.0.0.1:8000";

export async function getBeds() {
  // return await axios.get<Beds>(baseURL + "/companies/1/gardens/1/beds", {
  //     headers: {
  //       Authorization: "Token " + storeToRefs(userStore()).getToken.value.token
  //     },
  //     responseType: 'stream'
  //   })
  //   .then(function (response): Beds {
  //     console.log(response);
  //     // console.log(response.data.beds[0].plant);
  //     return response.data;
  //   });

  const response = await axios.get(baseURL + "/companies/1/gardens/1/beds", {
    headers: {
      Authorization: "Token " + storeToRefs(userStore()).getToken.value.token,
    },
    responseType: "stream",
  });

  const stream = response.data;

  console.log(stream);
  stream.on("data", (data: any) => {
    console.log(data);
  });

  stream.on("end", () => {
    console.log("stream done");
  });

  //static demo data
  //   const crops: Bed[] = [];

  //   const crop1: Bed = {
  //     id: 1,
  //     plant: "Beans",
  //     variety: "Cauliflower",
  //     // location: 1,
  //     soil_humidity: 0.65,
  //     health: [
  //       {
  //         type: "nutrients",
  //         loglevel: 2,
  //         shortcut: "N",
  //       },
  //       {
  //         type: "water",
  //         loglevel: 0,
  //         shortcut: "W",
  //       },
  //       {
  //         type: "diseases",
  //         loglevel: 2,
  //         shortcut: "D",
  //       },
  //     ],
  //     // status: "vegetating",
  //     harvest: "3 months",
  //     yield: "N/A",
  //   };
  //   const crop2: Bed = {
  //     id: 2,
  //     plant: "Beetroot",
  //     variety: "Carrot",
  //     // location: 2,
  //     soil_humidity: 0.05,
  //     health: [
  //       {
  //         type: "nutrients",
  //         loglevel: 1,
  //         shortcut: "N",
  //       },
  //       {
  //         type: "water",
  //         loglevel: 1,
  //         shortcut: "W",
  //       },
  //       {
  //         type: "diseases",
  //         loglevel: 2,
  //         shortcut: "D",
  //       },
  //     ],
  //     // status: "ripening",
  //     harvest: "12 months",
  //     yield: "N/A",
  //   };
  //   const crop3: Bed = {
  //     id: 3,
  //     plant: "Broccoli",
  //     variety: "Chicory",
  //     // location: 3,
  //     soil_humidity: 0.45,
  //     health: [
  //       {
  //         type: "nutrients",
  //         loglevel: 1,
  //         shortcut: "N",
  //       },
  //       {
  //         type: "water",
  //         loglevel: 3,
  //         shortcut: "W",
  //       },
  //       {
  //         type: "diseases",
  //         loglevel: 2,
  //         shortcut: "D",
  //       },
  //     ],
  //     // status: "budding",
  //     harvest: "4 weeks",
  //     yield: "N/A",
  //   };
  //   const crop4: Bed = {
  //     id: 4,
  //     plant: "Carrot",
  //     variety: "Courgette",
  //     // location: 1,
  //     soil_humidity: 0.15,
  //     health: [
  //       {
  //         type: "nutrients",
  //         loglevel: 3,
  //         shortcut: "N",
  //       },
  //       {
  //         type: "water",
  //         loglevel: 1,
  //         shortcut: "W",
  //       },
  //       {
  //         type: "diseases",
  //         loglevel: 2,
  //         shortcut: "D",
  //       },
  //     ],
  //     // status: "flowering",
  //     harvest: "5 weeks",
  //     yield: "N/A",
  //   };
  //   const crop5: Bed = {
  //     id: 5,
  //     plant: "Chicory",
  //     variety: "Courgette",
  //     // location: 1,
  //     soil_humidity: 0.61,
  //     health: [
  //       {
  //         type: "nutrients",
  //         loglevel: 2,
  //         shortcut: "N",
  //       },
  //       {
  //         type: "water",
  //         loglevel: 3,
  //         shortcut: "W",
  //       },
  //       {
  //         type: "diseases",
  //         loglevel: 2,
  //         shortcut: "D",
  //       },
  //     ],
  //     // status: "budding",
  //     harvest: "1 month",
  //     yield: "N/A",
  //   };
  //   const crop6: Bed = {
  //     id: 6,
  //     plant: "Pepper",
  //     variety: "Radish",
  //     // location: 4,
  //     soil_humidity: 0.37,
  //     health: [
  //       {
  //         type: "nutrients",
  //         loglevel: 3,
  //         shortcut: "N",
  //       },
  //       {
  //         type: "water",
  //         loglevel: 2,
  //         shortcut: "W",
  //       },
  //       {
  //         type: "diseases",
  //         loglevel: 1,
  //         shortcut: "D",
  //       },
  //     ],
  //     // status: "budding",
  //     harvest: "2 months",
  //     yield: "N/A",
  //   };

  //   crops.push(crop3);
  //   crops.push(crop4);
  //   crops.push(crop1);
  //   crops.push(crop2);
  //   crops.push(crop5);
  //   crops.push(crop6);

  //   return crops;
}
