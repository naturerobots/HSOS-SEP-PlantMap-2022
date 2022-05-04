<template>
  <div class="sidebar">
    <div class="sidebar-content">
      <nav class="bg-primary sidebar-nav">
        <div class="mt-10 mb-10">
          <router-link :to="'/dashboard'">
            <img
              src="@/assets/img/logo_small_white.svg"
              class="w-10 h-10 mb-3 mx-auto"
            />
            <!-- ToDo: Create Image Component & custom class for this -->
          </router-link>
          <div class="mt-10">
            <ul>
              <!-- ToDo: Edit icons & links -->
              <li class="my-12 text-center">
                <router-link to="/dashboard"> 1 </router-link>
              </li>
              <li class="my-12 text-center">
                <router-link to="/crops"> 2 </router-link>
              </li>
              <li class="my-12 text-center">
                <router-link to="/3d"> 3 </router-link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  </div>
</template>

<script setup lang="ts"></script>
