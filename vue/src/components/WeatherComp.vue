<template>
  <div class="card w-96 shadow-xl m-2">
    <div class="card-body p-5">
      <h2 class="text-xl text-center text-primary-focus">Wetter Ibbenbüren</h2>
      <div class="card card-side">
        <!-- <font-awesome-icon icon="fa-solid fa-cloud-hail-mixed" /> -->
        <figure>
          <img src="http://openweathermap.org/img/wn/10d@2x.png" />
        </figure>
        <div class="card-body">
          <h2 class="font-bold text-primary-focus">Montag, 21.05.2022</h2>
          <p class="mt-2 text-primary-focus text-2xl">3 / 6°C</p>
          <p class="mt-2 text-primary-focus">leichter Regen</p>
        </div>
      </div>
      <!-- <div class="grid grid-cols-5 mt-5">
        <div class="col-span-2">
          <figure>
          <img src="http://openweathermap.org/img/wn/10d@2x.png" />
        </figure>
        </div>
        <div class="col-span-3">
          <h2 class="font-bold text-primary-focus">Montag, 21.05.2022</h2>
          <p class="mt-2 text-primary-focus text-2xl">3 / 6°C</p>
          <p class="mt-2 text-primary-focus">leichter Regen</p>
        </div>
      </div> -->
      <div class="grid grid-cols-3 mt-5">
        <div class="text-center">
          <h2 class="font-bold text-primary-focus">Di. 22.05.</h2>
          <figure>
            <img src="http://openweathermap.org/img/wn/03d@2x.png" />
          </figure>
          <p class="weather-forecasts">4 / 8°C</p>
          <p class="weather-forecasts">wolkig</p>
        </div>
        <div class="text-center">
          <h2 class="font-bold text-primary-focus">Mi. 23.05.</h2>
          <figure>
            <img src="http://openweathermap.org/img/wn/10d@2x.png" />
          </figure>
          <p class="weather-forecasts">3 / 8°C</p>
          <p class="weather-forecasts">leicht bewölkt</p>
        </div>
        <div class="text-center">
          <h2 class="font-extrabold text-primary-focus">Do. 24.05.</h2>
          <figure>
            <img src="http://openweathermap.org/img/wn/10d@2x.png" />
          </figure>
          <p class="weather-forecasts">4 / 8°C</p>
          <p class="weather-forecasts">bedeckt</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts"></script>
