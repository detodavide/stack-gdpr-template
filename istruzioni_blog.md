# Demo Blog - Istruzioni di Avvio Completo

Questa guida ti permette di avviare un blog GDPR-compliant da zero usando lo stack STAKC, verificando ogni componente dal setup alla dashboard admin.

## 1. Prerequisiti

- Docker e Docker Compose installati
- Node.js e npm (solo per frontend Next.js)
- Python 3.x (per script e test)

## 2. Setup progetto e configurazione

```bash
# Clona lo stack (o copia la cartella stack-gdpr-template)
git clone <repo-url> demo-blog
cd demo-blog

# Esegui lo script di setup
bash setup-project.sh --name=demo-blog --template=blog --plugins=gdpr,security,analytics --frontend=nextjs_base --domain=localhost
```

## 3. Controllo e modifica file .env

- Apri `.env` generato nella root del progetto
- Verifica e personalizza:
  - PASSWORD e chiavi (SECRET_KEY, GDPR_ENCRYPTION_KEY)
  - SMTP per email
  - PORT e DOMAIN

## 4. Installazione dipendenze frontend

```bash
cd frontend_templates/nextjs_base
npm install
npm run build
cd ../..
```

## 5. Avvio servizi

```bash
cd demo-blog
docker-compose up -d
```

## 6. Verifica servizi

- Controlla che tutti i container siano attivi:
  ```bash
  docker-compose ps
  ```
- Controlla i log:
  ```bash
  docker-compose logs -f api
  ```
- Verifica healthcheck:
  - http://localhost/health

## 7. Accesso applicazione

- **Frontend Blog:** [http://localhost](http://localhost)
- **API Docs:** [http://localhost/docs](http://localhost/docs)
- **Admin Panel:** [http://localhost/admin](http://localhost/admin)
- **MailHog (dev):** [http://localhost:8025](http://localhost:8025)

## 8. Generazione e verifica Privacy Policy

```bash
python scripts/generators/generate_privacy_policy.py --output docs/privacy_policy.md --project-name demo-blog --contact-email dpo@localhost
```
- Apri `docs/privacy_policy.md` e verifica che sia aggiornata e corretta.

## 9. Test end-to-end GDPR

```bash
pytest tests/core/test_gdpr_e2e.py
```
- Verifica che tutti i test passino (consenso, export, cancellazione, breach).

## 10. Verifica dashboard GDPR admin

- Accedi alla dashboard GDPR admin:
  - **GDPR Admin Dashboard:** [http://localhost/admin/gdpr](http://localhost/admin/gdpr) (o percorso configurato)
- Controlla che tutte le metriche siano visibili:
  - Consensi attivi/scaduti
  - Export e cancellazioni richieste/completate
  - Notifiche breach
  - Versioni privacy policy
  - Audit trail
  - Richieste DPO

## 11. Personalizzazione e sviluppo

- Modifica `.env` per password, chiavi, SMTP
- Personalizza contenuti blog in `project_templates/blog/`
- Modifica template frontend in `frontend_templates/nextjs_base/`
- Estendi dashboard GDPR admin per nuove metriche

## 12. Note e troubleshooting

- Tutti i plugin sono modulari e attivabili/disattivabili
- Backup e audit automatici su database
- Sicurezza: rate limiting, bot detection, IP blocking, security headers
- Se una metrica non appare, verifica che la tabella corrispondente sia presente nel database
- Consulta i log per errori e debugging

---
Demo pronta per presentazione, sviluppo, audit GDPR e test end-to-end.
