import axios from "axios";
import type { Weather, WeatherCurrent, WeatherForecast } from "@/types/weather";

//FIXME: Find a solution that the token is not directly implemented
const appid = "a8b46be95a90a7e303aa7edd4fc1463e";
const baseURL = "https://api.openweathermap.org/data/2.5";
const exclude = "current,minutely,hourly";
const lang = "de";
const units = "metric";

export async function getWeatherInformation(lat: number, lon: number) {
  const weather: Weather = {
    current: {} as WeatherCurrent,
    forecast: [] as WeatherForecast[],
  };

  //TODO: Checking if the requests were successful
  //      -> What to do if the request failed?

  //API call for the current weather data
  let response = await axios.get(baseURL + "/weather", {
    params: { lat, lon, lang, units, appid },
  });
  weather.current = createWeatherCurrentObj(response.data);

  //API call for the 7 days forecast data
  response = await axios.get(baseURL + "/onecall", {
    params: { lat, lon, exclude, lang, units, appid },
  });
  weather.forecast = createWeatherForecastObj(response.data);

  return weather;
}

function createWeatherCurrentObj(data: any): WeatherCurrent {
  const current: WeatherCurrent = {} as WeatherCurrent;

  current.name = data["name"];
  current.dt = new Date(data["dt"] * 1000);
  current.tempMin = data["main"]["temp_min"]; //FIXME: temp_min is the current place min temp and not the min temp of the day
  current.tempMax = data["main"]["temp_max"];
  current.description = data["weather"][0]["description"];
  current.icon = data["weather"][0]["icon"];

  return current;
}

function createWeatherForecastObj(data: any): WeatherForecast[] {
  const forecast: WeatherForecast[] = [] as WeatherForecast[];

  for (const result of data["daily"]) {
    const currentForecast: WeatherForecast = {} as WeatherForecast;
    currentForecast.dt = new Date(result["dt"] * 1000);
    currentForecast.tempMin = result["temp"]["min"];
    currentForecast.tempMax = result["temp"]["max"];
    currentForecast.description = result["weather"][0]["description"];
    currentForecast.icon = result["weather"][0]["icon"];

    forecast.push(currentForecast);
  }

  return forecast;
}
