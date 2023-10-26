#!/bin/bash

# Arrête et supprime tous les conteneurs
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)

# Supprime tous les réseaux inutilisés
docker network prune -f

# Supprime tous les volumes inutilisés
docker volume prune -f

# Supprime toutes les images inutilisées
docker image prune -f

# Supprime tous les "build cache" inutilisés
docker builder prune -f
