# TextHawk: Exploring Efficient Fine-Grained Perception of Multimodal Large Language Models

![examples](figures/examples.png)

## Introduction

*TextHawk* is a Multimodal Large Language Model (MLLM) specifically designed for document-oriented tasks, while preserving the general capabilities. It is aimed to explore efficient fine-grained perception by designing four dedicated components:

- ReSampling and ReArrangement (ReSA)
- Scalable Positional Embeddings (SPEs)
- Query Proposal Network (QPN)
- Multi-Level Cross-Attention (MLCA)

## DocGemini

We create a new instruction-tuning dataset *DocGemini* for document-oriented tasks by enriching the multimodal document data with Gemini Pro. Each data sample contains:

- A brief summary of the document topics.
- Short QA pairs, up to 10.
- Insights behind each answer.

DocGemini consists of 30K images and 195K QA pairs with insights.

## Benchmarks

| Model | ViT<br>(Params.) | MME<br>Perception | MMB<br>dev | SEED<br>Image | GQA | DocVQA | ChartQA | InfoVQA | TabFact | WTQ | $\textbf{RefCOCO}^\textbf{val}$ | $\textbf{RefCOCO}^\textbf{test-A}$ | $\textbf{RefCOCO}^\textbf{test-B}$ |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
Donut | Swin-B<br>(0.1B) | - | - | - | - | 67.5 | 41.8 | 11.6 | 54.6 | 18.8 | - | - | -
Pix2Struct | - | - | - | - | - | **76.6** | 58.6 | 40.0 | - | - | - | - | - |
InternLM-XC | EVA-G<br>(1B) | **1528.4** | **74.8** | 66.1 | - | - | - | - | - | - | - | - | -
LLaVA-1.5-7B | CLIP-L<br>(0.3B) | 1510.7| 65.2 | - | 62.0 | - | - | - | - | - | - | - | -
Shikra-7B | CLIP-L<br>(0.3B) | - | 58.8 | - | - | - | - | - | - | - | 87.0 | <ins>91.1</ins> | 81.8
Qwen-VL-Chat | CLIP-G<br>(2B) | 1487.6 | 60.6 | 65.4 | 57.5 | 62.6 | 66.3 | - | - | - | **88.6** | **92.3** | **84.5**
Monkey | CLIP-G<br>(2B) | - | 59.3 | - | 60.7 | 66.5 | 65.1 | 36.1 | - | 25.3 | - | - | -
UReader | CLIP-L<br>(0.3B) | - | - | - | - | 65.4 | 59.3 | 42.2 | 67.6 | 29.4 | - | - | -
TextMonkey | CLIP-G<br>(2B) | - | - | - | - | 73.0 | **66.9** | - | - | 31.9 | - | - | -
$\textbf{TextHawk}^*$ | SigLIP-SO<br>(0.4B) | <ins>1520.9</ins> | 73.0 | **69.2** | **64.7** | <ins>73.6</ins> | 64.0 | <ins>47.3</ins> | <ins>70.7</ins> | <ins>33.5</ins> | <ins>87.3</ins> | 90.9 | <ins>83.3</ins>
$\textbf{TextHawk}$ | SigLIP-SO<br>(0.4B) | 1500.0 | <ins>74.6</ins> | **69.2** | <ins>64.6</ins> | **76.4** | <ins>66.6</ins> | **50.6** | **71.1** | **34.7** | 87.2 | 90.8 | 82.5

> Note: $\textbf{TextHawk}^*$ is fine-tuned without the DocGemini.
