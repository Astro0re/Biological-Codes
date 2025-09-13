# Genotype identification software using computer vision

import pandas as pd
import numpy as nu 
import tensorflow as tf
import kueras 

# Genotype identification using sequence identification 

# Import dataset 
# Source Hugging Face [Docty](https://huggingface.co/Docty)
df = pd.read_parquet("hf://datasets/Docty/Blood-Cells/data/train-00000-of-00001.parquet") 

df[1]

X_train, X_test, Y_train, Y_test = train_test_split(df, test_size=0.3, random_state=42)