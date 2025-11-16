from pydantic import BaseModel, Field
from typing import Dict, Optional

class FlowSchema(BaseModel):
    flow_id: Optional[str] = Field(default=None, alias="Flow ID")
    features: Dict

class FeedbackSchema(BaseModel):
    flow_id: str = Field(..., alias="Flow ID")
    true_label: str
    features: Dict

    class Config:
        allow_population_by_field_name = True
