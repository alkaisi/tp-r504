#! /bin/bash

docker kill tp-b_s-nginx_1
docker kill tp-b_s-app2_1
docker kill tp-b_s-app1_1

docker rm tp-b_s-nginx_1
docker rm tp-b_s-app2_1
docker rm tp-b_s-app1_1

