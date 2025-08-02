from typing import Type, List, Dict, Union, Literal, Callable, Any
from abc import ABC, abstractmethod
from evaluate import load as load_metric

class VQAMetric(ABC):
    metric_name: str = "Bleu"
    description: str = "A metric for evaluating the quality of answers in Visual Question Answering tasks."

    @abstractmethod
    def evaluate(self, reference: Union[str, List[str]], prediction: Union[str, List[str]], **kwargs)-> Dict[str, float]:
        pass 


class BleuMetric(VQAMetric):
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.metric_name = "Bleu"
        self.metric_fn = load_metric("bleu")
    
    def evaluate(self, reference: Union[str, List[str]], prediction: Union[str, List[str]],weights: List[float] | None = None, \
                 metric_type: List[str] = None) -> Dict[str, float]:
        # Implement the BLEU score calculation here
        pass 

class RougeMetric(VQAMetric):
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.metric_name = "Rouge"
        self.metric_fn = load_metric("rouge")

    def evaluate(self, reference: Union[str, List[str]], prediction: Union[str, List[str]], metric_type: List[str] = None) -> Dict[str, float]:
        # Implement the ROUGE score calculation here
        pass
        

class F1Metric(VQAMetric):
    def __init__(self, model_name: str):
        self.model_name = model_name 
        self.metric_name = "F1"
        self.metric_precision = load_metric("bleu")
        self.metric_recall = load_metric("rouge")
        def calculate_f1(prediction, reference) -> float:

            if isinstance(prediction, str):
                prediction = [prediction]
            if isinstance(reference, str):
                reference = [reference]
            precision = self.metric_precision.compute(predictions=prediction, references=reference)
            recall = self.metric_recall.compute(predictions=prediction, references=reference)
            return 2 * (precision * recall) / (precision + recall + 1e-9) 
        self.f1_fn = calculate_f1
    def evaluate(self, reference: Union[str, List[str]], prediction: Union[str, List[str]]) -> Dict[str, float]:
        # Implement the F1 score calculation here
        return self.f1_fn(prediction, reference)

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
        
        if not config:
            self.metrics = default_setup()
        
        self.metrics = default_setup()
        

    def sequence_run_experiment(self, reference: Union[str, List[str]], prediction: Union[str, List[str]]) -> Dict[str, float]:
        results = {}
        for metric_name in self.metrics:
            results[metric_name] = self.metrics[metric_name].evaluate(reference, prediction)
        return results
    def parallel_run_experiment(self, reference: Union[str, List[str]], prediction: Union[str, List[str]]) -> Dict[str, float]:
        from concurrent.futures import ThreadPoolExecutor, as_completed
        
        results = {}
        with ThreadPoolExecutor() as executor:
            future_to_metric = {executor.submit(self.metrics[metric_name].evaluate, reference, prediction): metric_name for metric_name in self.metrics}
            for future in as_completed(future_to_metric):
                metric_name = future_to_metric[future]
                try:
                    results[metric_name] = future.result()
                except Exception as e:
                    results[metric_name] = str(e)
        return results
    
