from pydantic import BaseModel, Field
from typing import Dict, Optional


# ===========================
# Input for /predict
# ===========================
class FlowSchema(BaseModel):
    flow_id: Optional[str] = Field(default=None, alias="Flow ID")
    features: Dict[str, float]


# ===========================
# Input for /feedback or /learn
# ===========================
class FeedbackSchema(BaseModel):
    flow_id: str = Field(..., alias="Flow ID")
    true_label: str
    features: Dict[str, float]

    class Config:
        allow_population_by_field_name = True


# ===========================
# Output for /predict
# ===========================
class PredictionResponse(BaseModel):
    flow_id: Optional[str]
    prediction: str
    confidence: float
    latency_ms: float   # <-- BỔ SUNG BẮT BUỘC
#