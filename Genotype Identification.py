# Genotype identification software using computer vision

import os
import pandas as pd
import numpy as nu 
import tensorflow as tf
import keras
from keras import layers, models, optimizers
from keras.utils import load_img, img_to_array, save_img
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from PIL import image
import cv2


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

# Split data
x_train, x_test, y_train, y_test = train_test_split(Eryth['image'], Eryth['label'], test_size=0.2, random_state=42)
# Transform the image data into a numpy array
encode = Eryth['image']

image.open(encode)

# Train Model on the Erythrocytes (Sequential Processing)
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape(28,28)),
    tf.keras.layers.Dense()
])
# Using a simple CNN model for image classification
model.fit(Eryth)

# bit classification of Erythrocytes
global bit_count
bit_count = []

#  Cerate new classes of Erythrocytes using bit count as a basis (those below a certain bit count are considered unhealthy)
def sorting():
    if bit_count < [] :
        df['label'] = 'Grade A'
    elif bit_count < [] :
        df['label'] = 'Grade B'
    elif bit_count < [] :
        df['label'] = 'Grade C'
    else:
        df['label']  = 'Grade Unkown'