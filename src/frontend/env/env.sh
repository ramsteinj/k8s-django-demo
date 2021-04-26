#!/bin/bash

echo "
    var env = {
        BACKEND_HOST: '${BACKEND_HOST}',
        BACKEND_PORT: '${BACKEND_PORT}',
        BACKEND_ENDPOINT: 'http://${BACKEND_HOST}:${BACKEND_PORT}'
    }
"