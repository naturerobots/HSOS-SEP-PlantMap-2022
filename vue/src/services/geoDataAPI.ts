import axios from "axios";
import type { GeoDataArray } from "../types/geoData";

//FIXME: Find a solution that the token is not directly implemented
const appid = "a8b46be95a90a7e303aa7edd4fc1463e";
const baseURL = "https://api.openweathermap.org/geo/1.0/reverse";
const limit = 5;

//http://api.openweathermap.org/geo/1.0/reverse?lat=52.2799112&lon=8.0471788&limit=5&appid=a8b46be95a90a7e303aa7edd4fc1463e
export async function getGeoData(
  lat: number,
  lon: number
): Promise<GeoDataArray> {
  const response = await axios.get<GeoDataArray>(baseURL, {
    params: { lat, lon, limit, appid },
  });

  return response.data;
}
