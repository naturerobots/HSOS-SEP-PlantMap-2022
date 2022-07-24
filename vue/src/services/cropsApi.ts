import type { Bed } from "@/types/crop";

export async function getCrops(): Promise<Bed[]> {
  //static demo data
  const crops: Bed[] = [];

  const crop1: Bed = {
    id: 1,
    plant: "Beans",
    variety: "Cauliflower",
    location: 1,
    soilHumidity: "65%",
    health: [
      {
        type: "Nutrient Deficiency",
        loglevel: 2,
        shortcut: "N",
      },
      {
        type: "Watering",
        loglevel: 0,
        shortcut: "W",
      },
      {
        type: "Disease Detection",
        loglevel: 2,
        shortcut: "D",
      },
    ],
    status: "vegetating",
    harvest: "3 months",
    yield: "N/A",
  };
  const crop2: Bed = {
    id: 2,
    plant: "Beetroot",
    variety: "Carrot",
    location: 2,
    soilHumidity: "5%",
    health: [
      {
        type: "Nutrient Deficiency",
        loglevel: 1,
        shortcut: "N",
      },
      {
        type: "Watering",
        loglevel: 1,
        shortcut: "W",
      },
      {
        type: "Disease Detection",
        loglevel: 2,
        shortcut: "D",
      },
    ],
    status: "ripening",
    harvest: "12 months",
    yield: "N/A",
  };
  const crop3: Bed = {
    id: 3,
    plant: "Broccoli",
    variety: "Chicory",
    location: 3,
    soilHumidity: "45%",
    health: [
      {
        type: "Nutrient Deficiency",
        loglevel: 1,
        shortcut: "N",
      },
      {
        type: "Watering",
        loglevel: 3,
        shortcut: "W",
      },
      {
        type: "Disease Detection",
        loglevel: 2,
        shortcut: "D",
      },
    ],
    status: "budding",
    harvest: "4 weeks",
    yield: "N/A",
  };
  const crop4: Bed = {
    id: 4,
    plant: "Carrot",
    variety: "Courgette",
    location: 1,
    soilHumidity: "15%",
    health: [
      {
        type: "Nutrient Deficiency",
        loglevel: 3,
        shortcut: "N",
      },
      {
        type: "Watering",
        loglevel: 1,
        shortcut: "W",
      },
      {
        type: "Disease Detection",
        loglevel: 2,
        shortcut: "D",
      },
    ],
    status: "flowering",
    harvest: "5 weeks",
    yield: "N/A",
  };
  const crop5: Bed = {
    id: 5,
    plant: "Chicory",
    variety: "Courgette",
    location: 1,
    soilHumidity: "61%",
    health: [
      {
        type: "Nutrient Deficiency",
        loglevel: 2,
        shortcut: "N",
      },
      {
        type: "Watering",
        loglevel: 3,
        shortcut: "W",
      },
      {
        type: "Disease Detection",
        loglevel: 2,
        shortcut: "D",
      },
    ],
    status: "budding",
    harvest: "1 month",
    yield: "N/A",
  };
  const crop6: Bed = {
    id: 6,
    plant: "Pepper",
    variety: "Radish",
    location: 4,
    soilHumidity: "37%",
    health: [
      {
        type: "Nutrient Deficiency",
        loglevel: 3,
        shortcut: "N",
      },
      {
        type: "Watering",
        loglevel: 2,
        shortcut: "W",
      },
      {
        type: "Disease Detection",
        loglevel: 1,
        shortcut: "D",
      },
    ],
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
