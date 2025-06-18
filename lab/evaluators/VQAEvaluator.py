from typing import Type, List, Dict, Union, Lieteral, Callable, Any
from abc import ABC, abstracmethod
from evaluate import load as load_metric

class VQAMetric(ABC):
    @abstracmethod
    def evaluate(self, reference: Union[str, List[str]], prediction: Union[str, List[str]], **kwargs)-> Dict[str, float]:
        pass 


class BleuMetric(VQAMetric):
    def __init__(self, model_name: str):
        self.model_name = model_name 
    
    def evaluate(self, reference: Union[str, List[str]], prediction: Union[str, List[str]],weights: List[float] | None = None, \
                 metric_type: List[str] = None) -> Dict[str, float]:
        # Implement the BLEU score calculation here
        pass 

class RougeMetric(VQAMetric):
    def __init__(self, model_name: str):
        self.model_name = model_name 
    
    def evaluate(self, reference: Union[str, List[str]], prediction: Union[str, List[str]], metric_type: List[str] = None) -> Dict[str, float]:
        # Implement the ROUGE score calculation here
        pass    

class F1Metric(VQAMetric):
    def __init__(self, model_name: str):
        self.model_name = model_name 
    
    def evaluate(self, reference: Union[str, List[str]], prediction: Union[str, List[str]]) -> Dict[str, float]:
        # Implement the F1 score calculation here
        pass
class METEORMetric(VQAMetric):
    def __init__(self, model_name: str):
        self.model_name = model_name 
    
    def evaluate(self, reference: Union[str, List[str]], prediction: Union[str, List[str]]) -> Dict[str, float]:
        # Implement the METEOR score calculation here
        pass


class BertScoreMetric(VQAMetric):
    def __init__(self, model_name: str, embedding_model: str = 'bert-base-uncased', lang: str = 'en'):
        self.embedding_model = embedding_model
        self.lang = lang
        self.model_name = model_name 
    
    def evaluate(self, reference: Union[str, List[str]], prediction: Union[str, List[str]], lang: str = 'en') -> Dict[str, float]:
        # Implement the BERTScore calculation here
        pass
class LLMasJudgeMetric(VQAMetric):
    def __init__(self, model_name: str, judge_model: Callable, judgement_prompt: str = "Is the answer correct? Answer with 'yes' or 'no'.") -> None:

        self.model_name = model_name 
    
    def evaluate(self, reference: Union[str, List[str]], prediction: Union[str, List[str]], judge_model: Callable) -> Dict[str, float]:
        # Implement the LLM as judge evaluation here
        pass

class ANLSMetric(VQAMetric):
    def __init__(self, model_name: str, **kwargs):
        self.model_name = model_name 
    
    def evaluate(self, reference: Union[str, List[str]], prediction: Union[str, List[str]]) -> Dict[str, float]:
        # Implement the ANLS score calculation here
        pass

class VQAEvaluator:
    def __init__(self, model_name:str):
        self.model_name = model_name
        self.metrics: Dict[str, Type[VQAMetric]] | None = None
    def setup(self, config: Dict[str, Any]) -> None:
        '''{
            "Bleu":BleuMetric(model_name),
            "Rouge": RougeMetric(model_name),
            "F1 Score": F1Metric(model_name),
            "METEOR": METEORMetric(model_name),
            "BertScore":BertScoreMetric(model_name),
            "LLM As Judge": LLMasJudgeMetric(model_name)
        }'''

        def default_setup():
            return {
            "Bleu": BleuMetric(self.model_name),
            "Rouge": RougeMetric(self.model_name),
            "F1": F1Metric(self.model_name),
            }

        

    def run_experiment(self, reference: Union[str, List[str]], prediction: Union[str, List[str]]) -> Dict[str, float]:
        results = {}
        for metric in self.metrics:
            pass 
