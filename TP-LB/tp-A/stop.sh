#!/bin/bash

# Arrêter et supprimer les conteneurs
docker stop nginx1 nginx2 nginx-lb
docker rm nginx1 nginx2 nginx-lb
