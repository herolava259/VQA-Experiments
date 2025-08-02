import string
import nltk
import spacy
from nltk.corpus import gutenberg, stopwords, wordnet
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer


def ensure_nltk_resources():
    import nltk
    resources = [
        'punkt',
        'stopwords',
        'wordnet',
        'omw-1.4'
    ]

    for resource in resources:
        try:
            nltk.data.find(resource)
        except LookupError:
            nltk.download(resource)


def load_vn_stop_words():
    import requests
    url = "https://raw.githubusercontent.com/stopwords-iso/stopwords-vi/master/stopwords-vi.txt"
    response = requests.get(url)
    return set(response.text.strip().split("\n"))

vn_stop_words = load_vn_stop_words()

def filter_out_punctuation_and_stopwords(text: str, keep_punctuation=False, keep_stop_word=False):

    if not keep_punctuation:
        punctuations = set(string.punctuation)
        text = ''.join(w for w in text if w not in punctuations)

    if not keep_stop_word:
        text = ''.join(w for w in text if w not in vn_stop_words)

    return text

from abc import ABC, abstractmethod
class VNTokenizer(ABC):

    @abstractmethod
    def tokenize(self, txt: str, **kwargs):
        pass


from spacy.lang.vi import Vietnamese
from typing import List

class SpacySentencizer(VNTokenizer):

    def __init__(self):
        self.nlp = Vietnamese()
        self.nlp.add_pipe("sentencizer")


    def tokenize(self, txt: str, len_per_paragraph = 1024, **kwargs) -> List[str]:

        end_signs = {'.', '?', '!', ":"}

        paragraphs = []
        prev, count = 0, 1
        prev_sent_pos = 0

        for i, letter in enumerate(txt):
            if letter in end_signs:
                prev_sent_pos = i
                count += 1
            if count == 1:
                continue
            if i - prev + 1 > len_per_paragraph:
                paragraphs.append(self.nlp(txt[prev:prev_sent_pos+1]))
                prev_sent_pos += 1
                prev = i + 1
                count = 1

        if prev < len(txt):
            paragraphs.append(self.nlp(txt[prev]))

        without_stop_word = False
        without_punctuation = False

        if kwargs.get("without_stop_word", None):
            without_stop_word = kwargs["without_stop_word"]

        if kwargs.get("without_punctuation", None):
            without_punctuation = kwargs["without_punctuation"]


        if not without_punctuation and not without_stop_word:
            return paragraphs
        from functools import partial
        filter_fn = partial(filter_out_punctuation_and_stopwords, keep_punct = not without_punctuation, keep_stop_word = not without_stop_word)

        return [filter_fn(p) for p in paragraphs]

from pyvi import ViTokenizer

class PyViSentencizer(VNTokenizer):
    def tokenize(self, txt: str, len_per_paragraph = 1024, **kwargs) -> List[str]:
        end_signs = {'.', '?', '!', ":"}

        paragraphs = []
        prev, count = 0, 1
        prev_sent_pos = 0

        for i, letter in enumerate(txt):
            if letter in end_signs:
                prev_sent_pos = i
                count += 1
            if count == 1:
                continue
            if i - prev + 1 > len_per_paragraph:
                paragraphs.append(ViTokenizer.tokenize(txt[prev:prev_sent_pos + 1]))
                prev_sent_pos += 1
                prev = i + 1
                count = 1

        if prev < len(txt):
            paragraphs.append(ViTokenizer.tokenize(txt[prev]))

        without_stop_word = False
        without_punctuation = False

        if kwargs.get("without_stop_word", None):
            without_stop_word = kwargs["without_stop_word"]

        if kwargs.get("without_punctuation", None):
            without_punctuation = kwargs["without_punctuation"]

        if not without_punctuation and not without_stop_word:
            return paragraphs
        from functools import partial
        filter_fn = partial(filter_out_punctuation_and_stopwords, keep_punct=not without_punctuation,
                            keep_stop_word=not without_stop_word)

        return [filter_fn(p) for p in paragraphs]

import underthesea

class UndertheseaTokenizer(VNTokenizer):
    def tokenize(self, txt: str, **kwargs):

        paragraphs = underthesea.word_tokenize(txt)

        without_stop_word = False
        without_punctuation = False

        if kwargs.get("without_stop_word", None):
            without_stop_word = kwargs["without_stop_word"]

        if kwargs.get("without_punctuation", None):
            without_punctuation = kwargs["without_punctuation"]

        if not without_punctuation and not without_stop_word:
            return paragraphs

        from functools import partial
        filter_fn = partial(filter_out_punctuation_and_stopwords, keep_punct=not without_punctuation,
                            keep_stop_word=not without_stop_word)

        return [filter_fn(p) for p in paragraphs]