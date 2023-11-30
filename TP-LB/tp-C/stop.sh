#! /bin/bash

docker kill tp-c_nginx_1
docker kill tp-c_app_1

docker rm tp-c_nginx_1
docker rm tp-c_app_1
