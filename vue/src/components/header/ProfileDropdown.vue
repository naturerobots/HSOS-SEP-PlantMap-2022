<template>
  <q-btn flat fab padding="0" ripple="false">
    <img
      alt="profil"
      src="https://images.pexels.com/photos/7457498/pexels-photo-7457498.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
      class="mx-auto object-cover rounded-full h-10 w-10"
    />
    <q-menu auto-close>
      <q-list style="min-width: 100px">
        <!-- TODO: add profile img + name -->
        <q-item clickable>
          <q-item-section>Profile</q-item-section>
        </q-item>
        <q-item clickable>
          <q-item-section>Settings</q-item-section>
        </q-item>
        <q-item clickable>
          <q-item-section>Help</q-item-section>
        </q-item>
        <q-separator />
        <q-item clickable @click="logoutUser()">
          <q-item-section>Logout</q-item-section>
        </q-item>
      </q-list>
    </q-menu>
  </q-btn>
</template>

<script setup lang="ts">
import { logout } from "@/services/userApi";
import { useRouter, type Router } from "vue-router";

const router: Router = useRouter();

async function logoutUser(): Promise<void> {
  await logout();
  router.push({ name: "login" });
}
</script>
