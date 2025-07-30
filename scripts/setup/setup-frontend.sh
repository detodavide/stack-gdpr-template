#!/bin/bash
# Setup frontend con plugin
set -e
FRONTEND="$1"
PLUGINS="$2"

if [ "$FRONTEND" != "" ]; then
  echo "Configurazione frontend: $FRONTEND"
  # Placeholder per setup frontend
fi
for plugin in $(echo $PLUGINS | tr "," "\n"); do
  echo "Configurazione frontend per plugin: $plugin"
  # Placeholder per setup frontend plugin
  echo "Frontend per plugin $plugin configurato"
done
