# Using Node:10 Image Since it contains all the necessarity build tools required for dependencies with native build (node-gyp, python, gcc, g++, make)
# First Stage : to install and build dependences
FROM node:16-alpine
WORKDIR /app
COPY ./package.json ./
RUN apk add --no-cache curl
# Install always the latest version of npm
ADD https://www.npmjs.com/install.sh ./install.sh
RUN sh install.sh
RUN npm install --legacy-peer-deps

COPY . .
# Make executable wait for it
RUN chmod +x /app/wait_for_it.sh

RUN npm run build

RUN apk add bash

EXPOSE 4000 9229
CMD ["npm", "run", "start:debug"]
