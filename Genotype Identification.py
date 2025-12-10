# Genotype identification software using computer vision

import os
import pandas as pd
import numpy as nu 
import tensorflow as tf
import keras
from keras import layers, models, optimizers
from keras.utils import load_img, img_to_array, save_img
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from PIL import image


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

    df_img = Eryth['image']
    df_label = Eryth['label']


    # Change to a numpy array
    df_img.as_numpy_iterator().next()

    # Split data
    train_size = int( df_img * .7)
    val_size = int(df_img * .2)
    test_size = int(df_img * .1)

    # Transform the image data into a numpy array
    df_img.map(lambda x, y: (x/255, y))

    x = df_img
    y = df_label


    # Train Model on the Erythrocytes Sequential and Regression?
    model = tf.keras.Sequential()

    model.add(Conv2D(125, (3,3), activation='relu', input_shape=(256,256,3), padding='same'))
    model.add(Conv2D(125, activation='relu' ,padding='same'))
    model.add(MaxPooling2D())

    model.add(Conv2D(225, activation='relu' ,padding='same'))
    model.add(Conv2D(225, activation='relu' ,padding='same'))
    model.add(Conv2D(225, activation='relu' ,padding='same'))
    model.add(MaxPooling2D())

    model.add(Conv2D(300, (3,3), activation='relu', padding='same'))
    model.add(Conv2D(300, activation='relu' ,padding='same'))
    model.add(Conv2D(300, activation='relu' ,padding='same'))
    model.add(MaxPooling2D())

    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    model.summary()
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

__main__