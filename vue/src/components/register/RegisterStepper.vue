<template>
  <div class="register">
    <div class="mb-6">
      <h3 class="text-3xl font-bold">Sign up</h3>
      <p class="text-secondary pt-2 font-bold">
        Sign up for free. Please enter your details.
      </p>
    </div>
    <q-stepper v-model="step" header-nav ref="stepper" color="primary" flat>
      <q-step
        :name="1"
        title="Details"
        icon="info"
        :done="step > 1"
        :header-nav="step > 1"
      >
        <div class="grid grid-cols-4 gap-4 place-items-stretch">
          <div class="col-span-4 space-y-2">
            <label class="font-bold text-black"> Last Name </label>
            <input
              class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
              type="text"
              placeholder="Enter Last Name"
            />
          </div>
          <div class="col-span-4 space-y-2">
            <label class="font-bold text-black"> First Name </label>
            <input
              class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
              type="text"
              placeholder="Enter First Name"
            />
          </div>
          <div class="col-span-4 space-y-2 pt-3">
            <button
              @click="
                () => {
                  step = 2;
                }
              "
              type="submit"
              class="w-full flex justify-center bg-primary text-white p-3 rounded-full tracking-wide font-bold shadow-lg"
            >
              Continue
            </button>
            <p class="text-center pt-3 text-secondary">
              Already a member?
              <router-link to="/login" class="pl-1 text-black font-bold">
                Login
              </router-link>
            </p>
          </div>
        </div>
      </q-step>

      <q-step
        :name="2"
        title="Account"
        icon="account_circle"
        :done="step > 2"
        :header-nav="step > 2"
      >
        <div class="grid grid-cols-4 gap-4 place-items-stretch">
          <div class="col-span-4 space-y-2">
            <label class="font-bold text-black"> Email </label>
            <input
              class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
              type="email"
              placeholder="Enter Email Address"
            />
          </div>
          <div class="col-span-4 space-y-2">
            <label class="font-bold text-black"> Password </label>
            <input
              class="w-full content-center text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
              type="text"
              placeholder="Enter Password"
            />
          </div>
          <div class="col-span-4 space-y-2">
            <label class="font-bold text-black"> Repeat Password </label>
            <input
              class="w-full content-center text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
              type="text"
              placeholder="Repeat Password"
            />
          </div>
          <div class="col-span-4 space-y-2 pt-3">
            <button
              @click="
                () => {
                  step = 3;
                }
              "
              type="submit"
              class="w-full flex justify-center bg-primary text-white p-3 rounded-full tracking-wide font-bold shadow-lg mb-2"
            >
              Sign up
            </button>
            <p class="text-center pt-3 text-secondary">
              <a
                @click="step = 1"
                class="pl-1 text-black font-bold cursor-pointer"
              >
                Back
              </a>
            </p>
          </div>
        </div>
      </q-step>

      <q-step
        :name="3"
        title="Verification"
        icon="pin"
        :done="step > 3"
        :header-nav="step > 3"
      >
        <div class="grid grid-cols-4 gap-4 place-items-stretch">
          <div class="col-span-4 space-y-2">
            <p>
              Please confirm your account by entering the authorization code
              sent to <b>*******@mail.com</b>.
            </p>
          </div>
          <div class="col-span-4 space-y-2">
            <label class="font-bold text-black"> Code </label>
            <fieldset class="p-0 mt-6">
              <div>
                <input
                  class="w-12 mr-4 text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
                />
                <input
                  class="w-12 mr-4 text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
                />
                <input
                  class="w-12 mr-4 text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
                />
                <input
                  class="w-12 mr-4 text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
                />
                <input
                  class="w-12 mr-4 text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
                />
                <input
                  class="w-12 mr-4 text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
                />
              </div>
            </fieldset>
          </div>
          <div class="col-span-4 space-y-2 pt-3">
            <button
              @click="startOnboarding()"
              type="submit"
              class="w-full flex justify-center bg-primary text-white p-3 rounded-full tracking-wide font-bold shadow-lg mb-2"
            >
              Confirm
            </button>
          </div>
        </div>
      </q-step>
    </q-stepper>
  </div>
</template>

<script setup lang="ts">
import { ref, type Ref } from "vue";
import { useRouter, type Router } from "vue-router";

const step: Ref<number> = ref(1);
const router: Router = useRouter();

function startOnboarding(): void {
  router.push({ name: "onboarding" });
}
</script>

<style>
.register {
  width: 500px;
}
</style>
