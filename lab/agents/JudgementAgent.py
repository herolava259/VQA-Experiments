from google import genai 
import os
from pydantic import BaseModel, Field
import os 

class ScoreResult(BaseModel):
  score: int = Field(...)
  judgement: str = Field(...)


class GeminiJudgementAgent:
  def __init__(self, api_key: str, model_type="gemini-1.5-flash"):

    self.api_key = api_key
    self.judgement_prompt = JUDGE_PROMPT
    self.model_type = model_type
    self.gemini_llm_client =  genai.Client(api_key=api_key)
  
  def __excute__(self, context, question, answer, reference_answer):
    formatted_prompt = self.judgement_prompt.format(context=context, question=question, answer=answer, reference_answer=reference_answer)
    response = self.gemini_llm_client.models.generate_content(
      model=self.model_type,
      contents = formatted_prompt,
      config={
          "response_mime_type": "application/json",
          "response_schema": {
              "type": "object",
              "properties": {
                  "Score": {"type": "integer"},
                  "Judgement": {"type": "string"},
              },
          },
      },
    )

    parsed_result = response.parsed
    return ScoreResult(score=parsed_result["Score"], judgement=parsed_result["Judgement"])