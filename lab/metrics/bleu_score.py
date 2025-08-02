from nltk.util import ngrams
from collections import Counter
import numpy as np

def brevity_penalty(reference, candidate):
    ref_length = len(reference)
    cd_length = len(candidate)

    if ref_length > cd_length:
        BP = 1
    else:
        penalty = 1 - (ref_length / cd_length)
        BP = np.exp(penalty)

    return BP

def clipped_precision(reference, candidate, n_gram= 4):

    clipped_precision_scores = []

    for i in range(1, n_gram+1):
        candidate_n_gram = Counter(ngrams(candidate, i))
        reference_n_gram = Counter(ngrams(reference, i))

        c = sum(candidate_n_gram.values())

        for ref_n_gram, freq in reference_n_gram.items():
            if ref_n_gram in candidate_n_gram:
                reference_n_gram[ref_n_gram] = min(freq, candidate_n_gram[ref_n_gram])
            else:
                reference_n_gram[ref_n_gram] = 0

        clipped_precision_scores.append(sum(reference_n_gram.values()) / c)

    weights = [1/n_gram] * n_gram

    s = np.array([w_i * np.log(p_i) for w_i, p_i in zip(weights, clipped_precision_scores)])
    s = np.exp(np.sum(s))

    return s


def bleu_score(reference, candidate, n_gram = 4):
    BP = brevity_penalty(reference, candidate)
    precision = clipped_precision(reference, candidate, n_gram)

    return BP * precision


if __name__ == '__main__':
    print(bleu_score('hello world', 'hello teacher'))
