# Common Errors

This page should be used as a summary of common errors encountered while
developing the project. Have a look at it, when you're encountering some weird
problem, maybe it's listed here and if not, consider adding it.

## Docker Compose Error

If you are having trouble starting the development container, the problem may be
that you are using the old `docker-compose` package.

After doing a `apt search docker compose` we retrieve the following result.

```bash
docker-compose/focal,focal 1.25.0-1 all
  Punctual, lightweight development environments using Docker

docker-compose-plugin/focal,now 2.6.0~ubuntu-focal amd64 [installed]
  Docker Compose (V2) plugin for the Docker CLI.

python3-ck/focal,focal 1.9.4-1.1 all
  Python3 light-weight knowledge manager
```

The `docker-compose` package is deprecated and **may not support
compose specification 3.8 if you are using a distro with old packages**. Install the `docker-compose-plugin`
package instead to solve this problem!

If you have the old `docker-compose` installed remove it with
`sudo apt remove docker-compose` and install the newer version with
`sudo apt install docker-compose-plugin`.
Now `docker compose version` should return:

```bash
Docker Compose version v2.5.0
```

If the `docker-compose-plugin` package can't be found, set up the docker
repository, use the installation guide provided
[here](https://docs.docker.com/engine/install/ubuntu/).
