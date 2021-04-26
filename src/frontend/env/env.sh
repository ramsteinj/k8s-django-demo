#!/bin/bash

echo "
    var BACKEND_HOST='${BACKEND_HOST}';
    var BACKEND_PORT='${BACKEND_PORT}';
    var BACKEND_ENDPOINT= 'http://${BACKEND_HOST}:${BACKEND_PORT}';
"