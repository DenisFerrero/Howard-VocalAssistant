# Using Node:10 Image Since it contains all the necessarity build tools required for dependencies with native build (node-gyp, python, gcc, g++, make)
# First Stage : to install and build dependences
FROM node:10 as builder
WORKDIR /app
COPY ./package.json ./
RUN npm install

COPY . .
# Make executable wait for it
RUN chmod +x /app/wait_for_it.sh

# Offline speech models
# RUN wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
# RUN wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer

# Additional lib
# #TODO Install Sox

RUN npm run build

# Second Stage : Setup command to run your app
FROM node:10-alpine
WORKDIR /app
COPY --from=builder /app ./
EXPOSE 4000
CMD ["npm", "run", "start:prod"]
