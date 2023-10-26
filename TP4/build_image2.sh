#!/bin/bash

# Construire l'image à partir de Dockerfile2
docker build -t im-tp4-v2 -f Dockerfile2 .

echo "Taille de votre nouvelle image im-tp4-v2:"
docker images im-tp4-v2 --format "{{.Size}}"
