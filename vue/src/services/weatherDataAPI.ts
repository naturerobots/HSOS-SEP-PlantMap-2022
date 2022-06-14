import axios from "axios";
import type {
  WeatherDataCurrent,
  WeatherDataForecast,
} from "@/types/weatherData";

//FIXME: Find a solution that the token is not directly implemented
const appid = "a8b46be95a90a7e303aa7edd4fc1463e";
const baseURL = "https://api.openweathermap.org/data/2.5";
const exclude = "current,minutely,alerts";
const lang = "de";
const units = "metric";

//TODO: Checking if the requests were successful
//      -> What to do if the request failed?

//API call for the current weather data
export async function getWeatherDataCurrent(
  lat: number,
  lon: number
): Promise<WeatherDataCurrent> {
  const response = await axios.get<WeatherDataCurrent>(baseURL + "/weather", {
    params: { lat, lon, lang, units, appid },
  });

  return response.data;
}

//API call for the 7 days forecast data
export async function getWeatherDataForecast(
  lat: number,
  lon: number
): Promise<WeatherDataForecast> {
  const response = await axios.get<WeatherDataForecast>(baseURL + "/onecall", {
    params: { lat, lon, exclude, lang, units, appid },
  });

  return response.data;
}
