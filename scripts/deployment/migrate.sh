#!/bin/bash
# Migrations con plugin
set -e
PLUGINS="$1"
for plugin in $(echo $PLUGINS | tr "," "\n"); do
  echo "Migrazione per plugin: $plugin"
  # Placeholder per migrazione plugin
  echo "Migrazione per plugin $plugin completata"
done
