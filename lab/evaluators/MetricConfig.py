from pydantic import BaseModel, Field

class BaseMetricConfig(BaseModel):
    MetricName: str = Field(default="Bleu")

