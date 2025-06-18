import numpy as np
from nltk.util import ngrams
from collections import Counter, defaultdict
from typing import List

def ngram_gen(chain: List[str], n_gram:int=4):
    chain_np = np.array(chain)
    num_ngrams = chain_np.shape[0] - n_gram + 1

    if num_ngrams <= 0:
        return np.array([])
    return np.array([chain_np[i:i+n_gram] for i in range(num_ngrams)])


def rouge_score_n(reference: List[str], candidate: List[str], n_gram: int = 4):

    ref_n_grams = defaultdict(int)
    ref_n_grams.update(Counter(ngrams(reference, n_gram)))
    cd_n_grams = defaultdict(int)
    cd_n_grams.update(Counter(ngrams(candidate, n_gram)))

    return sum(min(cd_n_grams[n_gram], ref_n_grams[n_gram]) for n_gram in ref_n_grams)

def lcs(reference, candidate):

    dp = np.zeros((len(reference), len(candidate)), dtype=np.int32)
    m, n = dp.shape

    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                continue
            if reference[i] == candidate[j]:
                dp[i, j] = dp[i-1, j-1]+1

            dp[i, j] = np.maximum.reduce(dp[i, j],dp[i, j-1], dp[i-1, j])

    return int(dp[m-1, n-1])


def rouge_score_l_recall(reference: List[str], candidate: List[str]):
    return lcs(reference, candidate) / len(reference)

def rouge_score_l_precision(reference: List[str], candidate: List[str]):
    return lcs(reference, candidate) / len(candidate)

def rouge_score_l_f1(reference: List[str], candidate: List[str]):
    tp, tp_fp, tp_fn = lcs(reference, candidate), len(reference), len(candidate)

    precision = tp / tp_fp
    recall = tp / tp_fn

    return 2.0 * ((precision * recall) / (precision + recall + 1e-8))


if __name__ == '__main__':
    print(lcs('abb', 'abb'))


