# Genotype identification software using computer vision

import pandas as pd
import numpy as nu 
import tensorflow as tf
import keras
from keras import layers, models, optimizers
from keras.utils import load_img, img_to_array, save_img
from keras.preprocessing.image import ImageDataGenerator


# Genotype identification using sequence identification 

class __main__:
    def __init__(self):
        pass
# Import dataset 
# Source Hugging Face [Docty](https://huggingface.co/Docty)
global df
df = pd.read_parquet("hf://datasets/Docty/Blood-Cells/data/train-00000-of-00001.parquet") 

# Filter out only Erythrocytes (Red Blood cells)
global Eryth 
Eryth =[]

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