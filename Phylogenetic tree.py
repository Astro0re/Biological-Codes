# Phylogenetic tree distance calculation function for DNA sequences.
from DNA_Sequence import val , dna_gen , dna_ver , count_dna
from Sequence_Alignment import s_a , diff_s_a , relational
import pandas as pd

def phylo_tree():
    # n = number of differences between two sequences
    # L = length of the sequences
    # p = n/L
    # formula = -(3/4) * ln(1-(4/3)*p)
    pass