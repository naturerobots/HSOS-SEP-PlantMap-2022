import type { Crop } from "@/types/crop";

export async function getCrops() {
  //static demo data
  const crops: Crop[] = [];

  const crop1: Crop = {
    id: 1,
    plant: "Beans",
    variety: "Cauliflower",
    location: 1,
    soilHumidity: "65%",
    health: "Good",
    status: "vegetating",
    harvest: "3 months",
    yield: "N/A",
  };
  const crop2: Crop = {
    id: 2,
    plant: "Beetroot",
    variety: "Carrot",
    location: 2,
    soilHumidity: "5%",
    health: "Good",
    status: "ripening",
    harvest: "12 months",
    yield: "N/A",
  };
  const crop3: Crop = {
    id: 3,
    plant: "Broccoli",
    variety: "Chicory",
    location: 3,
    soilHumidity: "45%",
    health: "Okay",
    status: "budding",
    harvest: "4 weeks",
    yield: "N/A",
  };
  const crop4: Crop = {
    id: 4,
    plant: "Carrot",
    variety: "Courgette",
    location: 1,
    soilHumidity: "15%",
    health: "Bad",
    status: "flowering",
    harvest: "5 weeks",
    yield: "N/A",
  };
  const crop5: Crop = {
    id: 5,
    plant: "Chicory",
    variety: "Courgette",
    location: 1,
    soilHumidity: "61%",
    health: "Okay",
    status: "budding",
    harvest: "1 month",
    yield: "N/A",
  };
  const crop6: Crop = {
    id: 6,
    plant: "Pepper",
    variety: "Radish",
    location: 4,
    soilHumidity: "37%",
    health: "Bad",
    status: "budding",
    harvest: "2 months",
    yield: "N/A",
  };

  crops.push(crop3);
  crops.push(crop4);
  crops.push(crop1);
  crops.push(crop2);
  crops.push(crop5);
  crops.push(crop6);

  return crops;
}
