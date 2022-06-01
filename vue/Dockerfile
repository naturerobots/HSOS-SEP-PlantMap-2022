FROM node:lts-alpine as build-stage

RUN mkdir -p /vue
COPY . /vue
WORKDIR /vue

RUN npm ci
RUN npm run build

FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /vue/dist /usr/share/nginx/html
EXPOSE 80
