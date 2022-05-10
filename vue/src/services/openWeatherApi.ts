import axios from "axios";
import type { Weather, WeatherCurrent, WeatherForecast } from "@/types/weather";

//TODO: Checking if the request was successful

//TODO: Find a solution that the token is not directly implemented
const appid = "a8b46be95a90a7e303aa7edd4fc1463e";
const baseURL = "https://api.openweathermap.org/data/2.5";
const exclude = "current,minutely,hourly";
const lang = "de";
const units = "metric";

//TODO: maybe better naming for "weather"
export async function getWeatherInformation(lat: number, lon: number) {
  const weather: Weather = {
    current: {} as WeatherCurrent,
    forecast: [] as WeatherForecast[],
  };

  //API call for the current weather data
  //https://api.openweathermap.org/data/2.5/weather?lat=52.2799112&lon=8.0471788&lang=de&units=metric&appid=a8b46be95a90a7e303aa7edd4fc1463e
  let response = await axios.get(baseURL + "/weather", {
    params: { lat, lon, lang, units, appid },
  });
  weather.current = createWeatherCurrentObj(response.data);

  //API call for the 7 days forecast data
  //https://api.openweathermap.org/data/2.5/onecall?lat=52.2799112&lon=8.0471788&exclude=minutely,hourly&lang=de&units=metric&appid=a8b46be95a90a7e303aa7edd4fc1463e
  response = await axios.get(baseURL + "/onecall", {
    params: { lat, lon, exclude, lang, units, appid },
  });
  weather.forecast = createWeatherForecastObj(response.data);

  return weather;
}

//TODO: "any" Parameter ersetzen
function createWeatherCurrentObj(data: any): WeatherCurrent {
  const current: WeatherCurrent = {} as WeatherCurrent;

  current.name = data["name"];
  current.dt = data["dt"];
  current.tempMin = data["main"]["temp_min"];
  current.tempMax = data["main"]["temp_max"];
  current.description = data["weather"][0]["description"];
  current.icon = data["weather"][0]["icon"];

  return current;
}

//TODO: "any" Parameter ersetzen
function createWeatherForecastObj(data: any): WeatherForecast[] {
  const forecast: WeatherForecast[] = [] as WeatherForecast[];

  for (const result of data["daily"]) {
    const currentForecast: WeatherForecast = {} as WeatherForecast;
    currentForecast.dt = result["dt"];
    currentForecast.tempMin = result["temp"]["min"];
    currentForecast.tempMax = result["temp"]["max"];
    currentForecast.description = result["weather"][0]["description"];
    currentForecast.icon = result["weather"][0]["icon"];

    forecast.push(currentForecast);
  }

  return forecast;
}
