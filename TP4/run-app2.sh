#!/bin/bash

#!/bin/bash

# Lancer le conteneur avec un bind mount
docker run -d \
    --name tp4-app-v2 \
    --network net-tp4 \
    -p 5000:5000 \
    -v $(pwd)/srv:/srv \
    im-tp4-v2
