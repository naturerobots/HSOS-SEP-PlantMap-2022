<template>
  <div class="fixed w-28 h-full z-10 bg-background shadow-3">
    <div class="text-center q-mt-sm q-mb-md">
      <router-link :to="'/dashboard'">
        <img
          src="@/assets/img/logo_small_white.svg"
          class="w-20 h-20 q-my-lg q-mx-auto"
        />
      </router-link>
    </div>
    <q-btn
      padding="30px xs"
      stack
      color="primary"
      flat
      class="full-width no-shadow"
    >
      <router-link to="/dashboard" class="text-black">
        <img src="@/assets/icons/dashboard.svg" class="q-mx-auto q-mb-sm" />
        <div>Dashboard</div>
      </router-link>
    </q-btn>
    <q-btn
      label=""
      padding="30px xs"
      stack
      color="primary"
      flat
      class="full-width"
    >
      <router-link to="/crops" style="text-decoration: none" class="text-black">
        <img src="@/assets/icons/crops.svg" class="q-mx-auto q-mb-sm" />
        <div class="text-no-wrap">Crops</div>
      </router-link>
    </q-btn>
    <q-btn
      label=""
      padding="30px xs"
      stack
      color="primary"
      flat
      class="full-width"
    >
      <router-link to="/3d" style="text-decoration: none" class="text-black">
        <img src="@/assets/icons/3d.svg" class="q-mx-auto q-mb-sm" />
        <div>3D</div>
      </router-link>
    </q-btn>
  </div>
</template>
<script setup lang="ts"></script>

<style></style>
