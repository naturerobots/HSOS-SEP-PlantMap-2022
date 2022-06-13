export type GeoDataArray = GeoData[];

export interface GeoData {
  name: string;
  lat: number;
  lon: number;
  local_names: any;
  country: string;
  state: string;
}
