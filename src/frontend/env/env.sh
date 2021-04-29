#!/bin/bash

echo "
    var env = {
        POD_NAME: '${POD_NAME}',
        BACKEND_HOST: '${BACKEND_HOST}',
        BACKEND_PORT: '${BACKEND_PORT}',
        BACKEND_ENDPOINT: 'http://${BACKEND_HOST}:${BACKEND_PORT}'
    }
"