<template>
  <div class="scene">
    <div id="three-scene-canvas"></div>

    <div id="info-card">
      <div id="info-detail">
        <div class="hole"></div>
        <div class="description">test</div>
      </div>
    </div>
  </div>
</template>

<style>
.description {
  z-index: 100;
  margin-top: 20px;
  margin-left: 240px;
  width: 100%;
  height: 100%;
}
.hole {
  position: absolute;
  top: 20px;
  left: 20px;
  width: 200px;
  height: 160px;
  box-shadow: 0 0 0 9999px rgba(255, 255, 255, 1);
  border-radius: 8px;
}
.scene {
  position: relative;
}
#info-detail {
  overflow: hidden;
  position: relative;
  margin-left: 20%;
  width: 400px;
  height: 200px;
  /*background-color: red;*/
  border-radius: 16px;
  box-shadow: 0px 0px 150px -50px rgba(0, 0, 0, 0.5);
}

#info-card {
  pointer-events: none;
  position: absolute; /* let us position them inside the container */
  left: 0; /* make their default position the top left of the container */
  top: 0;
  cursor: pointer; /* change the cursor to a hand when over us */
  font-size: large;
  user-select: none; /* don't let the text get selected */
  text-shadow:         /* create a black outline */ -1px -1px 0 #000,
    0 -1px 0 #000, 1px -1px 0 #000, 1px 0 0 #000, 1px 1px 0 #000, 0 1px 0 #000,
    -1px 1px 0 #000, -1px 0 0 #000;
}
</style>

<script setup lang="ts">
import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";
//import { PLYLoader } from "three/examples/jsm/loaders/PLYLoader.js";
//import { CustomPLYLoader } from "@/components/three-scenes/CustomPlyLoader.js";
import { CustomPLYLoader } from "./CustomPlyLoader.ts";
import { onMounted, computed } from "vue";
import axios from "axios";

// 'http://localhost:8000/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/0bf37a0851b7402d88674e153f58e6f8.ply'
// https://pointly.medium.com/how-to-convert-ply-files-to-las-laz-d4100ef3625a
// https://gis.stackexchange.com/questions/314732/converting-ply-files-to-las-for-arcgis-input
// https://pdal.io/apps/translate.html

// The InfoCard is realized like shown in this tutorial
// https://r105.threejsfundamentals.org/threejs/lessons/threejs-align-html-elements-to-3d.html

//console.log("THREE", THREE);
//console.log("OrbitControls", OrbitControls);

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

var loader: CustomPLYLoader;

var infoCardCube: THREE.Mesh;
const tempV = new THREE.Vector3();

var highlightedPlant = null;

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

  var geometry: THREE.BoxGeometry = new THREE.BoxGeometry(0, 0, 0);
  var material: THREE.MeshNormalMaterial = new THREE.MeshNormalMaterial();

  infoCardCube = new THREE.Mesh(geometry, material);
  scene.add(infoCardCube);

  loader = new CustomPLYLoader();

  loader.setPropertyNameMapping({
    r: "red",
    g: "green",
    b: "blue",
  });

  let token =
    "5726934a783cfffa69dc7664dccd9a10c6028408c7b39eea50524804beac31d0";
  let url = "http://localhost:8000/companies/1/gardens/1/beds/1/3d-scene/";

  axios.defaults.baseURL = "http://localhost:8000/";
  axios.defaults.headers.common = { Authorization: `Token ` + token };

  axios
    .post(url)
    .then(function (response) {
      //console.log("then", response);

      // load Plant Ply files
      let plants = response["data"]["plants"];
      loadPlants(plants);

      // Set Camera position
      highlightedPlant = plants[1];
      setCameraToPlant(highlightedPlant);
    })
    .catch(function (error) {
      console.log("catch", error);
    });

  //var geometry: THREE.BoxGeometry = new THREE.BoxGeometry(0.2, 0.2, 0.2);
  //var material: THREE.MeshNormalMaterial = new THREE.MeshNormalMaterial();

  //var mesh = new THREE.Mesh(geometry, material);
  //scene.add(mesh);

  renderer.setSize(size.width, size.height);
  renderer.setAnimationLoop(animationCallback);
  canvasScene?.appendChild(renderer.domElement);

  // set backgroud color white
  renderer.setClearColor(0xffffff, 1);
});

let animationCallback = (time: number): void => {
  updateInfoCard();
  controls.update();
  renderer.render(scene, camera);
};

let setCameraToPlant = (plant): void => {
  let location = plant["location3d"];

  let x = parseFloat(location["x"]);
  let y = parseFloat(location["y"]);
  let z = parseFloat(location["z"]);

  controls.target.set(x, y, z);
  camera.position.set(x, -1, 0);
  camera.lookAt(new THREE.Vector3(x, y, z));
  controls.update();

  infoCardCube.position.set(x, y, z);

  updateInfoCard();
};

let updateInfoCard = (): void => {
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
    //const x2 = (tempV.x *  .5 + .5) * renderer.domElement.clientWidth;
    //const y2 = (tempV.y * -.5 + .5) * renderer.domElement.clientHeight;
    const x2 = (tempV.x * 0.5 + 0.5) * renderer.domElement.clientWidth;
    const y2 = (tempV.y * -0.5 + 0.5) * renderer.domElement.clientHeight;

    // move the elem to that position
    //elem.style.transform = `translate(-50%, -50%) translate(${x2}px,${y2}px)`;
    var infoCard: Element | null = document.querySelector("#info-card");
    if (infoCard != null) {
      infoCard.style.transform = `translate(-50%, -50%) translate(${x2}px,${y2}px)`;
    }
  }
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
