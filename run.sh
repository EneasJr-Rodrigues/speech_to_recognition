#!/bin/bash
echo "Up Containers - Speech-API"
docker-compose --env-file config/local/.env up -d
echo "=================================="