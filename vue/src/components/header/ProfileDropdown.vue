<template>
  <q-btn flat fab padding="0" :ripple="false">
    <img
      alt="profil"
      src="https://images.pexels.com/photos/7457498/pexels-photo-7457498.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
      class="mx-auto object-cover rounded-full h-10 w-10"
    />
    <q-menu auto-close>
      <q-list style="min-width: 100px">
        <!-- TODO: add profile img + name -->
        <q-item clickable @click="openAdministration()">
          <q-item-section>Administration</q-item-section>
        </q-item>
        <q-separator />
        <q-item clickable to="settings">
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

  <q-dialog v-model="alert">
    <q-card class="w-96">
      <q-card-section>
        <div class="text-h6">Administration</div>
      </q-card-section>
      <q-card-section class="q-pt-none">
        <div v-if="storeCompanyId">
          <p class="m-0">Select Company</p>
          <q-select
            v-model="selectedCompany"
            :options="companies"
            option-value="id"
            option-label="name"
            emit-value
            map-options
          />
        </div>
        <div v-if="storeGardenId">
          <p class="m-0">Select Garden</p>
          <q-select
            v-model="selectedGarden"
            :options="gardens"
            option-value="id"
            option-label="name"
            emit-value
            map-options
          />
        </div>
      </q-card-section>

      <q-card-actions align="right">
        <q-btn flat label="Cancel" color="secondary" v-close-popup />
        <q-btn
          flat
          label="Save"
          color="primary"
          @click="setCompanyAndGarden()"
          v-close-popup
        />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script setup lang="ts">
import { logout } from "@/services/userApi";
import { companyStore } from "@/stores/companyStore";
import { sensorStore } from "@/stores/sensorStore";
import { userStore } from "@/stores/userStore";
import { gardenStore } from "@/stores/gardenStore";
import type { Company } from "@/types/company";
import type { Garden } from "@/types/garden";
import { storeToRefs } from "pinia";
import { ref, type Ref, watch } from "vue";
import { useRouter, type Router } from "vue-router";

const router: Router = useRouter();
const alert: Ref<boolean> = ref(false);

let companies: Ref<Company[]> = storeToRefs(companyStore()).getCompanies;
let gardens: Ref<Garden[]> = ref<Garden[]>([]);

let selectedCompany: Ref<number | undefined> = ref<number>();
let selectedGarden: Ref<number | undefined> = ref<number>();

const storeCompanyId: Ref<number | undefined> = storeToRefs(
  companyStore()
).getSelectedCompany;
const storeGardenId: Ref<number | undefined> = storeToRefs(
  gardenStore()
).getSelectedGarden;

async function logoutUser(): Promise<void> {
  if (await logout()) {
    userStore().disposeStore();
    companyStore().disposeStore();
    gardenStore().disposeStore();
    sensorStore().disposeStore();
    router.push({ name: "login" });
  }
}

watch(selectedCompany, async (newSelectedCompany, oldSelectedCompany) => {
  if (storeCompanyId.value && newSelectedCompany != oldSelectedCompany) {
    gardens.value = await gardenStore().loadGardens(newSelectedCompany);

    if (gardens.value[0]) {
      selectedGarden.value = gardens.value[0].id;
    }
  }
});

async function openAdministration(): Promise<void> {
  if (!storeCompanyId.value && !storeGardenId.value) return;

  if (storeGardenId.value) {
    selectedGarden.value = storeGardenId.value;
    if (storeCompanyId.value) {
      gardens.value = await gardenStore().loadGardens(storeCompanyId.value);
    } else {
      gardens.value = await gardenStore().loadUserGardens();
      if (gardens.value[0]) {
        selectedGarden.value = gardens.value[0].id;
      }
    }
  }

  selectedCompany.value = storeCompanyId.value;
  alert.value = true;
}

async function setCompanyAndGarden(): Promise<void> {
  if (selectedCompany.value) {
    companyStore().setSelectedCompany(selectedCompany.value);
  }

  if (selectedGarden.value) {
    gardenStore().setSelectedGarden(selectedGarden.value);
    if (selectedCompany.value) {
      gardenStore().loadDataFromApi(selectedCompany.value);
    }
  }
}
</script>
