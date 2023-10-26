#!/bin/bash

# Remplissage de la BDD via les commandes du fichier data.sql
mysql -u root -p'foo' -h 127.0.0.1 --port=3307 < data.sql
