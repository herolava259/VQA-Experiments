from bleu_score import bleu_score
from rouge_score import rouge_score_n
from typing import List

def f1_score(candidate: List[str], reference: List[str], n_gram=4):
    precision = bleu_score(candidate, reference, n_gram)
    recall = rouge_score_n(reference, candidate, n_gram)

    return (2.0 * precision * recall) / (precision + recall + 1e-8)

