#!/bin/bash
echo "Remove all volumes - Speech-API"
docker-compose --env-file config/local/.env down
echo "=================================="