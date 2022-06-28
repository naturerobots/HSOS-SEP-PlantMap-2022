import axios from "axios";
import type {
  WeatherDataCurrent,
  WeatherDataForecast,
} from "@/types/weatherData";

//FIXME: token stored in .env -> could be safed in .env.local later which is ignored by git
const appid: string = import.meta.env.VITE_TOKEN_OWM;
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
