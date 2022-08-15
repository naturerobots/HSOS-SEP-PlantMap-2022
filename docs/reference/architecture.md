# Architecture

This section provides an overview of the software architecture as well as the
Docker setup.

## Overview :bookmark_tabs:

This overview should complement the [data flow](../data-flow.md) description and
goes into more technical detail. The Django 4[^1] server combines all components
into a single REST-API, which is then used by the VueJs[^2] frontend. Django uses
gRPC with Protocol Buffers[^3] to query SEEREP[^4] for scalar data. Protocol
Buffers is a language and platform neutral mechanism for serializing data,
developed and open-sourced by Google. It's equivalent to JSON, except it's more
efficient and much faster.

Downloading the point clouds from SEEREP every time a request for them is passed
to the Django server would take too long for a satisfactory experience, so they
are cached locally. For that, the RabbitMQ[^5] message broker handles
asynchronous tasks to download the point clouds in predetermined time intervals.

The PostgreSQL[^6] database is used by Django to store general information like
the user data and their access rights. In addition to that, coordinates for the
beds are stored so that they can be accurately displayed on a satellite image.

<figure markdown>
![frontend-backend](../imgs/backend-frontend.png){width=600px}
    <figcaption> Overview of the software architecture </figcaption>
</figure>

## Docker Setup :whale:

The Digital Logbook is split into three Docker containers. We use a Visual
Studio Code development container as a preconfigured development environment. In
the development container, often abbreviated to dev-container, developers can
work on the Django and VueJs code. The Docker image for that can be downloaded
from the GitHub container registry of the repository[^7]. RabbitMQ 3.10.7 and
PostgreSQL 14 are the standard images from Docker Hub[^8].

<figure markdown>
![docker-setup](../imgs/docker-setup.png){width=500px}
    <figcaption> Docker setup of the PlantMap Digital Logbook</figcaption>
</figure>

[^1]: [Django, Official Documentation](https://www.djangoproject.com/)
[^2]: [Vue, Official Documentation](https://vuejs.org/)
[^3]: [Google, Protocol Buffers Documentation](https://developers.google.com/protocol-buffers)
[^4]: [Github, SEEREP](https://github.com/agri-gaia/seerep)
[^5]: [RabbitMQ, Official Documentation](https://www.rabbitmq.com/)
[^6]: [PostgreSQL, Official Documentation](https://www.postgresql.org/)
[^7]: [Github container registry of the
    repository](https://github.com/naturerobots/HSOS-SEP-PlantMap-2022/pkgs/container/plant-map-digital-logbook)
[^8]: [Docker Hub](https://hub.docker.com/)