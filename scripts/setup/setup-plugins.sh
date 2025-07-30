#!/bin/bash
# Setup plugin specifici
set -e
PLUGINS="$1"
for plugin in $(echo $PLUGINS | tr "," "\n"); do
  echo "Configurazione plugin: $plugin"
  # Placeholder per configurazione
  # Esempio: python scripts/setup/configure_plugin.py $plugin
  echo "Plugin $plugin configurato"
done
