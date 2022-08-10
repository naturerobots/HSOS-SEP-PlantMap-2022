import type { Coords } from "./coords";
import type { Health } from "./health";

export interface Crop {
  id: number;
  bed_id: number;
  plant: string;
  variety: string;
  // location: number;
  soil_humidity: string;
  // status: string;
  harvest: string;
  yield: string;
  health: Health[];
  // plant_coords: Coords;
}
