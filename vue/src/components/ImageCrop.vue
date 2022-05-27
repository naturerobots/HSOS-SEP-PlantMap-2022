<template>
  <input
    class="form-control"
    type="file"
    accept="image/*"
    @change="loadImage($event)"
  />

  <hr class="my-5" />

  <div v-if="uploaded.image.src.length != 0" style="width: 20%">
    <button @click="rotate" class="btn btn-primary">Rotate</button>
    <button @click="crop" class="btn btn-primary">Crop</button>

    <hr class="my-5" />

    <cropper
      ref="cropperChild"
      class="cropper"
      :src="imgSource"
      @change="change"
      :style="{
        width: uploaded.image.width + 'px',
        heigth: uploaded.image.height + 'px',
      }"
    />

    <hr class="my-5" />

    <img :src="cropped.image.src" />
  </div>
</template>

<script setup lang="ts">
import { Cropper, type Coordinates } from "vue-advanced-cropper";
import "vue-advanced-cropper/dist/style.css";

import { reactive, computed, ref } from "vue";

const uploaded = reactive({ image: new Image() });
const cropped = reactive({ image: new Image() });

//https://stackoverflow.com/questions/65002098/how-to-define-type-for-refbinding-on-template-in-vue3-using-typescript
const cropperChild = ref<InstanceType<typeof Cropper>>();

const imgSource = computed<string>({
  get: () => uploaded.image.src,
  set: (src: string) => {
    let newImage = new Image();
    newImage.src = src;
    uploaded.image = newImage;
  },
});

function rotate() {
  cropperChild.value?.rotate(90);
}

function crop() {
  let newImage = new Image();
  newImage.src = cropperChild.value
    ?.getResult()
    .canvas?.toDataURL("image/png") as string;
  cropped.image = newImage;
}

function loadImage(event: Event) {
  if (!event || !event.target) {
    return;
  }

  let file = event.target as HTMLInputElement;

  if (!file.files || file.files.length === 0) {
    return;
  }

  var reader = new FileReader();

  reader.readAsDataURL(file.files[0]);

  reader.onload = (event) => {
    imgSource.value = event.target?.result as string;
  };
}

function change(coordinates: Coordinates) {
  console.log("---");
  console.log(coordinates);
  console.log("---");
}
</script>

<style></style>
