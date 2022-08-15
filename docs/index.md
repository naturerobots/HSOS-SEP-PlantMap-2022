# Home :house_with_garden:

This page provides general information about the project, as well as context, too
better understand the problems it tries to solve.

This project was developed by students from the [University of Applied
Sciences Osnabrück](https://www.hs-osnabrueck.de/en/) in their software
engineering course in cooperation with [Nature Robots](https://naturerobots.de/)
and the [DFKI PBR
Osnabrück](https://www.dfki.de/web/forschung/forschungsbereiche/planbasierte-robotersteuerung).

## Current Problems In Agriculture :tractor:

The current industrial agriculture has a couple of different problems, that have
an **impact on all of us**. First, it is responsible for one quarter of the
world's greenhouse gas emissions[^1]. Second, the destruction of the Earths
ecosystem, resulting in substantial loss in biodiversity. Biodiversity describes
the variety of living species on Earth[^2], including plants, animals and
others. Due to the highly international market for agricultural products,
farmers try to optimize for yields and income. This results in huge areas which
are optimized for machines, rather than small animals and wild plants.
Additionally, the use of artificial fertilizer and pesticides, harm small insects
on the ground and in the air. A study from 2017 showed a 75% decline of the
flying insect biomass in protected areas in Germany[^3]. In conclusion, **we have to
change something** to preserve our Earth.

## Microfarming :seedling:

One possible solution could be mircofarming. Microfarming describes the use off
small agricultural areas for the cultivation and sale of vegetables, which does
not require large machinery. It focuses and the on the preservation and
regeneration of the entire ecosystem by using mulch in combination with minimal
tillage[^4]. Low investment costs and relatively high crop yields make it
**competitive against conventional farming**. One example for a mircofarming
garden is grööntüügs[^5] (lower German for greenery) from Ibbenbüren a drone
picture of their garden can be found below.

But there are some **hurdles to overcome** when starting or running a
mircofarming garden:

- The management of the cultivation, crop rotations and work planning can be
  complex and can often lead to the fact that newcomers are not able to be
  economically profitable.
- Scaling up the garden is often not possible due to the amount of time
  needed to monitor the plants manually.
- Very little tools to support gardeners in their work (hardware and software wise).

With the development of the **PlantMap Digital Logbook** we want to tackle some
of the existing problems, when switching to or running an environment friendly garden.

<figure markdown>
  ![Grööntüügs Ibbenbüren](imgs/mirco-farming-garden.jpg){width=700px}
  <figcaption> Grööntüügs Ibbenbüren </figcaption>
</figure>

## Goals of this project :goal_net:

This section outlines the main goals of the developed **PlantMap Digital
Logbook**. Most of them are directly derived from the above listed hurdles. If
you are having trouble to grasp some of the concepts or terminology here, please
have a look at [project overview](./concept.md) or the
[terminology](reference/definitions.md) page.

- Create a digital representation of a garden, to have a better overview of it's
  current status. It should also be possible to have multiple gardens in
  different locations.
- Provide an overview of all beds and plants in a garden.
- Add notifications for warnings, e.g when the plants need water or a disease is detected.
- Possibility to view recorded point clouds of individual beds.
- Provide a user management, so that employees and admins can be assigned to a garden.

Of course there are many things that could be added, future plans are listed in
the [improvements section](getting-started/improvements.md).

[^1]: [Our World in Data, Environmental Impacts of Food Production](https://ourworldindata.org/environmental-impacts-of-food#:~:text=The%20expansion%20of%20agriculture%20has,threat%20for%2024%2C000%20of%20them.)
[^2]: [National Geographic, Biodiversity](https://education.nationalgeographic.org/resource/biodiversity)
[^3]: [PLOS ONE, More than 75 percent decline over 27 years in total flying insect biomass
    in protected areas](More than 75 percent decline over 27 years in total
    flying insect biomass in protected areas)
[^4]: [Nature Robots, Ökologische Anbausysteme: Mikrofarming
    (German)](https://naturerobots.de/blog/oekologische-anbausysteme-mikrofarming/)
[^5]: [Open Food Network, Grööntüügs ](https://openfoodnetwork.de/groontuugs/shop#/about)