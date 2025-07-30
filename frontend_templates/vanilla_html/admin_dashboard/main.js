const API_URL = "http://localhost:8000/gdpr";

function fetchAdminLogs() {
  fetch(`${API_URL}/admin/logs`)
    .then(res => res.json())
    .then(logs => {
      const ul = document.getElementById('admin-logs');
      ul.innerHTML = '';
      logs.forEach(log => {
        const li = document.createElement('li');
        li.textContent = `Admin ${log.admin_id} - ${log.action} su user ${log.target_user_id || '-'} (${log.details}) [${log.created_at}]`;
        ul.appendChild(li);
      });
    });
}

function logAdminAction() {
  const admin_id = parseInt(document.getElementById('admin_id').value);
  const action = document.getElementById('action').value;
  const target_user_id = parseInt(document.getElementById('target_user_id').value) || null;
  const details = document.getElementById('details').value;
  fetch(`${API_URL}/admin/log`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ admin_id, action, target_user_id, details })
  })
    .then(res => res.json())
    .then(log => {
      alert('Azione registrata!');
      fetchAdminLogs();
    });
}
