import React, { useState } from "react";

const API_URL = "http://localhost:8000/test";

export default function SecurityDashboard() {
  const [rateResult, setRateResult] = useState("");
  const [botResult, setBotResult] = useState("");
  const [headersResult, setHeadersResult] = useState("");

  const testRateLimit = async () => {
    let results: number[] = [];
    for (let i = 0; i < 105; i++) {
      const res = await fetch(API_URL);
      results.push(res.status);
    }
    setRateResult(results.join(", "));
  };

  const testBotDetection = async () => {
    const res = await fetch(API_URL, { headers: { "User-Agent": "python-requests" } });
    setBotResult(res.status.toString());
  };

  const testSecurityHeaders = async () => {
    const res = await fetch(API_URL);
    const headers = [
      "X-Frame-Options",
      "X-Content-Type-Options",
      "Referrer-Policy",
      "Content-Security-Policy",
      "Strict-Transport-Security"
    ];
    let out = headers.map(h => `${h}: ${res.headers.get(h)}`).join("\n");
    setHeadersResult(out);
  };

  return (
    <div style={{ padding: "2em" }}>
      <h1>Security Dashboard</h1>
      <section>
        <h2>Rate Limiting</h2>
        <button onClick={testRateLimit}>Test Rate Limit</button>
        <pre>{rateResult}</pre>
      </section>
      <section>
        <h2>Bot Detection</h2>
        <button onClick={testBotDetection}>Test Bot Detection</button>
        <pre>{botResult}</pre>
      </section>
      <section>
        <h2>Security Headers</h2>
        <button onClick={testSecurityHeaders}>Test Security Headers</button>
        <pre>{headersResult}</pre>
      </section>
    </div>
  );
}
