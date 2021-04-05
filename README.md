# Howard-VocalAssistant
Vocal assistant for developer

# Docker build command
## Build vocal assistant image (linux)
docker build -t vocal-assistant -f docker/dev/VocalAssistant.linux.Dockerfile .
## Build interface
docker build -t interface -f docker/dev/Interface.Dockerfile .
## Run the docker-compose
docker-compose -f ./docker/dev/docker-compose.yml up -d
