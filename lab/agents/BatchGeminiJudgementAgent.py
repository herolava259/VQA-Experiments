from lab.utilties.ScoreResult import ScoreResult


class BatchGeminiJudgementAgent:
    def __init__(self, api_key: str, model_type="gemini-1.5-flash"):
        self.api_key = api_key
        self.judgement_prompt = BATCH_JUDGE_PROMPT
        self.model_type = model_type
        self.gemini_llm_client = genai.Client(api_key=api_key)

    def __execute__(self, evaluations: list[dict]):
        formatted_prompt = self.judgement_prompt.format(
            list_of_evaluations=",\n".join([
                f"""<Item>{{
                    "ExampleId": "{item["example_id"]}"
                    "Question": "{item['question']}",
                    "Context": "{item['context']}",
                    "Answer": "{item['answer']}",
                    "Referenced Answer": "{item['reference_answer']}"
                }}</Item>""" for item in evaluations
            ])
        )

        response = self.gemini_llm_client.models.generate_content(
            model=self.model_type,
            contents=formatted_prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "Score": {"type": "integer"},
                            "Judgement": {"type": "string"},
                            "ExampleId": {"type": "string"}
                        },
                        "required": ["Score", "Judgement", "ExampleId"]
                    }
                },
            },
        )

        parsed_results = response.parsed

        return [
            ScoreResult(score=item["Score"], judgement=item["Judgement"], example_id= item["ExampleId"])
            for item in parsed_results
        ]
