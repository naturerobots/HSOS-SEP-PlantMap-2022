// import type { Crop } from "./crop";
import type { Location3d } from "./location3d";
import type { Health } from "./health";

export type Crop3dArray = Crop3d[];

export interface Crop3d {
  /*
  geometryUUID: string,
  url: string,
  crop: Crop,
  location3d: Location3d,
  locationDescription: string,
  progress: number,
  */

  geometryUUID: string;
  url: string;
  name: string;
  type: string;
  locationDescription: string;
  location3d: Location3d;
  health: Health[];
  yield: string;
  status: string;
  harvest: string;
  progress: 0.6;
}
