<template>
  <div class="px-6 py-3 border-b flex-none w-full">
    <div
      class="pl-3 py-3 h-16 flex items-center justify-between"
      style="flex-wrap: nowrap"
    >
      <div class="text-3xl text-black">
        <div>{{ title }}</div>
      </div>
      <div class="flex items-center" style="flex-wrap: nowrap">
        <!--TODO: Add Quasar components (Button, Avatar)-->
        <!--FIXME: Maybe add a type that contains widgetOptions and storeOptions, so that both must always be passed together -->
        <div v-if="widgetOptions && storeOptions" class="mr-3">
          <widget-comp
            :widgetOptions="widgetOptions"
            :storeOptions="storeOptions"
            label="widgets"
          ></widget-comp>
        </div>

        <div class="mr-3">
          <a href="#" class="block relative">
            <svg
              class="fill-primary"
              xmlns="http://www.w3.org/2000/svg"
              version="1.1"
              width="24"
              height="24"
              x="0"
              y="0"
              viewBox="0 0 24 24"
              style="enable-background: new 0 0 512 512"
            >
              <g>
                <g xmlns="http://www.w3.org/2000/svg">
                  <path
                    d="m21.379 16.913c-1.512-1.278-2.379-3.146-2.379-5.125v-2.788c0-3.519-2.614-6.432-6-6.92v-1.08c0-.553-.448-1-1-1s-1 .447-1 1v1.08c-3.387.488-6 3.401-6 6.92v2.788c0 1.979-.867 3.847-2.388 5.133-.389.333-.612.817-.612 1.329 0 .965.785 1.75 1.75 1.75h16.5c.965 0 1.75-.785 1.75-1.75 0-.512-.223-.996-.621-1.337z"
                    class=""
                  ></path>
                  <path
                    d="m12 24c1.811 0 3.326-1.291 3.674-3h-7.348c.348 1.709 1.863 3 3.674 3z"
                    class=""
                  ></path>
                </g>
              </g>
            </svg>
          </a>
        </div>
        <div>
          <profile-dropdown></profile-dropdown>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import WidgetComp from "@/components/header/widget/WidgetComp.vue";
import ProfileDropdown from "@/components/header/ProfileDropdown.vue";
import type { WidgetOption, StoreOption } from "@/types/widgetOption";

defineProps<{
  title: string;
  widgetOptions?: WidgetOption[];
  storeOptions?: StoreOption[];
}>();
</script>
