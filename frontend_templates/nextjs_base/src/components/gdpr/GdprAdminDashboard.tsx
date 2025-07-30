import React, { useEffect, useState } from "react";

const API_BASE = "http://localhost:8000/api/gdpr";

export default function GdprAdminDashboard() {
  const [metrics, setMetrics] = useState<any>({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchMetrics() {
      const res = await fetch(`${API_BASE}/metrics`);
      if (res.ok) {
        setMetrics(await res.json());
      }
      setLoading(false);
    }
    fetchMetrics();
  }, []);

  if (loading) return <div>Loading GDPR metrics...</div>;

  return (
    <div style={{ padding: "2em" }}>
      <h1>GDPR Admin Dashboard</h1>
      <section>
        <h2>Consensi</h2>
        <p>Attivi: {metrics.consents_active}</p>
        <p>Scaduti: {metrics.consents_expired}</p>
      </section>
      <section>
        <h2>Export Dati</h2>
        <p>Richieste: {metrics.exports_requested}</p>
        <p>Completate: {metrics.exports_completed}</p>
      </section>
      <section>
        <h2>Cancellazioni</h2>
        <p>Richieste: {metrics.deletions_requested}</p>
        <p>Completate: {metrics.deletions_completed}</p>
      </section>
      <section>
        <h2>Data Breach</h2>
        <p>Notifiche inviate: {metrics.breach_notified}</p>
      </section>
      <section>
        <h2>Versioni Privacy Policy</h2>
        <ul>
          {(metrics.policy_versions || []).map((v: any) => (
            <li key={v.version}>Versione {v.version} - {v.date}</li>
          ))}
        </ul>
      </section>
      <section>
        <h2>Audit Trail</h2>
        <p>Operazioni registrate: {metrics.audit_logs_count}</p>
      </section>
      <section>
        <h2>Richieste DPO</h2>
        <p>Totali: {metrics.dpo_requests}</p>
        <p>Evase: {metrics.dpo_resolved}</p>
      </section>
    </div>
  );
}
