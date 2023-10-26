#!/bin/bash

./purge.sh

./create_network.sh
docker network ls

./run_mysql.sh

# Attendre 40 secondes
echo "Veuillez patienter..."
sleep 40

./filldb.sh

./build_image.sh

./run-app.sh
