from fastapi import FastAPI
from pydantic import BaseModel
import redis
import numpy as np
import json

app = FastAPI()

r = redis.Redis(host="redis", port=6379, decode_responses=True)

WINDOW_SIZE = 20

class TelemetryEvent(BaseModel):
    cpu: float
    latency: float

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/ingest")
def ingest(event: TelemetryEvent):
    r.lpush("cpu", event.cpu)
    r.lpush("latency", event.latency)

    r.ltrim("cpu", 0, WINDOW_SIZE - 1)
    r.ltrim("latency", 0, WINDOW_SIZE - 1)

    cpu_vals = list(map(float, r.lrange("cpu", 0, -1)))
    latency_vals = list(map(float, r.lrange("latency", 0, -1)))

    if len(cpu_vals) < WINDOW_SIZE:
        return {
            "status": "collecting_baseline",
            "samples": len(cpu_vals)
        }

    cpu_mean, cpu_std = np.mean(cpu_vals), np.std(cpu_vals)
    lat_mean, lat_std = np.mean(latency_vals), np.std(latency_vals)

    cpu_z = (event.cpu - cpu_mean) / (cpu_std + 1e-6)
    lat_z = (event.latency - lat_mean) / (lat_std + 1e-6)

    anomaly = abs(cpu_z) > 3 or abs(lat_z) > 3

    return {
        "status": "processed",
        "cpu": event.cpu,
        "latency": event.latency,
        "cpu_zscore": round(cpu_z, 2),
        "latency_zscore": round(lat_z, 2),
        "anomaly": anomaly
    }

