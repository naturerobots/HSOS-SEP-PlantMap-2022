<template>
  <div class="scene">
    <div id="three-scene-canvas"></div>
  </div>
</template>

<script setup lang="ts">
import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";
//import { PLYLoader } from "three/examples/jsm/loaders/PLYLoader.js";
//import { CustomPLYLoader } from "@/components/three-scenes/CustomPlyLoader.js";
import { CustomPLYLoader } from "./CustomPlyLoader.ts";
import { onMounted } from "vue";
import axios from "axios";

// 'http://localhost:8000/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/0bf37a0851b7402d88674e153f58e6f8.ply'
// https://pointly.medium.com/how-to-convert-ply-files-to-las-laz-d4100ef3625a
// https://gis.stackexchange.com/questions/314732/converting-ply-files-to-las-for-arcgis-input
// https://pdal.io/apps/translate.html

console.log("THREE", THREE);
console.log("OrbitControls", OrbitControls);

const size = {
  // width: 300, // window.innerWidth
  // height: 300, // window.innerHeight
  width: window.innerWidth - 200,
  height: window.innerHeight - 200,
};

var renderer: THREE.WebGLRenderer;
var camera: THREE.PerspectiveCamera;
var scene: THREE.Scene;
var controls: OrbitControls;

var loader = new CustomPLYLoader();

onMounted(() => {
  var canvasScene: Element | null = document.querySelector(
    "#three-scene-canvas"
  );

  // https://r105.threejsfundamentals.org/threejs/lessons/threejs-align-html-elements-to-3d.html

  renderer = new THREE.WebGLRenderer();

  camera = new THREE.PerspectiveCamera(75, size.width / size.height, 0.01, 10);

  controls = new OrbitControls(camera, renderer.domElement);

  scene = new THREE.Scene();

  // add spotlight for the shadows
  var spotLight = new THREE.SpotLight(0xffffff);
  spotLight.position.set(20, 20, 20);
  scene.add(spotLight);

  loader.setPropertyNameMapping({
    r: "red",
    g: "green",
    b: "blue",
  });

  let token =
    "0d59c8f03059643e894d8f54c3d1665f56edb7786cafa38494b1132f23d00a80";
  let url = "http://localhost:8000/companies/1/gardens/1/beds/1/3d-scene/";

  axios.defaults.baseURL = "http://localhost:8000/";
  axios.defaults.headers.common = { Authorization: `Token ` + token };

  axios
    .post(url)
    .then(function (response) {
      console.log("then", response);

      // load Plant Ply files
      let plants = response["data"]["plants"];
      loadPlants(plants);

      // Set Camera position
      let plant = plants[1];
      setCameraToPlant(plant);
    })
    .catch(function (error) {
      console.log("catch", error);
    });

  var geometry: THREE.BoxGeometry = new THREE.BoxGeometry(0.2, 0.2, 0.2);
  var material: THREE.MeshNormalMaterial = new THREE.MeshNormalMaterial();

  var mesh = new THREE.Mesh(geometry, material);
  //scene.add(mesh);

  renderer.setSize(size.width, size.height);
  renderer.setAnimationLoop(animationCallback);
  canvasScene?.appendChild(renderer.domElement);

  // set backgroud color white
  renderer.setClearColor(0xffffff, 1);
});

let animationCallback = (time: number): void => {
  controls.update();
  renderer.render(scene, camera);
};

let setCameraToPlant = (plant): void => {
  let location = plant["location"];

  let x = parseFloat(location["x"]);
  let y = parseFloat(location["y"]);
  let z = parseFloat(location["z"]);

  controls.target.set(x, y, z);
  camera.position.set(x, -1, 0);
  camera.lookAt(new THREE.Vector3(x, y, z));
  controls.update();
};

let loadPlants = (plants): void => {
  plants.forEach((plant) => {
    let url = plant["url"];
    loadPly(url);
  });
};

let loadPly = (url): void => {
  loader.load(url, function (geometry: any) {
    //geometry.computeVertexNormals();

    console.log("geometry", geometry);

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
