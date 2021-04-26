FROM nginx:1.17.10

RUN rm /etc/nginx/conf.d/default.conf

COPY ./frontend/env /usr/share/nginx/env
COPY ./frontend/content /usr/share/nginx/html
COPY ./frontend/conf/nginx.conf /etc/nginx/nginx.conf

RUN mkdir /app
WORKDIR /app
COPY ./frontend/docker-entrypoint.sh /app