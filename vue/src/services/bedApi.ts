import { bedStore } from "@/stores/bedStore";
import { companyStore } from "@/stores/companyStore";
import { gardenStore } from "@/stores/gardenStore";
import { userStore } from "@/stores/userStore";
import type { Bed } from "@/types/bed";
import type { Beds } from "@/types/beds";
import axios, { type AxiosResponse } from "axios";
import { storeToRefs } from "pinia";
import type { Stream } from "stream";
import type { Ref } from "vue";

const baseURL = "http://127.0.0.1:8000";

export async function loadBeds(): Promise<boolean> {
  const companyId: Ref<number | undefined> = storeToRefs(
    companyStore()
  ).getSelectedCompany;
  const gardenId: Ref<number | undefined> = storeToRefs(
    gardenStore()
  ).getSelectedGarden;

  const loading = fetch(
    baseURL +
      "/companies/" +
      companyId.value +
      "/gardens/" +
      gardenId.value +
      "/beds",
    {
      headers: {
        Authorization: "Token " + storeToRefs(userStore()).getToken.value.token,
      },
    }
  ).then(async (response) => {
    // response.body is a ReadableStream
    const reader = response.body?.getReader();
    const beds: Beds = {
      beds: [],
    };
    for await (const chunk of readChunks(reader)) {
      console.log(`received chunk of size ${chunk?.length}`);
      if (chunk) {
        console.log(Utf8ArrayToStr(chunk));
        const json = JSON.parse(Utf8ArrayToStr(chunk));
        //console.log(json);
        beds.beds.push(json);
        //console.log(beds);
        bedStore().setBed(json);
      }
    }
    return false;
  });
  return loading;

  // readChunks() reads from the provided reader and yields the results into an async iterable
  function readChunks(
    reader: ReadableStreamDefaultReader<Uint8Array> | undefined
  ) {
    return {
      async *[Symbol.asyncIterator]() {
        let readResult = await reader?.read();
        while (!readResult?.done) {
          yield readResult?.value;
          readResult = await reader?.read();
        }
      },
    };
  }

  //https://jsfiddle.net/3VuLx/2/
  function Utf8ArrayToStr(array: any) {
    let out, i, c;
    let char2, char3;

    out = "";
    const len = array.length;
    i = 0;
    while (i < len) {
      c = array[i++];
      switch (c >> 4) {
        case 0:
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
        case 6:
        case 7:
          // 0xxxxxxx
          out += String.fromCharCode(c);
          break;
        case 12:
        case 13:
          // 110x xxxx   10xx xxxx
          char2 = array[i++];
          out += String.fromCharCode(((c & 0x1f) << 6) | (char2 & 0x3f));
          break;
        case 14:
          // 1110 xxxx  10xx xxxx  10xx xxxx
          char2 = array[i++];
          char3 = array[i++];
          out += String.fromCharCode(
            ((c & 0x0f) << 12) | ((char2 & 0x3f) << 6) | ((char3 & 0x3f) << 0)
          );
          break;
      }
    }

    return out;
  }

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
