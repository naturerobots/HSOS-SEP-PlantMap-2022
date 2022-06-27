<template>
  <div class="flex h-full" style="flex-wrap: nowrap">
    <div class="order-none w-28" style="min-width: 7rem">
      <sidebar></sidebar>
    </div>
    <div class="grow order-1">
      <div class="flex flex-col h-full" style="flex-wrap: nowrap">
        <header-bar
          :title="title"
          :widgetOptions="widgetOptions"
          :storeOptions="storeOptions"
        ></header-bar>
        <div class="grow">
          <slot></slot>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Sidebar from "@/components/SidebarMenuQuasar.vue";
import HeaderBar from "@/components/header/HeaderBar.vue";
import type { StoreOption, WidgetOption } from "@/types/widgetOption";
defineProps<{
  widgetOptions?: WidgetOption[];
  storeOptions?: StoreOption[];
  title: string;
}>();
</script>
