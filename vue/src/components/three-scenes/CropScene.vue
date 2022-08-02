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
//var mesh: THREE.Mesh;

onMounted(() => {
  var canvasScene: Element | null = document.querySelector(
    "#three-scene-canvas"
  );

  renderer = new THREE.WebGLRenderer();

  camera = new THREE.PerspectiveCamera(70, size.width / size.height, 0.01, 10);
  camera.position.z = 1;

  var controls: OrbitControls = new OrbitControls(camera, renderer.domElement);
  //controls.enableZoom = false;

  scene = new THREE.Scene();

  // position and point the camera to the center of the scene
  //camera.position.x = 10;
  //camera.position.y = 10;
  //camera.position.z = 10;
  camera.lookAt(new THREE.Vector3(0, 2, 0));

  // add spotlight for the shadows
  var spotLight = new THREE.SpotLight(0xffffff);
  spotLight.position.set(20, 20, 20);
  scene.add(spotLight);

  //var loader = new PLYLoader();

  var loader = new CustomPLYLoader();

  loader.setPropertyNameMapping({
    r: "red",
    g: "green",
    b: "blue",
  });

  var server = "http://localhost:8000";
  var mediaPath = "/media/pointclouds/ply/";
  var gardenId = "e1ef73b1258b475a996d2b72924c27ac/";
  var gardenPath = server + mediaPath + gardenId;

  var plys = [
    gardenPath + "0bf37a0851b7402d88674e153f58e6f8.ply",
    gardenPath + "0d927fa6b3534f9580d1db73d483b254.ply",
    gardenPath + "0eb265aaeeba46afa8e6c6a0d55620c1.ply",
    gardenPath + "1c216ceec7b3479cbf9a9bab5cb22eac.ply",
    gardenPath + "4d52f34f5873493dbe6a8d0544731e51.ply",
    gardenPath + "9e0639672f0944e7a8bf52d0ff7e0465.ply",
    gardenPath + "32c842075a0f41f3afb54d1eba840328.ply",
    gardenPath + "42bf69e416754deba45cc3e6707de975.ply",
    gardenPath + "42f443fbbe6e4f18abf505a45f1f5c59.ply",
    gardenPath + "56ba6c3ae8334789934fcf9712f3d1d5.ply",
    gardenPath + "59b9dc7c1cd346a48f5d5c607c974861.ply",
    gardenPath + "75c64b23a0e241a09068ce54bbd72378.ply",
    gardenPath + "941b9dec6a834536a87f18f082b0613e.ply",
    gardenPath + "3909e0e7abc7460a8176e8bc80af96df.ply",
    gardenPath + "5162fef543f24b1b822533e5588bb8b9.ply",
    gardenPath + "06694a57e7cf4ee1acce970ab9d9d67a.ply",
    gardenPath + "a9ba6215acc14825984f4e51b2f1e50a.ply",
    gardenPath + "a671dab73f9844b280ac4d36f0314ad5.ply",
    gardenPath + "afbe633eee354131b4979e9ba8b66a78.ply",
    gardenPath + "b57e00b276394d2b8b4ebf528cbc8465.ply",
    gardenPath + "bfd43b9c75394a68ae6dfdcdaf033eb7.ply",
    gardenPath + "c830142e228048c28f52164d43866f26.ply",
    gardenPath + "ce7d48e970d64d14a79752b394a2530e.ply",
    gardenPath + "d2dadb3c9920461ea06694bbcda9ed03.ply",
    gardenPath + "d32462d274d14b558a005e68fa4baf51.ply",
    gardenPath + "e46c7de24fce437eaa2112c57139d619.ply",
    gardenPath + "e79b844a5f9e429ea84e1a9f5a700d40.ply",
    gardenPath + "f2c61a5a0ba3479bb4ed5470dd56e3b4.ply",
    gardenPath + "f5b4f99c5c1b4eafb901edfefabacce5.ply",
    gardenPath + "f28e06e81e174ecdb5f2ff1164b02180.ply",
    gardenPath + "f3817e815d074f67b44ce4b26f890a24.ply",
    gardenPath + "f892521817554bf7a500e495b395e9ec.ply",
  ];

  plys = plys.slice(0, -1);

  let stats: any = {
    success: [],
    failed: [],
  };

  plys.forEach((ply) => {
    //let path = 'http://localhost:8000/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/0bf37a0851b7402d88674e153f58e6f8.ply';
    loader.load(ply, function (geometry: any) {
      //geometry.computeVertexNormals();

      console.log("geometry", geometry);

      let nanCollection = [];

      for (let i = 0; i < geometry.attributes.position.array.length; i++) {
        // check if array value is false or NaN
        if (Number.isNaN(geometry.attributes.position.array[i])) {
          nanCollection.push(i);
        }
      }

      if (nanCollection.length == 0) {
        var material = new THREE.PointsMaterial({
          size: 0.001,
          vertexColors: true,
        });

        var particleSystem = new THREE.Points(geometry, material);

        scene.add(particleSystem);

        stats.success.push({
          ply: ply,
        });
      } else {
        stats.failed.push({
          ply: ply,
          nanCollection: JSON.stringify(nanCollection),
        });
      }

      console.log(
        "success: " + JSON.stringify(stats.success.length),
        JSON.stringify(stats.success)
      );
      console.log(
        "failed: " + JSON.stringify(stats.failed.length),
        JSON.stringify(stats.failed)
      );
    });
  });

  var geometry: THREE.BoxGeometry = new THREE.BoxGeometry(0.2, 0.2, 0.2);
  var material: THREE.MeshNormalMaterial = new THREE.MeshNormalMaterial();

  var mesh = new THREE.Mesh(geometry, material);
  scene.add(mesh);

  renderer.setSize(size.width, size.height);
  renderer.setAnimationLoop(animationCallback);
  canvasScene?.appendChild(renderer.domElement);

  // set backgroud color red
  //renderer.setClearColor(0xffffff, 1);
});

let animationCallback = (time: number): void => {
  //mesh.rotation.x = time / 2000;
  //mesh.rotation.y = time / 1000;
  renderer.render(scene, camera);
};
</script>
