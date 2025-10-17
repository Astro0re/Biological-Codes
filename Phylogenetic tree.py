# Phylogenetic tree distance calculation function for DNA sequences.
from DNA_Sequence import dna_ver , count_dna
from Sequence_Alignment import s_a , diff_s_a , relational
import pandas as pd
from math import log


def phylo_tree():
    global seq_1,seq_2,diff
    seq_1 = input('First Sequence: ')
    seq_2 = input('Second Sequence: ')

    ver_seq_1 = dna_ver(seq_1)
    ver_seq_2 = dna_ver(seq_2)

    s_a(ver_seq_1,ver_seq_2)
    diff_s_a(ver_seq_1,ver_seq_2)
    # n = number of differences between two sequences
    # L = length of the sequences
    # p = n/L
    # formula = -(3/4) * ln(1-(4/3)*p)
    n = diff
    L = min(len(ver_seq_1),len(ver_seq_2))
    p = n/L
    distance = -(3/4) * log(1-(4/3)*p)
    print(f'Distance between two sequences is: {distance}')

s1= ['A','C','G','T','A','C','G','T']
s2= ['G','C','T','T','A','C','T','T']

phylo_tree(s1,s2)
