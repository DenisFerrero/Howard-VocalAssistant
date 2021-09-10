# Howard

Vocal assistant for developer

## Development

### Run assistant

```shell
cd ./Assistant && npm run start:dev
```

### Run interface

```shell
cd ./Interface && npm run dev
```

## Docker

### Build images

```shell
docker build -t web-interface -f ./Interface/Dockerfile ./Interface
docker build -t vocal-assistant -f ./Assistant/Dockerfile ./Assistant
```

### Run the docker-compose

```shell
docker-compose -f docker-compose.dev.yml up
```

## Raspberry auto-installation (**Still untested!!**)

```shell
./install.sh
```
