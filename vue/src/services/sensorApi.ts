import sensorMockData from "@/assets/mocks/sensorMockData.json";

import type { Sensor } from "@/types/sensor";

export async function getSensorInformation(): Promise<Sensor[]> {
  return sensorMockData;
}
