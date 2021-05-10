FROM nginx:1.17.10

RUN rm /etc/nginx/conf.d/default.conf

COPY ./backend-nginx/conf/nginx.conf /etc/nginx/nginx.conf

RUN mkdir /app
WORKDIR /app
COPY ./backend-nginx/docker-entrypoint.sh /app