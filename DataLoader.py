# Here all crowd datasets from the main sources will be downloaded

# - [Crowd Counting - Mall](https://www.kaggle.com/datasets/fmena14/crowd-counting) 
# - [Crowd Counting - Mall V2](https://personal.ie.cuhk.edu.hk/~ccloy/downloads_mall_dataset.html)
# - [Human Tracking & Object Detection Dataset](https://www.kaggle.com/datasets/trainingdatapro/people-tracking/data?select=images)

import kagglehub
import shutil
import os

# download dataset
path = kagglehub.dataset_download("trainingdatapro/people-tracking")
print("Dataset downloaded to:", path)

# destination folder
dest = "data/datacrowd-analysis/Human"

if not os.path.exists(dest):
    shutil.copytree(path, dest)
else:
    print("The destination folder already exists!")

print("Dataset in:", dest)