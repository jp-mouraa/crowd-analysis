# Here all crowd datasets from the main sources will be downloaded

# - [Crowd Counting - Mall](https://www.kaggle.com/datasets/fmena14/crowd-counting) 
# - [Crowd Counting - Mall V2](https://personal.ie.cuhk.edu.hk/~ccloy/downloads_mall_dataset.html)
# - [Human Tracking & Object Detection Dataset](https://www.kaggle.com/datasets/trainingdatapro/people-tracking/data?select=images)

import kagglehub
import shutil
import os

datasets_config = [("fmena14/crowd-counting", "data/raw/Mall"), 
                 ("trainingdatapro/people-tracking", "data/raw/HumanTracking")]

for dataset_path in datasets_config:
    # download dataset
    path = kagglehub.dataset_download(dataset_path[0])
    print("Dataset downloaded to:", path)

    # destination folder
    dest = dataset_path[1]

    if not os.path.exists(dest):
        shutil.copytree(path, dest)
    else:
        print("The destination folder already exists!")

    print("Dataset in:", dest)