# Vailidate Sequence 
def val(seq):
    SEQ=seq.upper()
    for i in SEQ:
        if i != "A" or "C" or "G" or "T":
            return "Error Validating Sequence"
        
#DNA Sequence in Python
import random

Nuc=['A','G','T','C']

# Sequence Generator
def DNA_Gen():
    print("Generating Sequence...")
    Nuc = ['A', 'G', 'T', 'C']
    Ran = random.choices(Nuc, k=10)
    print(Ran)


# Sequence Verification
def DNA(var):
    print("Validating Sequence...")
    seq=['A','G','T','C']
    for i in var:
        if i not in seq :
            print('Error')
        else:
            return var

# Edit Verification code to check if
# the percentage of nucleotides not within regulation is big enough to null the sequence

# Sequence Nucleotide Count
def Count_DNA(var):
    print("Sorting Sequence...")
    A_Cou=[]
    G_Cou=[]
    T_Cou=[]
    C_Cou=[]
    for i in var:
        if i == 'A':
            A_Cou.append(i)
        elif i == 'G':
            G_Cou.append(i)
        elif i == 'T':
            T_Cou.append(i)
        elif i == 'C':
            C_Cou.append(i)
    print(f' A = {len(A_Cou)} , G = {len(G_Cou)}, T = {len(T_Cou)}, C = {len(C_Cou)}')


b= ['A', 'T']

a = DNA_Gen()

DNA(b)
Count_DNA(b)

DNA(a)
Count_DNA(a)
