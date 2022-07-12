<template>
  <div class="scene">
    <div id="three-scene-canvas"></div>
  </div>
</template>

<script setup lang="ts">
import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";
import { PLYLoader } from "three/examples/jsm/loaders/PLYLoader.js";
import { onMounted } from "vue";

// 'http://localhost:8000/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/0bf37a0851b7402d88674e153f58e6f8.ply'

console.log("THREE", THREE);
console.log("OrbitControls", OrbitControls);

const size = {
  width: 300, // window.innerWidth
  height: 300, // window.innerHeight
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

  var loader = new PLYLoader();
  //var group = new THREE.Object3D();
  // let path = __dirname + 'models/car.ply';
  // let path = __dirname + 'car.ply';
  // let path = 'car.ply';

  var gardenId = "e1ef73b1258b475a996d2b72924c27ac";

  var server = "http://localhost:8000";

  var plys = [
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/0bf37a0851b7402d88674e153f58e6f8.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/0d927fa6b3534f9580d1db73d483b254.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/0eb265aaeeba46afa8e6c6a0d55620c1.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/1c216ceec7b3479cbf9a9bab5cb22eac.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/4d52f34f5873493dbe6a8d0544731e51.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/9e0639672f0944e7a8bf52d0ff7e0465.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/32c842075a0f41f3afb54d1eba840328.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/42bf69e416754deba45cc3e6707de975.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/42f443fbbe6e4f18abf505a45f1f5c59.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/56ba6c3ae8334789934fcf9712f3d1d5.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/59b9dc7c1cd346a48f5d5c607c974861.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/75c64b23a0e241a09068ce54bbd72378.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/941b9dec6a834536a87f18f082b0613e.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/3909e0e7abc7460a8176e8bc80af96df.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/5162fef543f24b1b822533e5588bb8b9.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/06694a57e7cf4ee1acce970ab9d9d67a.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/a9ba6215acc14825984f4e51b2f1e50a.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/a671dab73f9844b280ac4d36f0314ad5.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/afbe633eee354131b4979e9ba8b66a78.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/b57e00b276394d2b8b4ebf528cbc8465.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/bfd43b9c75394a68ae6dfdcdaf033eb7.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/c830142e228048c28f52164d43866f26.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/ce7d48e970d64d14a79752b394a2530e.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/d2dadb3c9920461ea06694bbcda9ed03.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/d32462d274d14b558a005e68fa4baf51.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/e46c7de24fce437eaa2112c57139d619.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/e79b844a5f9e429ea84e1a9f5a700d40.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/f2c61a5a0ba3479bb4ed5470dd56e3b4.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/f5b4f99c5c1b4eafb901edfefabacce5.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/f28e06e81e174ecdb5f2ff1164b02180.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/f3817e815d074f67b44ce4b26f890a24.ply",
    server +
      "/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/f892521817554bf7a500e495b395e9ec.ply",
  ];

  plys.forEach((ply) => {
    //let path = 'http://localhost:8000/media/pointclouds/ply/e1ef73b1258b475a996d2b72924c27ac/0bf37a0851b7402d88674e153f58e6f8.ply';
    loader.load(ply, function (geometry) {
      geometry.computeVertexNormals();

      //var material = new THREE.MeshNormalMaterial({
      //    flatShading: true
      //});

      var material = new THREE.PointsMaterial({
        size: 10,
        sizeAttenuation: false,
      });

      var mesh = new THREE.Mesh(geometry, material);
      scene.add(mesh);
    });
  });

  var geometry: THREE.BoxGeometry = new THREE.BoxGeometry(0.2, 0.2, 0.2);
  var material: THREE.MeshNormalMaterial = new THREE.MeshNormalMaterial();

  var mesh = new THREE.Mesh(geometry, material);
  scene.add(mesh);

  renderer.setSize(size.width, size.height);
  renderer.setAnimationLoop(animationCallback);
  canvasScene?.appendChild(renderer.domElement);
});

let animationCallback = (time: number): void => {
  //mesh.rotation.x = time / 2000;
  //mesh.rotation.y = time / 1000;
  renderer.render(scene, camera);
};

/*
let generateSprite = (): THREE.Texture =>  {
    var canvas = document.createElement('canvas');
    //var canvas = this.canvas;
    canvas.width = 16;
    canvas.height = 16;

    var context = canvas.getContext('2d');
    var gradient = context?.createRadialGradient(canvas.width / 2, canvas.height / 2, 0, canvas.width / 2, canvas.height / 2, canvas.width / 2);
    gradient?.addColorStop(0, 'rgba(255,255,255,1)');
    gradient?.addColorStop(0.2, 'rgba(0,255,255,1)');
    gradient?.addColorStop(0.4, 'rgba(0,0,64,1)');
    gradient?.addColorStop(1, 'rgba(0,0,0,1)');

    context?.fillStyle = gradient;

    context?.fillRect(0, 0, canvas.width, canvas.height);

    var texture = new THREE.Texture(canvas);
    texture.needsUpdate = true;
    return texture;
};
*/
</script>
