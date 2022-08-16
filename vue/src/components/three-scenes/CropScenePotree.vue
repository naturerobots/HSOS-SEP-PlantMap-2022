<template>
  <div class="scene">
    <div id="three-scene-canvas"></div>
  </div>
</template>

<script setup lang="ts">
import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";
import { onMounted } from "vue";

import { PointCloudOctree, Potree } from "potree-loader";

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

const potree = new Potree();
// Show at most 2 million points.
potree.pointBudget = 2_000_000;
// List of point clouds which we loaded and need to update.
const pointClouds: PointCloudOctree[] = [];

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

  // add spotlight for the shadows
  var spotLight = new THREE.SpotLight(0xffffff);
  spotLight.position.set(20, 20, 20);
  scene.add(spotLight);

  var server = "http://localhost:8000";
  var mediaPath = "/media/pointclouds/";
  var path = server + mediaPath + "las_converted/metadata.json";
  //var path = server + mediaPath + "ground_converted/metadata.json";

  potree
    .loadPointCloud(
      // The name of the point cloud which is to be loaded.
      "metadata.json",
      // Given the relative URL of a file, should return a full URL (e.g. signed).
      //relativeUrl => `${baseUrl}${relativeUrl}`,
      (relativeUrl) => path
    )
    .then((pco) => {
      console.log("pco", pco);
      pointClouds.push(pco);
      scene.add(pco); // Add the loaded point cloud to your ThreeJS scene.

      // The point cloud comes with a material which can be customized directly.
      // Here we just set the size of the points.
      pco.material.size = 1.0;
    });

  //potree.updatePointClouds(pointClouds, camera, renderer);

  var geometry: THREE.BoxGeometry = new THREE.BoxGeometry(0.2, 0.2, 0.2);
  var material: THREE.MeshNormalMaterial = new THREE.MeshNormalMaterial();

  var mesh = new THREE.Mesh(geometry, material);
  scene.add(mesh);

  renderer.setSize(size.width, size.height);
  //renderer.setAnimationLoop(animationCallback);
  renderer.setAnimationLoop(update);
  canvasScene?.appendChild(renderer.domElement);

  update();
  // set backgroud color red
  renderer.setClearColor(0xffffff, 1);
});

function update() {
  // This is where most of the potree magic happens. It updates the visiblily of the octree nodes
  // based on the camera frustum and it triggers any loads/unloads which are necessary to keep the
  // number of visible points in check.
  potree.updatePointClouds(pointClouds, camera, renderer);

  // Render your scene as normal
  renderer.clear();
  renderer.render(scene, camera);
}
</script>
