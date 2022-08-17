<template>
  <div class="scene">
    <div id="three-scene-canvas"></div>

    <div v-if="showInfoCard" id="info-card">
      <div id="info-detail">
        <div class="hole"></div>
        <div class="description">
          <div class="heading">{{ highlightedCrop3d?.name }}</div>

          <table id="properties">
            <tr>
              <th class="table-entry">Location:</th>
              <th class="table-entry">
                {{ highlightedCrop3d?.locationDescription }}
              </th>
            </tr>
            <tr>
              <th class="table-entry">Type:</th>
              <th class="table-entry">{{ highlightedCrop3d?.type }}</th>
            </tr>
            <!-- <div>Health: {{ highlightedCrop3d.health }}</div> -->
            <tr>
              <th class="table-entry">Health:</th>
              <th class="table-entry">
                <span
                  v-for="health in highlightedCrop3d?.health"
                  :key="health.type"
                >
                  {{ health.shortcut }}
                </span>
              </th>
            </tr>
            <tr>
              <th class="table-entry">Yield:</th>
              <th class="table-entry">{{ highlightedCrop3d?.yield }}</th>
            </tr>
            <tr>
              <th class="table-entry">Status:</th>
              <th class="table-entry">{{ highlightedCrop3d?.status }}</th>
            </tr>
            <tr>
              <th class="table-entry">Harvest:</th>
              <th class="table-entry">{{ highlightedCrop3d?.harvest }}</th>
            </tr>
          </table>

          <!-- progress bar -->
          <div class="progress-bar">
            <div class="progress" :style="getProgressWidthStyle()"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.progress-bar {
  /*position: relative;*/
  margin-top: 5px;
  width: 100%;
  background-color: #9c9b9b;
  border-radius: 16px;
}

.progress-bar .progress {
  /*position: absolute;*/
  /* background-color: green; */
  /*width: 50%;*/
  background-color: #79b729;
  height: 15px;
  border-radius: 16px;
}

.heading {
  text-align: center;
  font-size: x-large;
  font-weight: bolder;
}

#properties {
  width: 100%;
}

#properties .table-entry {
  /* line-height: 1.5 */

  font-size: small;
  font-weight: lighter;
  width: 50%;
  text-align: left;
}

.description {
  padding-left: 50%;
}

.hole {
  z-index: -1;
  position: absolute;
  box-shadow: 0 0 0 9999px rgba(255, 255, 255, 1);
  border-radius: 8px;
  width: 40%;
  height: 80%;
}
.scene {
  position: relative;
}
#info-detail {
  overflow: hidden;
  position: relative;
  padding: 5%;
  margin-left: 25%;
  border-radius: 16px;
  box-shadow: 0px 0px 150px -50px rgba(0, 0, 0, 0.5);

  width: 600px;
  height: 250px;
}

#info-card {
  z-index: 0;
  pointer-events: none;

  position: absolute; /* let us position them inside the container */
  left: 0; /* make their default position the top left of the container */
  top: 0;
  cursor: pointer; /* change the cursor to a hand when over us */
  font-size: large;
  user-select: none; /* don't let the text get selected */
}
</style>

<script setup lang="ts">
import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";
import { CustomPLYLoader } from "./CustomPlyLoader.ts";
import { onMounted, ref, Ref, computed } from "vue";
import axios from "axios";

import type { Crop3dArray, Crop3d } from "@/types/crop3d";
import type { Position } from "@/types/position";

import { storeToRefs } from "pinia";

import { userStore } from "@/stores/userStore";

import { companyStore } from "@/stores/companyStore";
import { gardenStore } from "@/stores/gardenStore";
import { bedStore } from "@/stores/bedStore";
import { cropsStore } from "@/stores/cropsStore";

// https://stemkoski.github.io/Three.js/Mouse-Over.html

const size = {
  width: window.innerWidth - 200,
  height: window.innerHeight - 200,
};

var renderer: THREE.WebGLRenderer;
var camera: THREE.PerspectiveCamera;
var scene: THREE.Scene;
var controls: OrbitControls;
var loader: CustomPLYLoader;

var infoCardCube: THREE.Mesh;
var tempV: THREE.Vector3;
var crop3dArray: Crop3dArray;
var highlightedCrop3d = ref<Crop3d>();
var globalPosition: Position;

const baseURL = "http://127.0.0.1:8000";
const companyId: Ref<number | undefined> = storeToRefs(
  companyStore()
).getSelectedCompany;
const gardenId: Ref<number | undefined> = storeToRefs(
  gardenStore()
).getSelectedGarden;
const bedId: Ref<number | undefined> = storeToRefs(bedStore()).getSelectedBedId;
const plantId: Ref<string | undefined> = storeToRefs(
  cropsStore()
).getSelectedCropId;

/*
console.log("companyId", companyId);
console.log("gardenId", gardenId);
console.log("bedId", bedId);
console.log("plantId", plantId);
*/

const showInfoCard = computed(() => {
  return highlightedCrop3d.value != undefined ? true : false;
});

onMounted(() => {
  var canvasScene: Element | null = document.querySelector(
    "#three-scene-canvas"
  );

  renderer = new THREE.WebGLRenderer();
  camera = new THREE.PerspectiveCamera(75, size.width / size.height, 0.01, 10);
  controls = new OrbitControls(camera, renderer.domElement);
  scene = new THREE.Scene();

  var geometry: THREE.BoxGeometry = new THREE.BoxGeometry(0, 0, 0);
  var material: THREE.MeshNormalMaterial = new THREE.MeshNormalMaterial();
  infoCardCube = new THREE.Mesh(geometry, material);
  scene.add(infoCardCube);

  tempV = new THREE.Vector3();

  // add spotlight for the shadows
  var spotLight = new THREE.SpotLight(0xffffff);
  spotLight.position.set(20, 20, 20);
  scene.add(spotLight);

  loader = new CustomPLYLoader();

  loader.setPropertyNameMapping({
    r: "red",
    g: "green",
    b: "blue",
  });

  let url =
    baseURL +
    "/companies/" +
    companyId.value +
    "/gardens/" +
    gardenId.value +
    "/beds/" +
    bedId.value +
    "/3d-scene/";
  let payload = {};
  let header = {
    headers: {
      Authorization: "Token " + storeToRefs(userStore()).getToken.value.token,
    },
  };

  axios
    .post(url, payload, header)
    .then(function (response): void {
      console.log("then", response);

      crop3dArray = response["data"]["plants"];
      globalPosition = response["data"]["global"]["position"];
      loadPlants(crop3dArray);

      let resetToGloabal = true;
      if (plantId != undefined) {
        console.log("plantId", plantId.value);
        let crop3d: Crop3d | null = getCrop3dById(plantId.value);
        console.log("crop3d", crop3d);
        if (crop3d != undefined) {
          setInfoCard(crop3d);
          setCameraToPosition(crop3d.position);
          resetToGloabal = false;
        }
      }
      if (resetToGloabal) {
        resetInfoCard();
        setCameraToPosition(globalPosition);
      }
    })
    .catch(function (): undefined {
      return undefined;
    });

  renderer.setSize(size.width, size.height);
  renderer.setAnimationLoop(animationCallback);
  canvasScene?.appendChild(renderer.domElement);

  // set background color white
  renderer.setClearColor(0xffffff, 1);
});

// eather get the first crop3d with the given id or null
let getCrop3dById = (id: string): Crop3d | undefined => {
  //id = "a671dab73f9844b280ac4d36f0314ad5";
  let crops: Crop3dArray = crop3dArray.filter((element) => {
    console.log(
      "element.geometryUUID",
      element.measurementUUID,
      "id",
      id,
      "check",
      element.measurementUUID == id
    );
    //console.log("element.geometryUUID", element.geometryUUID, "element.name", element.name)
    console.log("element.name", element.name);
    return element.measurementUUID == id;
  });
  if (crops.length == 0) {
    return undefined;
  }
  return crops[0];
};

let setInfoCard = (crop: Crop3d): void => {
  highlightedCrop3d.value = crop;
};

let resetInfoCard = (): void => {
  highlightedCrop3d.value = undefined;
};

let getProgressWidthStyle = (): string => {
  var width = highlightedCrop3d.value?.progress;
  width = width * 100;
  var widthStyle = "width: " + width + "%";
  //console.log("widthStyle: "+widthStyle);
  return widthStyle;
};

let animationCallback = (time: number): void => {
  updateInfoCardPosition();
  controls.update();
  renderer.render(scene, camera);
};

let setCameraToPosition = (position: Position): void => {
  let x = parseFloat(position.x);
  let y = parseFloat(position.y);
  let z = parseFloat(position.z);

  controls.target.set(x, y, z);
  camera.position.set(x, -1, 0);
  camera.lookAt(new THREE.Vector3(x, y, z));
  controls.update();

  infoCardCube.position.set(x, y, z);

  updateInfoCardPosition();
};

let updateInfoCardPosition = (): void => {
  if (typeof infoCardCube != "undefined") {
    //console.log("renderer.domElement.position().left ", renderer.domElement);

    // get the position of the center of the cube
    infoCardCube.updateWorldMatrix(true, false);
    infoCardCube.getWorldPosition(tempV);

    // get the normalized screen coordinate of that position
    // x and y will be in the -1 to +1 range with x = -1 being
    // on the left and y = -1 being on the bottom
    tempV.project(camera);

    // convert the normalized position to CSS coordinates
    const x2 = (tempV.x * 0.5 + 0.5) * renderer.domElement.clientWidth;
    const y2 = (tempV.y * -0.5 + 0.5) * renderer.domElement.clientHeight;
    //const y2 = (tempV.y * 0.5 + 0.5) * renderer.domElement.clientHeight - 0.5;

    // move the elem to that position
    var infoCard: Element | null = document.querySelector("#info-card");
    if (infoCard != null) {
      infoCard.style.transform = `translate(-50%, -50%) translate(${x2}px,${y2}px)`;
    }
  }
};

let loadPlants = (plants: Crop3dArray): void => {
  plants.forEach((plant: Crop3d) => {
    let url = plant["url"];
    loadPly(url);
  });
};

let loadPly = (url: string): void => {
  loader.load(url, function (geometry: any) {
    //geometry.computeVertexNormals();

    //console.log("geometry", geometry);

    let nanCollection = [];

    for (let i = 0; i < geometry.attributes.position.array.length; i++) {
      // check if geometry array has false or NaN values
      if (Number.isNaN(geometry.attributes.position.array[i])) {
        nanCollection.push(i);
      }
    }

    if (nanCollection.length == 0) {
      var material = new THREE.PointsMaterial({
        size: 0.01,
        vertexColors: true,
      });

      var particleSystem = new THREE.Points(geometry, material);

      scene.add(particleSystem);
    }
  });
};
</script>
