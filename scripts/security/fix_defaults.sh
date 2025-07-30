#!/bin/bash
# 🔒 SECURITY HOTFIX - Rimozione default pericolosi

# Genera secrets sicuri
openssl rand -base64 64 > .secrets/secret_key
openssl rand -base64 32 > .secrets/gdpr_key
openssl rand -base64 16 > .secrets/db_password

# Update .env.example
cat > .env.example << 'EOF'
# 🚨 CAMBIA TUTTI I VALORI IN PRODUZIONE
SECRET_KEY=CHANGE_ME_$(openssl rand -base64 64)
GDPR_ENCRYPTION_KEY=CHANGE_ME_$(openssl rand -base64 32)
DATABASE_URL=postgresql://admin:CHANGE_ME@localhost:5432/stakc_app
CORS_ORIGINS=https://yourdomain.com,https://api.yourdomain.com
ALLOWED_HOSTS=yourdomain.com,api.yourdomain.com
EOF
