import requests

def test_root():
    r = requests.get("http://localhost:8080/")
    assert r.status_code == 200
    assert r.json()["message"] == "AI Ops Service Running"

