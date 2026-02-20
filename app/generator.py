import time
import random
import requests
from datetime import datetime

API_ENDPOINT = "http://aiops-api:8000/ingest"

SOURCES = ["radar-1", "radar-2", "border-cam-3"]
ZONES = ["sector-1", "sector-2", "sector-3"]

def generate_event(anomalous=False):
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "source": random.choice(SOURCES),
        "event_type": "network_activity",
        "signal_strength": random.uniform(0.2, 0.5) if not anomalous else random.uniform(0.9, 1.0),
        "packet_rate": random.randint(100, 300) if not anomalous else random.randint(1500, 3000),
        "geo_zone": random.choice(ZONES),
        "confidence": random.uniform(0.7, 0.95)
    }

while True:
    event = generate_event(anomalous=random.random() < 0.05)
    try:
        r = requests.post(API_ENDPOINT, json=event, timeout=2)
        print("Sent:", r.status_code)
    except Exception as e:
        print("Send failed:", e)
    time.sleep(1)

