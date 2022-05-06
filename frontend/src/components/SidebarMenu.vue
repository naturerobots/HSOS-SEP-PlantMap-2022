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
              <li class="my-8 text-center text-sm text-white">
                <router-link to="/dashboard">
                  <img
                    src="@/assets/icons/dashboard.svg"
                    class="w-6 h-6 mx-auto mb-1"
                  />
                  <p>Dashboard</p>
                </router-link>
              </li>
              <li class="my-8 text-center text-sm text-white">
                <router-link to="/crops">
                  <img
                    src="@/assets/icons/crops.svg"
                    class="w-6 h-6 mx-auto mb-1"
                  />
                  <p>Crops</p>                  
                </router-link>
              </li>
              <li class="my-8 text-center text-sm text-white">
                <router-link to="/3d">
                  <img
                    src="@/assets/icons/3d.svg"
                    class="w-6 h-6 mx-auto mb-1"
                  />
                  <p>3D</p>                  
                </router-link>
              </li>
            </ul>
          </div>
        </div>
        <!-- if the navbar has more items later, the profile item can be added to it-->
        <div class="mb-10">
          <router-link to="/profile">
            <img src="@/assets/icons/user.svg" class="w-6 h-6 mx-auto" />
          </router-link>
        </div>
      </nav>
    </div>
  </div>
</template>

<script setup lang="ts"></script>
