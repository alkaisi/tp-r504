#!/bin/bash

# Lancer le conteneur à partir de l'image im-tp4
docker run -d \
    --name tp4-app \
    --network net-tp4 \
    -p 5000:5000 \
    im-tp4
