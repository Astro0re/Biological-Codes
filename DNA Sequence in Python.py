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
def DNA_Gen(self):
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
    print(f"{var} is valid") 

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

a = ['A','T','T','T','T','G','C']

DNA(b)
Count_DNA(b)

DNA(a)
Count_DNA(a)

# Locate the Start Code in a Sequence
def Start_locate(var):
    Start_Code_gene=('A','T','G')
    for i in var:
        if Start_Code_gene in var:
            print(f"Start point of the gene is at the {var.index(Start_Code_gene)} vaule")

loc = ['G','T','A','T','G','A','A']

Start_locate(loc)
