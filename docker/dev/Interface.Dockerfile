FROM node:15.13-alpine

# copy the app and sh files
WORKDIR /usr/src/app/
COPY ./Interface /usr/src/app/
COPY ./sh /usr/src/app/

# Make executable wait for it
RUN chmod +x /usr/src/app/wait_for_it.sh

# Add bash to run wait_for_it
RUN apk add --no-cache bash
# Install node_modules
RUN npm install

# build the application
RUN npm run build

# expose 5000 port
EXPOSE 5000

# set app serving to permissive / assigned
ENV NUXT_HOST=0.0.0.0
# set app port
ENV NUXT_PORT=5000

# start the app
CMD [ "npm", "run", "start" ]
