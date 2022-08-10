<template>
  <div class="w-max m-auto px-14">
    <div class="mb-6 text-center">
      <h3 class="text-3xl font-bold">Welcome back</h3>
      <p class="text-secondary pt-2 font-bold">
        Welcome back! Please enter your details.
      </p>
    </div>
    <div class="grid grid-cols-4 gap-4 place-items-stretch">
      <div class="col-span-4 space-y-2">
        <label class="font-bold text-black"> Email </label>
        <input
          v-model="email"
          class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
          type="email"
          placeholder="Enter Email Address"
        />
      </div>
      <div class="col-span-4 space-y-2">
        <label class="font-bold text-black"> Password </label>
        <input
          v-model="password"
          class="w-full content-center text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
          type="password"
          placeholder="Password"
        />
      </div>
      <div class="col-span-4 space-y-2 pt-3">
        <button
          type="submit"
          class="w-full flex justify-center bg-primary text-white p-3 rounded-full tracking-wide font-bold shadow-lg"
          @click="login"
        >
          Login
        </button>
        <p class="text-center pt-3 text-secondary">
          Don't have an account?
          <router-link to="/register" class="pl-1 text-black font-bold">
            Sign up for free
          </router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, type Ref } from "vue";
import { storeToRefs } from "pinia";
import { useRouter, type Router } from "vue-router";
import { userStore } from "@/stores/userStore";
import { companyStore } from "@/stores/companyStore";
import { gardenStore } from "@/stores/gardenStore";

const router: Router = useRouter();
const email: Ref<string | undefined> = ref<string>();
const password: Ref<string | undefined> = ref<string>();

async function login(): Promise<void> {
  const isLoggedIn: boolean = await userStore().loginUser(
    email.value,
    password.value
  );
  if (isLoggedIn) {
    await companyStore().loadDataFromApi();
    const companyId = storeToRefs(companyStore()).getCompanies?.value[0]?.id;
    if (companyId) {
      companyStore().setSelectedCompany(companyId);
      await gardenStore().loadDataFromApi(companyId);
      const gardenId = storeToRefs(gardenStore()).getGardens?.value[0]?.id;
      if (gardenId) {
        gardenStore().setSelectedGarden(gardenId);
        await gardenStore().loadSelectedGardenImg(companyId);
      }
    }

    router.push({ path: "/" });
  } else {
    console.log("User Feedback: Login failed");
    /* TODO: user feedback */
  }
}
</script>
