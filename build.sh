#!/bin/bash
echo "====================================================================="
echo "Build Project Speech to text"
docker-compose --env-file config/local/.env build
echo "====================================================================="
