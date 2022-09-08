import { bedStore } from "@/stores/bedStore";
import { companyStore } from "@/stores/companyStore";
import { gardenStore } from "@/stores/gardenStore";
import { userStore } from "@/stores/userStore";
import type { Beds } from "@/types/beds";
import { storeToRefs } from "pinia";
import type { Ref } from "vue";

const baseURL = "http://127.0.0.1:8000";

let lastChunkFailed;

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
    const reader = response.body?.getReader();
    const beds: Beds = {
      bedList: [],
    };
    for await (const chunk of readChunks(reader)) {
      if (chunk) {
        let json; 
        try {
          if (lastChunkFailed) {
            lastChunkFailed += Utf8ArrayToStr(chunk);
            json = JSON.parse(lastChunkFailed);
          }
          else {
            json = JSON.parse(Utf8ArrayToStr(chunk));
          }
          beds.bedList.push(json);
          bedStore().setBed(json);
          lastChunkFailed = null;
        } catch (error) {
          console.log(error);
          lastChunkFailed = Utf8ArrayToStr(chunk);
        }
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
}
