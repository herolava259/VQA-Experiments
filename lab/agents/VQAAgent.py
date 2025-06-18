


class VQAAgent:
    def __init__(self, model_fn, system_prompt):
        self.model_fn = model_fn 
        self.system_prompt = system_prompt 
    
    def __call__(self, question, image, task_prompt=None):

        if not task_prompt:
            final_prompt = question 
        else:
            final_prompt = task_prompt.format(question=question)
        
        response = self.model_fn(system = self.system_prompt,
                                 user = final_prompt)
        
        return response
    