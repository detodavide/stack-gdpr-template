#!/bin/bash
# Crea nuovo progetto GDPR-compliant
set -e
PROJECT_NAME="$1"
TEMPLATE="$2"
PLUGINS="$3"
FRONTEND="$4"

# Setup base
cp -r stack-gdpr-template "$PROJECT_NAME"
cd "$PROJECT_NAME"

# Attiva plugin
for plugin in $(echo $PLUGINS | tr "," "\n"); do
  echo "Attivazione plugin: $plugin"
  # Placeholder per attivazione plugin
done

# Setup frontend
if [ "$FRONTEND" != "" ]; then
  echo "Setup frontend: $FRONTEND"
  # Placeholder per setup frontend
fi

echo "✅ Progetto '$PROJECT_NAME' creato e configurato"
