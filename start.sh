#!/bin/bash

PODMAN_COMPOSE=`which podman-compose`

podman machine start

PODMAN_COMPOSE_PROVIDER="$PODMAN_COMPOSE" podman compose -f compose.yaml up -d
ollama pull granite3.2:latest

echo "Waiting for things to settle..."
sleep 10
open http://localhost:8000
