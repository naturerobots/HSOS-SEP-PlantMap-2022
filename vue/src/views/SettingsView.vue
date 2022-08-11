<template>
  <base-layout title="Settings">
    <div class="p-4 grid grid-cols-6 gap-8">
      <div class="col-span-2">
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
        </div>
      </div>
      <div class="col-span-2">
        <h6 class="pb-4">Admin settings</h6>
        <div class="grid grid-cols-4 gap-4 place-items-stretch">
          <div class="col-span-4 space-y-2">
            <button
              type="submit"
              class="w-full flex justify-center bg-primary text-white p-3 rounded-full tracking-wide font-bold shadow-lg"
              @click="repositionGardenImage()"
            >
              Reposition garden image
            </button>
          </div>
          <div class="col-span-2 space-y-2">
            <label class="font-bold text-black">
              Add user to current company
            </label>
            <input
              v-model="addUsernameCompany"
              class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
              type="text"
              placeholder="Username"
            />
            <q-toggle v-model="companyAdmin" label="admin" />
            <button
              type="submit"
              class="w-full flex justify-center bg-primary text-white p-3 rounded-full tracking-wide font-bold shadow-lg"
              @click="addUsernameToCompany()"
            >
              Add
            </button>
          </div>
          <div class="col-span-2 space-y-2">
            <label class="font-bold text-black">
              Add user to current garden
            </label>
            <input
              v-model="addUsernameGarden"
              class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
              type="text"
              placeholder="Username"
            />
            <q-toggle v-model="gardenAdmin" label="admin" />
            <button
              type="submit"
              class="w-full flex justify-center bg-primary text-white p-3 rounded-full tracking-wide font-bold shadow-lg"
              @click="addUsernameToGarden()"
            >
              Add
            </button>
          </div>
          <div class="col-span-2 space-y-2">
            <label class="font-bold text-black">
              Remove user from current company
            </label>
            <input
              v-model="removeUsernameCompany"
              class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
              type="text"
              placeholder="Username"
            />
            <button
              type="submit"
              class="w-full flex justify-center outline outline-1 outline-danger hover:text-white transition ease-in-out duration-300 text-[#FFA6A6] hover:bg-danger p-3 rounded-full tracking-wide font-bold shadow-lg"
              @click="removeUsernameToCompany()"
            >
              Remove
            </button>
          </div>
          <div class="col-span-2 space-y-2">
            <label class="font-bold text-black">
              Remove user from current garden
            </label>
            <input
              v-model="removeUsernameGarden"
              class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
              type="text"
              placeholder="Username"
            />
            <button
              type="submit"
              class="w-full flex justify-center outline outline-1 outline-danger hover:text-white transition ease-in-out duration-300 text-[#FFA6A6] hover:bg-danger p-3 rounded-full tracking-wide font-bold shadow-lg"
              @click="removeUsernameToGarden()"
            >
              Remove
            </button>
          </div>
          <div class="col-span-4 space-y-4 pt-3">
            <button
              type="submit"
              class="w-full flex justify-center outline outline-1 outline-danger hover:text-white transition ease-in-out duration-300 text-[#FFA6A6] hover:bg-danger p-3 rounded-full tracking-wide font-bold shadow-lg"
              @click="deleteGarden()"
            >
              Delete current garden
            </button>
            <button
              type="submit"
              class="w-full flex justify-center outline outline-1 outline-danger hover:text-white transition ease-in-out duration-300 text-[#FFA6A6] hover:bg-danger p-3 rounded-full tracking-wide font-bold shadow-lg"
              @click="deleteCompany()"
            >
              Delete current Company
            </button>
          </div>
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
import { companyStore } from "@/stores/companyStore";
import { gardenStore } from "@/stores/gardenStore";
import type { User } from "@/types/user";
import { useRouter, type Router } from "vue-router";

const router: Router = useRouter();
const email: Ref<string | undefined> = ref<string>();
const password: Ref<string | undefined> = ref<string>();
const firstName: Ref<string | undefined> = ref<string>();
const lastName: Ref<string | undefined> = ref<string>();

const addUsernameCompany: Ref<string | undefined> = ref<string>();
const addUsernameGarden: Ref<string | undefined> = ref<string>();

const removeUsernameCompany: Ref<string | undefined> = ref<string>();
const removeUsernameGarden: Ref<string | undefined> = ref<string>();

const companyAdmin: Ref<boolean | undefined> = ref<boolean>(false);
const gardenAdmin: Ref<boolean | undefined> = ref<boolean>(false);

const user: Ref<User> = storeToRefs(userStore()).getUser;

const companyId: Ref<number | undefined> = storeToRefs(
  companyStore()
).getSelectedCompany;
const gardenId: Ref<number | undefined> = storeToRefs(
  gardenStore()
).getSelectedGarden;

onMounted(() => {
  firstName.value = user.value.first_name;
  lastName.value = user.value.last_name;
  email.value = user.value.username;
});

function repositionGardenImage(): void {
  router.push({ path: "/cropimage" });
}

async function changeUserDetails(): Promise<void> {
  userStore().editUser(
    firstName.value === user.value.first_name ? undefined : firstName.value,
    lastName.value === user.value.last_name ? undefined : lastName.value,
    email.value === user.value.username ? undefined : email.value,
    password.value === "" ? undefined : password.value
  );
}

async function deleteGarden(): Promise<void> {
  if (!companyId.value || !gardenId.value) return;

  if (!(await gardenStore().deleteGarden(companyId.value, gardenId.value))) {
    console.log("Don't have the permissions to delete the garden"); //TODO: user feedback
    return;
  }

  //TODO: success: user feedback
}

async function deleteCompany(): Promise<void> {
  if (!companyId.value) return;

  if (!(await companyStore().deleteCompany(companyId.value))) {
    console.log("Don't have the permissions to delete the company"); //TODO: user feedback
    return;
  }

  if (companyId.value) {
    await gardenStore().loadDataFromApi(companyId.value);
    const gardenId = storeToRefs(gardenStore()).getGardens?.value[0]?.id;
    if (gardenId) {
      gardenStore().setSelectedGarden(gardenId);
    } else {
      gardenStore().setSelectedGarden(undefined);
    }
  } else {
    await gardenStore().resetStore();
  }

  //TODO: success: user feedback
}

/* TODO: user feedback */
async function addUsernameToCompany() {
  if (!addUsernameCompany.value || !companyId.value) return;

  userStore().addPermissionToCompany(
    addUsernameCompany.value,
    companyAdmin,
    companyId.value
  );
}

async function removeUsernameToCompany() {
  if (!removeUsernameCompany.value || !companyId.value) return;

  userStore().removePermissionFromCompany(
    removeUsernameCompany.value,
    companyId.value
  );
}

async function addUsernameToGarden() {
  if (!addUsernameGarden.value || !companyId.value || !gardenId.value) return;

  userStore().addPermissionToGarden(
    addUsernameGarden.value,
    gardenAdmin,
    companyId.value,
    gardenId.value
  );
}

async function removeUsernameToGarden() {
  if (!removeUsernameGarden.value || !companyId.value || !gardenId.value)
    return;

  userStore().removePermissionFromGarden(
    removeUsernameGarden.value,
    companyId.value,
    gardenId.value
  );
}
</script>
