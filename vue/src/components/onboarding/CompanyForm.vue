<template>
  <div class="bg-white grid grid-rows-6 gap-4 h-full">
    <div>
      <div class="flex h-full pl-14">
        <img
          class="w-56"
          src="@/assets/img/logo_with_text.svg"
          alt="Nature Robots"
        />
      </div>
    </div>
    <div class="row-span-4 place-self-center">
      <div class="w-max m-auto px-14">
        <div class="mb-6 text-center">
          <h3 class="text-3xl font-bold">Create a Company</h3>
          <p class="text-secondary pt-2 font-bold">
            Please enter your details.
          </p>
        </div>
        <div class="grid grid-cols-4 gap-4 place-items-stretch">
          <div class="col-span-4 space-y-2">
            <label class="font-bold text-black"> Name* </label>
            <input
              v-model="companyName"
              class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
              type="text"
              placeholder="Enter Company name"
            />
          </div>
          <div class="col-span-3 space-y-2">
            <label class="font-bold text-black"> Street </label>
            <input
              class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
              type="text"
              placeholder="Enter Street Name"
            />
          </div>
          <div class="col-span-1 space-y-2">
            <label class="font-bold text-black"> Number </label>
            <input
              class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
              type="text"
              placeholder="Number"
            />
          </div>
          <div class="col-span-2 space-y-2">
            <label class="font-bold text-black"> City </label>
            <input
              class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
              type="text"
              placeholder="Enter City"
            />
          </div>
          <div class="col-span-2 space-y-2">
            <label class="font-bold text-black"> Zip/Postal Code </label>
            <input
              class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
              type="text"
              placeholder="Enter Zip/Postal Code"
            />
          </div>
          <div class="col-span-4 space-y-2 pt-3">
            <button
              type="submit"
              class="w-full flex justify-center bg-primary text-white p-3 rounded-full tracking-wide font-bold shadow-lg"
              @click="company()"
            >
              Create
            </button>
            <p class="text-center pt-3 text-secondary">
              <a
                @click="finishOnboarding()"
                class="pl-1 text-black font-bold cursor-pointer"
              >
                Cancel
              </a>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, type Ref } from "vue";
import { useRouter, type Router } from "vue-router";
import { createCompany } from "@/services/companyApi";
import { companyStore } from "@/stores/companyStore";

const router: Router = useRouter();

const companyName: Ref<string | undefined> = ref<string>();
let companyId: number | undefined;

async function company(): Promise<void> {
  if (companyName.value) {
    companyId = await createCompany(companyName.value);

    if (companyId) {
      await companyStore().loadDataFromApi();
      companyStore().setSelectedCompany(companyId);
      router.push({ name: "onboarding-garden" });
    } else {
      /* TODO: add user feedback */
    }
  }
}

function finishOnboarding(): void {
  router.push({ name: "dashboard" });
}
</script>
