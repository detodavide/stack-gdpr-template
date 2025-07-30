# GDPR Compliance - STAKC GDPR Template

Questo stack è progettato per garantire la conformità al GDPR in modo automatico, modulare e verificabile. Di seguito sono elencate tutte le misure implementate e come vengono rispettati i principali requisiti del Regolamento Europeo 2016/679.

---

## 1. Privacy by Design & by Default

- Tutta la business logic è separata dai plugin GDPR e Security.
- I dati sensibili sono gestiti solo tramite modelli e servizi dedicati.
- I plugin sono isolati e possono essere aggiornati senza impattare il core.

## 2. Gestione Consensi

- Banner e dashboard consensi nel frontend (`CookieConsentBanner`, `PrivacyDashboard`).
- Endpoint API per registrare, aggiornare e revocare consensi.
- Scadenza consensi configurabile (`GDPR_CONSENT_EXPIRY_DAYS`).
- Consensi granulari per diverse categorie di dati.

## 3. Diritto all’Accesso e Portabilità

- Endpoint `/gdpr/export` per esportare tutti i dati utente in formato JSON, CSV o XML.
- Componente frontend `DataExportButton` per richiesta export.
- Log di tutte le esportazioni tramite audit trail.

## 4. Diritto alla Cancellazione (Right to Erasure)

- Endpoint API per cancellazione sicura dei dati utente.
- Anonimizzazione automatica dei dati scaduti (`GDPR_AUTO_ANONYMIZE`).
- Backup e log delle operazioni di cancellazione.

## 5. Audit Trail & Logging

- Plugin Audit registra tutte le operazioni sensibili (export, cancellazione, login, modifica dati).
- Log consultabili via API (`/audit/logs`) e esportabili.
- Audit log separati per compliance e sicurezza.

## 6. Sicurezza dei Dati

- Crittografia automatica dei dati sensibili (`GDPR_ENCRYPTION_KEY`).
- Rate limiting, bot detection, security headers tramite Security Plugin.
- Backup automatici e disaster recovery.

## 7. Data Minimization & Retention

- Retention configurabile (`GDPR_RETENTION_DAYS`).
- Solo i dati strettamente necessari vengono raccolti e conservati.
- Task automatici per pulizia e anonimizzazione.

## 8. Multi-tenant & Multi-template

- Ogni progetto può avere policy GDPR dedicate.
- Configurazione centralizzata e override via `.env`.

## 9. Documentazione & Trasparenza

- Tutte le policy, procedure e API sono documentate in `docs/`.
- OpenAPI/Swagger per trasparenza sulle API.
- Esempi di export, cancellazione e consensi disponibili.

## 10. Gestione Data Breach

- Plugin dedicato per notifiche di violazione dati (`data_breach_plugin`).
- Endpoint `/breach/notify` per segnalazione e audit di incidenti.
- Possibilità di integrazione con notifiche automatiche a utenti/DPO.

## 11. Registro delle Policy

- Modello e API per versionamento delle policy privacy/cookie.
- Endpoint `/gdpr/policy/version` per consultare e aggiornare le versioni.
- URL e data pubblicazione sempre disponibili per audit.

## 12. Log e Limitazione Azioni Amministrative

- Tutte le azioni di modifica/cancellazione dati da parte di admin vengono loggate (`/gdpr/admin/log`, `/gdpr/admin/logs`).
- Audit trail dedicato per accessi e operazioni amministrative.
- Possibilità di limitare e monitorare le operazioni sensibili.

---

## Checklist Compliance

- [x] Consenso esplicito e revocabile
- [x] Export dati utente
- [x] Cancellazione sicura
- [x] Audit trail completo
- [x] Crittografia dati
- [x] Retention configurabile
- [x] Privacy by design
- [x] Documentazione e trasparenza

---

## Come Validare la Compliance

1. Consulta la documentazione in `docs/`.
2. Esegui i test automatici (`pytest` su plugin GDPR e Audit).
3. Verifica la configurazione in `.env`.
4. Simula export/cancellazione tramite API e frontend.
5. Consulta i log di audit e backup.

---

> Questo stack è pensato per essere facilmente auditabile, estendibile e conforme alle best practice GDPR. Per esigenze specifiche, personalizza i plugin e aggiorna la documentazione.
