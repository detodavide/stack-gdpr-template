#!/bin/bash
# Backup con plugin data
set -e
PLUGINS="$1"
for plugin in $(echo $PLUGINS | tr "," "\n"); do
  echo "Backup dati per plugin: $plugin"
  # Placeholder per backup plugin
  echo "Backup per plugin $plugin completato"
done
