#!/bin/bash

PODMAN=`which podman`
PODMAN_COMPOSE=`which podman-compose`
OLLAMA=`which ollama`

[ -x "$PODMAN" ] && echo "Command '$PODMAN' not found, please install it." >&2 && exit 1
[ -x "$PODMAN_COMPOSE" ] && echo "Command '$PODMAN_COMPOSE' not found, please install it." >&2 && exit 1
[ -x "$OLLAMA" ] && echo "Command '$OLLAMA' not found, please install it." >&2 && exit 1

podman machine reset
podman machine init
podman machine set -m 10216
podman machine start
