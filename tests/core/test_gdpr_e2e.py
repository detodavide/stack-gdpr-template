"""
End-to-end tests for GDPR flows: consent, export, deletion, breach notification.
Run with: pytest tests/core/test_gdpr_e2e.py
"""
import requests
import pytest

API_URL = "http://localhost:8000/api/gdpr"
USER_TOKEN = "test-user-token"  # Replace with a valid token if needed
HEADERS = {"Authorization": f"Bearer {USER_TOKEN}"}

@pytest.mark.order(1)
def test_gdpr_consent():
    resp = requests.post(f"{API_URL}/consent", json={"consent": True}, headers=HEADERS)
    assert resp.status_code == 200
    assert resp.json().get("status") == "success"

@pytest.mark.order(2)
def test_gdpr_export():
    resp = requests.get(f"{API_URL}/my-data", headers=HEADERS)
    assert resp.status_code == 200
    assert "user" in resp.json()

@pytest.mark.order(3)
def test_gdpr_delete():
    resp = requests.delete(f"{API_URL}/delete-account", headers=HEADERS)
    assert resp.status_code == 200
    assert resp.json().get("status") == "deleted"

@pytest.mark.order(4)
def test_gdpr_breach():
    resp = requests.post(f"{API_URL}/breach", json={"description": "Test breach"}, headers=HEADERS)
    assert resp.status_code == 200
    assert resp.json().get("notified") is True
