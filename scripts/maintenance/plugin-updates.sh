#!/bin/bash
# Update plugin
set -e
PLUGINS="$1"
for plugin in $(echo $PLUGINS | tr "," "\n"); do
  echo "Aggiornamento plugin: $plugin"
  # Placeholder per update plugin
  echo "Plugin $plugin aggiornato"
done
