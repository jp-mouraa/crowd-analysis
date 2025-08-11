# crowd-analysis
The goal of the project is to use Large Language Models (LLM) to describe images of crowds.

## Algorithm
...

## Datasets

- [https://universe.roboflow.com/crowd-dataset/](https://universe.roboflow.com/crowd-dataset/crowd-counting-dataset-w3o7w)
- [Crowd Counting Dataset - Kaggle](https://www.kaggle.com/datasets/trainingdatapro/crowd-counting-dataset)

## Crowd Counting Framework
find a good name for this

## Environment Configuration
$ conda create -n crowd-analysis python=3.13

$ conda activate crowd-analysis

$ conda install --yes -c pytorch pytorch=1.7.1 torchvision 
cudatoolkit=11.0 **or** pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128

$ pip install ftfy regex 

$ cd ./crowd-analysis

$ pip install git+https://github.com/openai/CLIP.git

## Useful links

https://pytorch.org/get-started/locally/