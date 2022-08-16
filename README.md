# README

<!--
The following template was used to create this README:
https://github.com/othneildrew/Best-README-Template

MIT License

Copyright (c) 2021 Othneil Drew

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
-->

<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="docs/imgs/plant-map-logo.png" alt="Logo">
  </a>

  <h3 align="center">PlantMap digital logbook</h3>

  <p align="center">
    A tool to support sustainable farming
    <br />
    <a href="https://naturerobots.github.io/HSOS-SEP-PlantMap-2022/"><strong>Documentation»</strong></a>
    <br />
  </p>
</div>

## Table of Contents

- [README](#readme)
  - [Table of Contents](#table-of-contents)
  - [General](#general)
  - [Quick Start](#quick-start)
  - [Documentation](#documentation)
  - [Contributing](#contributing)
  - [License](#license)

## General

This project was developed in the software engineering course of the [University
of Applied Sciences Osnabrück](https://www.hs-osnabrueck.de/en/) in cooperation
with [Nature Robots](https://naturerobots.de/) and the [DFKI PBR
Osnabrück](https://www.dfki.de/web/forschung/forschungsbereiche/planbasierte-robotersteuerung).
The goal was to create a platform to support sustainable micro farming
gardeners. Mirco farming focus on the preservation and regeneration of the
entire ecosystem, as well as on soil fertility. In this process, up to fifty
different types of vegetables are cultivated close to each other in narrow
culture strips.  

However, the entry into the cultivation concept is associated with numerous
hurdles. A great deal of expertise is required for cultivation, making access
difficult for newcomers and those switching from conventional agriculture.

To overcome the obstacles, the **PlantMap Digital Logbook** creates a digital
twin of the garden. Thereby various aspects like the growth and the health of
the plants can be monitored. This allows for an early detection and treatment of
diseases, as well as optimizations on bed planning and yield estimates.
Furthermore, instructions can be passed to the gardener or his staff. The data is
gathered by the autonomous driving robot
[Lero](https://naturerobots.de/blog/lero-robot-prototype/) and is stored in the
semantical environment representation
[SEEREP](https://github.com/agri-gaia/seerep).

## Quick Start

For running the application, we assume that you have a current version of
[Visual Studio Code](https://code.visualstudio.com/) and
[Docker](https://www.docker.com/). Further, Visual Studio Code **needs** to have
the **docker and the remote container extensions installed**. If you didn't
understand the requirements,  please visit the [installation
guide](https://naturerobots.github.io/HSOS-SEP-PlantMap-2022/getting-started/installation/)
in the documentation for more detailed steps.

To get started, clone the repository and open it in Visual Studio Code:

```sh
  git clone https://github.com/naturerobots/HSOS-SEP-PlantMap-2022.git
  cd HSOS-SEP-PlantMap-2022
  code .
```

Next, we need to mount the current workspace into the projects docker container
to use it as a preconfigured development environment. For that, you can press
`F1` or `CTRL+SHIFT+P` and enter `Remote-Containers: Reopen Folder in Container`
and confirm with `ENTER`. Visual Studio Code additionally shows a notification
after opening the project in the bottom right corner with the same option. Now
the [docker
image](https://github.com/naturerobots/HSOS-SEP-PlantMap-2022/pkgs/container/plant-map-digital-logbook)
of the project along with the images for the
 [PostgreSQL](https://www.postgresql.org/) database and the
 [RabbitMQ](https://www.rabbitmq.com/) message broker are downloaded.
 Additionally, the set-up of all required packages and extensions is handled.

The default user for the container is:

```shell
user: docker
password: docker
  ```

## Documentation  

The full documentation of the project can be found on [GitHub
Pages](https://naturerobots.github.io/HSOS-SEP-PlantMap-2022/). It provides
detailed information on the architecture, the REST-API interface as well as
general topics.

## Contributing

Contributions are what make the open source community such an amazing place to
learn and inspire. Any contributions are **greatly appreciated**.

This repository uses [pre-commit](https://pre-commit.com/) checks to verify the
code style before committing. Since the pre-commit checks are automatically
installed in the development container, they are run before each commit you
make. The checks can also be run manually with:

```bash
pre-commit run -a
```

We also **enforce commit conventions** via the pre-commit checks to add semantic
meaning to the git history. A quick summary of the convention is provided here,
for more details, visit the
[documentation](https://naturerobots.github.io/HSOS-SEP-PlantMap-2022/getting-started/installation/).

Each commit should therefore have the following structure: `<type>(optional
scope): <description>`. Example types could be `feat`, `fix`, `build`, `docs`,
`refactor`, `test`. The [conventional commit
specification](https://www.conventionalcommits.org/en/v1.0.0/#specification)
provides concise information on when to use which type and how scopes can be
used.

## License

Distributed under the BSD 3-Clause License. See `LICENSE.txt` for more
information.
