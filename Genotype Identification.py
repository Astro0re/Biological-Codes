# Genotype identification software using computer vision

import pandas as pd
import numbers as nu 
import tensorflow as tf
import kueras 

# Genotype identification using sequence identification 

# Import dataset 
# Source Hugging Face [Docty](https://huggingface.co/Docty)
df = pd.read_parquet("hf://datasets/Docty/Blood-Cells/data/train-00000-of-00001.parquet") 

# Filter out only Erythrocytes (Red Blood cells)

#  Cerate new classes of Erythrocytes using bit count as a basis (those below a certain bit count are considered unhealthy)