<template>
  <div
    class="w-28 fixed h-full bg-background shadow-2 flex-none"
    style="min-height: 535px"
  >
    <div class="text-center">
      <router-link :to="'/dashboard'">
        <img src="@/assets/img/logo_small_white.svg" class="p-6 pb-9" />
      </router-link>
    </div>
    <ul>
      <router-link to="/dashboard" custom v-slot="{ href, navigate, isActive }">
        <li class="text-center hover">
          <a
            class="block py-7"
            v-bind:class="{ active: isActive }"
            :href="href"
            @click="navigate"
          >
            <svg
              v-bind:class="{ 'active-svg': isActive }"
              class="fill-primary mx-auto mb-2"
              xmlns="http://www.w3.org/2000/svg"
              width="27.349"
              height="27"
              viewBox="0 0 27.349 27"
            >
              <g id="home" transform="translate(0.675 0.5)">
                <path
                  id="Shape"
                  d="M16.262,26a.762.762,0,0,1-.761-.761v-6.12a1.279,1.279,0,0,0-1.278-1.278H11.775A1.279,1.279,0,0,0,10.5,19.119v6.12A.762.762,0,0,1,9.735,26H5.585a2.8,2.8,0,0,1-2.8-2.8v-7.8H2.361a.675.675,0,0,1-.074,0A2.392,2.392,0,0,1,.695,11.312L.705,11.3,11.306.7a2.394,2.394,0,0,1,3.386,0L25.3,11.307l0,0a2.394,2.394,0,0,1-1.694,4.085h-.392v7.8a2.8,2.8,0,0,1-2.8,2.8Z"
                  stroke-miterlimit="10"
                  stroke-width="1"
                />
              </g>
            </svg>
            Dashboard
          </a>
        </li>
      </router-link>
      <router-link to="/crops" custom v-slot="{ href, navigate, isActive }">
        <li class="text-center hover">
          <a
            class="block py-7"
            v-bind:class="{ active: isActive }"
            :href="href"
            @click="navigate"
          >
            <svg
              v-bind:class="{ 'active-svg': isActive }"
              class="fill-primary mx-auto mb-2"
              xmlns="http://www.w3.org/2000/svg"
              width="19.396"
              height="34.92"
              viewBox="0 0 19.396 34.92"
            >
              <path
                id="Pfad_362"
                data-name="Pfad 362"
                d="M105.976,48.456c-3.118,3.956-4.965,10.564-5.186,9.822-1.765-5.879-1.544-11.658,3.187-15.735,4.926-4.247,13.295-8.777,15.051-6.98.778.791-1.894,7.928-2.245,12.177a42.251,42.251,0,0,1-1.531,9.982c-1.255,3.854-3.948,6.2-9.822,4.424-.254-.077-1.572,8.964-3.574,7.835-.4-.144-1.63-.645,1.187-8.816a47.784,47.784,0,0,1,4.3-9.76c2.886-4.885,7.07-7.465,6.539-9.048C113.041,39.843,108.582,45.151,105.976,48.456Z"
                transform="translate(-99.773 -35.159)"
                fill-rule="evenodd"
              />
            </svg>
            Crops
          </a>
        </li>
      </router-link>
      <router-link to="/3d" custom v-slot="{ href, navigate, isActive }">
        <li class="text-center hover">
          <a
            class="block py-7"
            v-bind:class="{ active: isActive }"
            :href="href"
            @click="navigate"
          >
            <svg
              v-bind:class="{ 'active-svg': isActive }"
              class="fill-primary mx-auto mb-2"
              xmlns="http://www.w3.org/2000/svg"
              width="30.377"
              height="31.432"
              viewBox="0 0 30.377 31.432"
            >
              <g
                id="Gruppe_143"
                data-name="Gruppe 143"
                transform="translate(-53.469 -373.116)"
              >
                <path
                  id="Pfad_148"
                  data-name="Pfad 148"
                  d="M4.838,0H1.026A.953.953,0,0,0,.073.953V4.829a.953.953,0,1,0,1.906,0V1.906H4.838A.953.953,0,1,0,4.838,0Z"
                  transform="translate(53.396 373.116)"
                />
                <path
                  id="Pfad_149"
                  data-name="Pfad 149"
                  d="M426.718,0h-3.812a.953.953,0,1,0,0,1.906h2.859V4.829a.953.953,0,0,0,1.906,0V.953A.953.953,0,0,0,426.718,0Z"
                  transform="translate(-343.826 373.116)"
                />
                <path
                  id="Pfad_150"
                  data-name="Pfad 150"
                  d="M4.837,424.757H1.978v-2.923a.953.953,0,1,0-1.906,0v3.876a.953.953,0,0,0,.953.953H4.837a.953.953,0,1,0,0-1.906Z"
                  transform="translate(53.397 -22.124)"
                />
                <path
                  id="Pfad_151"
                  data-name="Pfad 151"
                  d="M426.718,420.881a.953.953,0,0,0-.953.953v2.923h-2.859a.953.953,0,1,0,0,1.906h3.812a.953.953,0,0,0,.953-.953v-3.876A.953.953,0,0,0,426.718,420.881Z"
                  transform="translate(-343.826 -22.124)"
                />
                <path
                  id="Pfad_152"
                  data-name="Pfad 152"
                  d="M57.928,7.553,45.66.125a.848.848,0,0,0-.883,0L32.5,7.553a.932.932,0,0,0-.439.8s0,0,0,.005V23.083a.931.931,0,0,0,.448.8l12.265,7.423a.848.848,0,0,0,.883,0l12.26-7.423.006,0a.881.881,0,0,0,.442-.787s0-.007,0-.011V8.354s0,0,0-.005A.931.931,0,0,0,57.928,7.553ZM44.337,28.914l-9.624-5.827,7.419-4.446a.943.943,0,0,0,.326-1.257.861.861,0,0,0-1.2-.341l-7.431,4.45V9.94l10.512,6.309Zm.881-14.26L34.712,8.346,45.218,1.985,55.724,8.346Zm11.394,6.839-7.432-4.45a.861.861,0,0,0-1.2.341.943.943,0,0,0,.326,1.257l7.419,4.446L46.1,28.914V16.249L56.612,9.94V21.494Z"
                  transform="translate(23.439 373.116)"
                />
              </g>
            </svg>
            3D
          </a>
        </li>
      </router-link>
    </ul>
  </div>
</template>
<script setup lang="ts">
import { useRoute } from "vue-router";

const route = useRoute();
</script>

<style lang="scss">
.active {
  background-color: $primary;
  color: white;
}

.active-svg {
  fill: white !important;
}

.hover:hover {
  background-color: rgba($primary, 0.1);
}
</style>
