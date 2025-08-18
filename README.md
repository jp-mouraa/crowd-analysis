# crowd-analysis
The goal of the project is to use Large Language Models (LLM) to describe images of crowds.

## Algorithm
...

## Datasets
[Roboflow]
- [Crowd Counting Dataset](https://universe.roboflow.com/crowd-dataset/crowd-counting-dataset-w3o7w)

[Kaggle]
- [Crowd Counting - Mall](https://www.kaggle.com/datasets/fmena14/crowd-counting) 
- [Crowd Counting - Mall V2](https://personal.ie.cuhk.edu.hk/~ccloy/downloads_mall_dataset.html)
- [Human Tracking & Object Detection Dataset](https://www.kaggle.com/datasets/trainingdatapro/people-tracking/data?select=images)

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

obs: download frames from Kaggle dataset and storage in ../data/images/CrowdCountingKaggle/frames/

## Useful links
[Clip]\
https://github.com/openai/CLIP?tab=readme-ov-file
https://github.com/mlfoundations/open_clip

[HuggingFace]\
https://huggingface.co/Salesforce/blip-image-captioning-large 

[PyTorch]\
https://pytorch.org/get-started/locally/