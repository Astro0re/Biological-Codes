# Genotype identification software using computer vision

import pandas as pd
import numpy as nu 
import tensorflow as tf
import kueras 

# Genotype identification using sequence identification 

class __main__:
    def __init__(self):
        pass
# Import dataset 
# Source Hugging Face [Docty](https://huggingface.co/Docty)
global df
df = pd.read_parquet("hf://datasets/Docty/Blood-Cells/data/train-00000-of-00001.parquet") 
print(df.head())
# Dataset conatins 8 labels for diffrent categories of blood cells
# 0 : Monocytes
# 1 : ig
# 2 : Neutrophils
# 3 : Basophils
# 4 : Lymphocytes
# 5 : Erythroblasts
# 6 : Eosinophils
# 7 : Platlets


# Filter out only Erythrocytes (Red Blood cells)
global Eryth 
Eryth = df[df['label'] == 5]

# Transform the image data into a numpy array

# Train Model on the Erythrocytes

# Using a simple CNN model for image classification


# bit classification of Erythrocytes
global bit_count
bit_count = []

#  Cerate new classes of Erythrocytes using bit count as a basis (those below a certain bit count are considered unhealthy)
def sorting():
    if bit_count < __ :
        df['label'] = 'Grade A'
    elif bit_count < __ :
        df['label'] = 'Grade B'
    elif bit_count < __ :
        df['label'] = 'Grade C'
    else:
        df['label']  = 'Grade Unkown'