from pydantic import BaseModel, Field

class ScoreResult(BaseModel):
  example_id:str = Field(default = "None")
  score: int = Field(...)
  judgement: str = Field(...)