# HSLN-Joint-Sentence-Classification
This is the source code for the paper that will be at EMNLP 2018: [Jin, Di, and Peter Szolovits. "Hierarchical Neural Networks for Sequential Sentence Classification in Medical Scientific Abstracts." arXiv preprint arXiv:1808.06161 (2018)](https://arxiv.org/abs/1808.06161).

Abstract:

>Prevalent models based on artificial neural network (ANN) for sentence classification often classify sentences in isolation without considering the context in which sentences appear. This hampers the traditional sentence classification approaches to the problem of sequential sentence classification, where structured prediction is needed for better overall classification performance. In this work, we present a hierarchical sequential labeling network to make use of the contextual information within surrounding sentences to help classify the current sentence. Our model outperforms the state-of-the-art results by 2%-3% on two benchmarking datasets for sequential sentence classification in medical scientific abstracts.

## Requirements:

* Tensorflow=1.8
* sklearn>0.18
* python=2.7
* numpu

## Data
### PubMed
The original data comes from: https://github.com/Franck-Dernoncourt/pubmed-rct. If you carefully look at the original data, you can find that in the end of some abstracts, there are some sentences that indicate the funding source of the research and are not relevant to the paper content, and these sentences are labeled as BACKGROUND type, which I think is not that reasonable. So I removed these sentences using the script "pubmed_data_cleaning.py". The command to run this script could be:

```
python pubmed_data_cleaning.py IN_FILE_PATH OUT_FILE_PATH
```

I have put the cleaned data files for PubMed-20k dataset inside the folder "data/PubMed-20k-RCT" for references.

### NICTA-PIBOSO
The original data is from the [ALTA-NICTA Challenge](https://www.kaggle.com/c/alta-nicta-challenge2), but it is hard to download from it. So I shared this dataset [here](https://github.com/jind11/NICTA-PIBOSO-Dataset). If you carefully look at this dataset, you will find that some sentences have multiple labels, but in our model scenerios, any sentence only accepts one label. So I assigned the label to the sentences that have multiple labels by majority voting, where I first obtained the statistics for each label, then within the label candidates, I chose the label that appears most times. For example, one sentence has three labels: A, B, and C, and in the whole train set, label A appears most frequently, so I chose label A for this sentence. I have put the processed data in the folder "data/nicta_piboso".

### Embeddings
The embeddings I mainly used is from [here](http://bio.nlplab.org/).

## Usage
1. [DO NOT MISS THIS STEP] Build vocab from the data and extract trimmed embedding vectors according to the config in model/config.py.

```
python build_data.py
```
2. Train the model with

```
python train.py
```

## Words in the end
This project is licensed under the terms of the MIT license. If used for research, citation would be appreciated. If you have any questions, feel free to post them in the issues. 
