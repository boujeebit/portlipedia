FROM node:alpine as builder
WORKDIR '/app'
COPY . .
RUN yarn install
RUN yarn build
RUN mv dist/static/js dist/js
RUN rm -rf dist/static/
RUN cat dist/index.html | sed 's/\/css\//\/static\/css\//g' > dist/temp.html
RUN mv dist/temp.html dist/index.html

CMD ["yarn", "serve"]