# Phylogenetic tree distance calculation function for DNA sequences.
from DNA_Sequence import dna_ver , count_dna
from Sequence_Alignment import s_a , diff_s_a , relational
import pandas as pd
from math import log


def phylo_tree():
    global seq_1,seq_2,diff
    seq_1 = str(input('First Sequence: '))
    seq_2 = str(input('Second Sequence: '))
    dna_ver(seq_1)
    dna_ver(seq_2)
    if dna_ver(seq_1) and dna_ver(seq_2) != "Sequence is Valid":
        print("Please recheck sequences")
        breakpoint

    s_a(seq_1,seq_2)
    diff=diff_s_a(seq_1,seq_2)
    # n = number of differences between two sequences
    # L = length of the sequences
    # p = n/L
    # formula = -(3/4) * ln(1-(4/3)*p)
    n = diff
    L = min(len(seq_1),len(seq_2))
    p = n/L
    distance = -(3/4) * log(1-(4/3)*p)
    print(f'Distance between two sequences is: {distance}')

s1= ['A','C','G','T','A','C','G','T']
s2= ['G','C','T','T','A','C','T','T']

phylo_tree()
# Output: Distance between two sequences is: 0.5108256237659907