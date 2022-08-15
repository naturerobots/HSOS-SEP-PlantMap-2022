import type { Coords } from "./coords";
import type { Health } from "./health";
export interface Bed {
  id: number;
  plant: string;
  variety: string;
  plants: string;
  soil_humidity: number;
  harvest: string;
  yield: string;
  health: Health[];
  plant_coords: Coords[];
  avg_plant_lat: number;
  avg_plant_lon: number;
}
