from pydantic import BaseModel
from datetime import datetime

class TelemetryEvent(BaseModel):
    cpu: float
    latency: float
