#!/bin/bash
set -e

docker compose --file ../observe/demo/docker-compose.yml --project-directory ../observe up --abort-on-container-exit --remove-orphans