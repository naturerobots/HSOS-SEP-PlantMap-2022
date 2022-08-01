<template>
  <div class="scene">
    <div id="three-scene-canvas"></div>
  </div>
</template>

<script setup lang="ts">
import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";
import { onMounted } from "vue";

console.log("THREE", THREE);
console.log("OrbitControls", OrbitControls);

const size = {
  width: 300, // window.innerWidth
  height: 300, // window.innerHeight
};

var renderer: THREE.WebGLRenderer;
var camera: THREE.PerspectiveCamera;
var scene: THREE.Scene;
var mesh: THREE.Mesh;

onMounted(() => {
  var canvasScene: Element | null = document.querySelector(
    "#three-scene-canvas"
  );

  renderer = new THREE.WebGLRenderer();

  camera = new THREE.PerspectiveCamera(70, size.width / size.height, 0.01, 10);
  camera.position.z = 1;

  var controls: OrbitControls = new OrbitControls(camera, renderer.domElement);
  controls.enableZoom = false;

  scene = new THREE.Scene();

  var geometry: THREE.BoxGeometry = new THREE.BoxGeometry(0.2, 0.2, 0.2);
  var material: THREE.MeshNormalMaterial = new THREE.MeshNormalMaterial();

  mesh = new THREE.Mesh(geometry, material);
  scene.add(mesh);

  renderer.setSize(size.width, size.height);
  renderer.setAnimationLoop(animationCallback);
  canvasScene?.appendChild(renderer.domElement);
});

let animationCallback = (time: number): void => {
  mesh.rotation.x = time / 2000;
  mesh.rotation.y = time / 1000;
  renderer.render(scene, camera);
};
</script>
