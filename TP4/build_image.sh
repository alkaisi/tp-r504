#!/bin/bash

# Construire l'image à partir du Dockerfile1
docker build -t im-tp4 -f Dockerfile1 .

# Afficher la taille des images
echo "Taille de l'image Debian11:"
docker images debian:11 --format "{{.Size}}"

echo "Taille de votre image im-tp4:"
docker images im-tp4 --format "{{.Size}}"
