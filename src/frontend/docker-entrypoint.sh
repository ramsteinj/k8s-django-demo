#!/bin/bash

# Generate env.js
echo "Generating env.js file..."
/usr/share/nginx/env/env.sh > /usr/share/nginx/html/env.js

# Start nginx
echo "Starting nginx..."
nginx