#!/bin/bash

PODMAN_COMPOSE_PROVIDER="/opt/homebrew/bin/podman-compose" podman compose -f compose.yaml down

podman rmi -a -f
podman volume rm -a
podman machine stop
