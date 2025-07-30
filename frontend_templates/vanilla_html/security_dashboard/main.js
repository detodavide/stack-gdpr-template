const API_URL = "http://localhost:8000/test";

function testRateLimit() {
  let results = [];
  let requests = [];
  for (let i = 0; i < 105; i++) {
    requests.push(fetch(API_URL).then(r => results.push(r.status)));
  }
  Promise.all(requests).then(() => {
    document.getElementById('rate-limit-result').textContent = results.join(', ');
  });
}

function testBotDetection() {
  fetch(API_URL, { headers: { 'User-Agent': 'python-requests' } })
    .then(r => document.getElementById('bot-detect-result').textContent = r.status);
}

function testIPBlocking() {
  // Simulazione: mostra solo la configurazione, non può cambiare IP client da browser
  document.getElementById('ip-block-result').textContent = 'Set BLOCKED_IPS in .env e verifica da backend.';
}

function testSecurityHeaders() {
  fetch(API_URL)
    .then(r => {
      let headers = [
        'X-Frame-Options',
        'X-Content-Type-Options',
        'Referrer-Policy',
        'Content-Security-Policy',
        'Strict-Transport-Security'
      ];
      let out = headers.map(h => `${h}: ${r.headers.get(h)}`).join('\n');
      document.getElementById('headers-result').textContent = out;
    });
}
