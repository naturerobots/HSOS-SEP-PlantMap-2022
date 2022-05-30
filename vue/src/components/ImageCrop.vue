<template>
  <input
    class="form-control"
    type="file"
    accept="image/*"
    @change="loadImage($event)"
  />

  <hr class="my-5" />

  <div v-if="uploaded && uploadedSrc.length > 0" style="width: 20%">
    <button @click="rotate" class="btn btn-primary">Rotate</button>
    <button @click="crop" class="btn btn-primary">Crop</button>

    <hr class="my-5" />

    <cropper
      ref="cropperChild"
      class="cropper"
      :src="uploadedSrc"
      :style="{
        width: uploaded.width + 'px',
        heigth: uploaded.height + 'px',
      }"
    />

    <hr class="my-5" />

    <img :src="cropped?.src" />
  </div>
</template>

<script setup lang="ts">
import { Cropper } from "vue-advanced-cropper";
import "vue-advanced-cropper/dist/style.css";

import { computed, ref } from "vue";

let uploaded = ref<HTMLImageElement>(new Image());
let cropped = ref<HTMLImageElement>();

//https://stackoverflow.com/questions/65002098/how-to-define-type-for-refbinding-on-template-in-vue3-using-typescript
const cropperChild = ref<InstanceType<typeof Cropper>>();

const uploadedSrc = computed<string>({
  get: () => uploaded.value?.src || "",
  set: (src: string) => {
    if (src.length == 0) return;

    let newImage = new Image();
    newImage.src = src;
    uploaded.value = newImage;
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
  cropped.value = newImage;
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
    uploadedSrc.value = event.target?.result as string;
  };
}
</script>
