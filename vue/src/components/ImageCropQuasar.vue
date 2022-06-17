<template>
  <div class="inline-flex space-x-3 pl-2 items-center">
    <div class="q-pa-md">
      <div class="q-gutter-y-md column" style="max-width: 300px">
        <q-file
          clearable
          filled
          v-model="model"
          label="Image upload"
          accept=".jpg, image/*"
          @rejected="onRejected"
          @clear="clearImg"
          @update:model-value="setBase64($event)"
        />
      </div>
    </div>
    <div v-if="base64">
      <q-btn rounded color="primary" label="Crop Image" @click="crop" />
    </div>
    <div v-if="base64Cropped">
      <q-btn rounded color="primary" label="Place Image" @click="place" />
    </div>
  </div>

  <div class="grid grid-cols-2 p-6 gap-4">
    <div v-if="base64" class="card bg-white">
      <div class="card-body">
        <cropper ref="cropperChild" class="cropper" :src="base64" />
      </div>
    </div>
    <div v-if="base64Cropped" class="card bg-white">
      <div class="card-body">
        <img :src="base64Cropped" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Cropper } from "vue-advanced-cropper";
import "vue-advanced-cropper/dist/style.css";
import { useRouter } from "vue-router";
import { useQuasar } from "quasar";
import { ref } from "vue";

const router = useRouter();
const $q = useQuasar();

//https://stackoverflow.com/questions/65002098/how-to-define-type-for-refbinding-on-template-in-vue3-using-typescript
const cropperChild = ref<InstanceType<typeof Cropper>>();

const model = ref<File>();
const base64 = ref<string>();
const base64Cropped = ref<string>();

function crop() {
  base64Cropped.value = cropperChild.value
    ?.getResult()
    .canvas?.toDataURL("image/png") as string;
}

function place() {
  if (base64Cropped.value && base64Cropped.value.length > 0) {
    router.push({ name: "imageupload", params: { src: base64Cropped.value } });
  }
}

function clearImg() {
  base64.value = null;
  base64Cropped.value = null;
}

function onRejected() {
  $q.notify({
    type: "negative",
    message: "Wrong file type!",
  });
}

function setBase64(file: File) {
  if (!file) return;

  var reader = new FileReader();
  reader.readAsDataURL(file);

  reader.onload = (event: ProgressEvent<FileReader>) => {
    base64.value = event.target?.result as string;
  };

  reader.onerror = (error: ProgressEvent<FileReader>) => {
    console.log("Error: ", error);
  };
}
</script>
