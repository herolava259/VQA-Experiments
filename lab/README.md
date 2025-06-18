# Evaluation Experiment for Visual Question Answering Task on Gemini Flash 1.5

## I. Models for Comparasion 
- Gemini 1.5 Flash. [Report](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf)
- Chat GPT 
<!-- - LayoutLMV3 -->
<!-- - Tesseract (for OCR Task) -->
- DoNuT(Document Understanding Transformer). [Paper](https://arxiv.org/pdf/2111.15664)
<!-- - CNN-GRU
- Intern-VL2
- ViT5-base
- Pho-T5 -->
## II. Metrics 
- BLEU: 1-4 ngrams. [Usage-with-HuggingFace](https://huggingface.co/spaces/evaluate-metric/bleu)
- F1: Precision: BLEU, Recall: ROUGE2
- Meteor (update later). [Paper](https://aclanthology.org/W05-0909.pdf)
- BertScore: using default bert model (bert-base-uncased) | [Paper](https://openreview.net/pdf?id=SkeHuCVFDr) | [Article](https://medium.com/@abonia/bertscore-explained-in-5-minutes-0b98553bfb71) | [Github](https://github.com/Tiiiger/bert_score) | [Usage](https://colab.research.google.com/gist/Abonia1/26c13b7034e85ec1dbe29c2fa0d07242/bertscore-demo.ipynb) | [Usage-With-HuggingFace](https://huggingface.co/spaces/evaluate-metric/bertscore)
- LLM As Judge: Using GPT4o-Mini. [Article-1](https://huggingface.co/learn/cookbook/llm_judge) | [Article-2](https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method)
- Average Normalized Levenshtein Similarity (ANLS). [Paper](https://arxiv.org/pdf/2402.03848) | [Github](https://github.com/deepopinion/anls_star_metric/tree/main)
## III. Use Cases
- OCR 
- Image Captioning
- Document Understanding

## IV. Datasets
- [5CD-AI/Viet-ViTextVQA-gemini-VQA (Vietnamese)](https://huggingface.co/datasets/5CD-AI/Viet-ViTextVQA-gemini-VQA)
- [Vi-VLM/Vista (Vietnamese)](https://huggingface.co/datasets/Vi-VLM/Vista)
- [Custom Data](https://drive.google.com/drive/folders/1HlM4mTZB7sCw1YSzjOHp1wfwywj1G3ri?fbclid=IwY2xjawK_aPtleHRuA2FlbQIxMABicmlkETE3N0hzT0dBV2V4M2FSTVl3AR48ujFdrfbY7hexwGNWJ_8F2is6AUnMRUyvk5vxdFIqnawgkKzGQTLIyzmgTA_aem_P72kV8LDuxxDwxBzBJ_sYA)
- [Viet-OCR-VQA3](https://huggingface.co/datasets/5CD-AI/Viet-Vintext-gemini-VQA)
- [5CD-AI/Viet-Receipt-VQA (Vietnamese)](https://huggingface.co/datasets/5CD-AI/Viet-Receipt-VQA)

## V. Notebook
- [Link here](https://colab.research.google.com/drive/1OH4CgqsChrjU-pBz8t9MsSzbv-CbyhLb?authuser=1&hl=vi#scrollTo=Q_7tq1lxqciX)

## Latest: Tools for Running Experiments

<!-- - [MLFlow](https://mlflow.org/)
- [WanDB](https://deep-learning-blogs.vercel.app/blog/mlops-wandb-integration)
- [AirFlow](https://medium.com/@mrunmayee.dhapre/ml-pipeline-in-airflow-71ca7e1f03ba)
- [ApacheBeam](https://cloud.google.com/blog/products/ai-machine-learning/dataflow-ml-innovations-on-apache-beam/) -->

## Reference Links