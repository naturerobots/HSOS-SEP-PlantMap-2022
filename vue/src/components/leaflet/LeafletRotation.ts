import L from "leaflet";

//https://github.com/IvanSanchez/Leaflet.ImageOverlay.Rotated

L.ImageOverlay.Rotated = L.ImageOverlay.extend({
  initialize: function (image, topleft, topright, bottomleft, options) {
    if (typeof image === "string") {
      this._url = image;
    } else {
      // Assume that the first parameter is an instance of HTMLImage or HTMLCanvas
      this._rawImage = image;
    }

    this._topLeft = L.latLng(topleft);
    this._topRight = L.latLng(topright);
    this._bottomLeft = L.latLng(bottomleft);

    L.setOptions(this, options);
  },

  //TODO: Explicit Type?
  onAdd: function (map: any) {
    if (!this._image) {
      this._initImage();

      if (this.options.opacity < 1) {
        this._updateOpacity();
      }
    }

    if (this.options.interactive) {
      L.DomUtil.addClass(this._rawImage, "leaflet-interactive");
      this.addInteractiveTarget(this._rawImage);
    }

    map.on("zoomend resetview", this._reset, this);

    this.getPane().appendChild(this._image);
    this._reset();
  },

  //TODO: Explicit Types?
  onRemove: function (map) {
    map.off("zoomend resetview", this._reset, this);
    L.ImageOverlay.prototype.onRemove.call(this, map);
  },

  _initImage: function () {
    let img = this._rawImage;
    if (this._url) {
      img = L.DomUtil.create("img");
      img.style.display = "none"; // Hide while the first transform (zero or one frames) is being done

      if (this.options.crossOrigin) {
        img.crossOrigin = "";
      }

      img.src = this._url;
      this._rawImage = img;
    }
    L.DomUtil.addClass(img, "leaflet-image-layer");

    // this._image is reused by some of the methods of the parent class and
    // must keep the name, even if it is counter-intuitive.
    const div = (this._image = L.DomUtil.create(
      "div",
      "leaflet-image-layer " +
        (this._zoomAnimated ? "leaflet-zoom-animated" : "")
    ));

    this._updateZIndex(); // apply z-index style setting to the div (if defined)

    div.appendChild(img);

    div.onselectstart = L.Util.falseFn;
    div.onmousemove = L.Util.falseFn;

    img.onload = function () {
      this._reset();
      img.style.display = "block";
      this.fire("load");
    }.bind(this);

    img.alt = this.options.alt;
  },

  _reset: function () {
    const div = this._image;

    if (!this._map) {
      return;
    }

    // Project control points to container-pixel coordinates
    const pxTopLeft = this._map.latLngToLayerPoint(this._topLeft);
    const pxTopRight = this._map.latLngToLayerPoint(this._topRight);
    const pxBottomLeft = this._map.latLngToLayerPoint(this._bottomLeft);

    // Infer coordinate of bottom right
    const pxBottomRight = pxTopRight.subtract(pxTopLeft).add(pxBottomLeft);

    // pxBounds is mostly for positioning the <div> container
    const pxBounds = L.bounds([
      pxTopLeft,
      pxTopRight,
      pxBottomLeft,
      pxBottomRight,
    ]);

    const size = pxBounds.getSize();
    const pxTopLeftInDiv = pxTopLeft.subtract(pxBounds.min);

    // LatLngBounds are needed for (zoom) animations
    this._bounds = L.latLngBounds(
      this._map.layerPointToLatLng(pxBounds.min),
      this._map.layerPointToLatLng(pxBounds.max)
    );

    L.DomUtil.setPosition(div, pxBounds.min);

    div.style.width = size.x + "px";
    div.style.height = size.y + "px";

    const imgW = this._rawImage.width;
    const imgH = this._rawImage.height;
    if (!imgW || !imgH) {
      return; // Probably because the image hasn't loaded yet.
    }

    // Sides of the control-point box, in pixels
    // These are the main ingredient for the transformation matrix.
    const vectorX = pxTopRight.subtract(pxTopLeft);
    const vectorY = pxBottomLeft.subtract(pxTopLeft);

    this._rawImage.style.transformOrigin = "0 0";

    // The transformation is an affine matrix that switches
    // coordinates around in just the right way. This is the result
    // of calculating the skew/rotation/scale matrices and simplyfing
    // everything.
    this._rawImage.style.transform =
      "matrix(" +
      vectorX.x / imgW +
      ", " +
      vectorX.y / imgW +
      ", " +
      vectorY.x / imgH +
      ", " +
      vectorY.y / imgH +
      ", " +
      pxTopLeftInDiv.x +
      ", " +
      pxTopLeftInDiv.y +
      ")";
  },

  //TODO: Explicit Types?
  reposition: function (topleft, topright, bottomleft) {
    this._topLeft = L.latLng(topleft);
    this._topRight = L.latLng(topright);
    this._bottomLeft = L.latLng(bottomleft);

    this._reset();
  },

  updateOpacity: function (opacity: number) {
    if (opacity >= 0 && opacity <= 1) this._image.style.opacity = opacity;
  },

  //TODO: Explicit Types?
  setUrl: function (url) {
    this._url = url;

    if (this._rawImage) {
      this._rawImage.src = url;
    }
    return this;
  },
});

L.imageOverlay.rotated = function (
  imgSrc,
  topleft,
  topright,
  bottomleft,
  options
) {
  return new L.ImageOverlay.Rotated(
    imgSrc,
    topleft,
    topright,
    bottomleft,
    options
  );
};
