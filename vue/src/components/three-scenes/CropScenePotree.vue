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

//import { Potree } from '@cognite/potree-core';

import Potree from "@cognite/potree-core";

//window.Potree = require('@cognite/potree-core');

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

  var server = "http://localhost:8000";
  var mediaPath = "/media/pointclouds/";
  var path = server + mediaPath + "ept/ept.json";
  //var path = server + mediaPath + "lion_takanawa/cloud.js";

  var points = new Potree.Group();
  points.setPointBudget(10000000);
  scene.add(points);

  console.log("points", points);

  Potree.loadPointCloud(path, "testPointCloud", function (data) {
    //console.log(Potree);
    console.log("data", data);
    var pointcloud = data.pointcloud;
    points.add(pointcloud);
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
