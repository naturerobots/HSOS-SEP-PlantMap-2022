<template>
  <base-layout title="Settings">
    <div class="p-4 max-w-lg">
      <div class="grid grid-cols-4 gap-4 place-items-stretch">
        <div class="col-span-4 space-y-2">
          <label class="font-bold text-black"> First Name </label>
          <input
            v-model="firstName"
            class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
            type="text"
            placeholder="Enter First Name"
          />
        </div>
        <div class="col-span-4 space-y-2">
          <label class="font-bold text-black"> Last Name </label>
          <input
            v-model="lastName"
            class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
            type="text"
            placeholder="Enter Last Name"
          />
        </div>
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
            type="text"
            placeholder="Password"
          />
        </div>
        <div class="col-span-4 space-y-2 pt-3">
          <button
            type="submit"
            class="w-full flex justify-center bg-primary text-white p-3 rounded-full tracking-wide font-bold shadow-lg"
            @click="changeUserDetails()"
          >
            Save
          </button>
        </div>
        <div class="col-span-4 space-y-2 pt-3">
          <button
            type="submit"
            class="w-full flex justify-center outline outline-1 outline-danger hover:text-white transition ease-in-out duration-300 text-[#FFA6A6] hover:bg-danger p-3 rounded-full tracking-wide font-bold shadow-lg"
            @click="deleteCompany()"
          >
            Delete Company
          </button>
        </div>
      </div>
    </div>
  </base-layout>
</template>

<script setup lang="ts">
import { onMounted, ref, type Ref } from "vue";
import { storeToRefs } from "pinia";
import BaseLayout from "@/components/layout/BaseLayout.vue";
import { userStore } from "@/stores/userStore";
import type { User } from "@/types/user";

const email: Ref<string | undefined> = ref<string>();
const password: Ref<string | undefined> = ref<string>();
const firstName: Ref<string | undefined> = ref<string>();
const lastName: Ref<string | undefined> = ref<string>();

const user: Ref<User> = storeToRefs(userStore()).getUser;

onMounted(() => {
  firstName.value = user.value.first_name;
  lastName.value = user.value.last_name;
  email.value = user.value.username;
});

async function changeUserDetails(): Promise<void> {
  userStore().editUser(
    firstName.value === user.value.first_name ? undefined : firstName.value,
    lastName.value === user.value.last_name ? undefined : lastName.value,
    email.value === user.value.username ? undefined : email.value,
    password.value === "" ? undefined : password.value
  );
}

async function deleteCompany(): Promise<void> {
  /* TODO: implement delete */
}
</script>
