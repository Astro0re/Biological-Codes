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
def dna_gen(self):
    print("Generating Sequence...")
    Nuc = ['A', 'G', 'T', 'C']
    Ran = random.choices(Nuc, k=10)
    print(Ran)


# Sequence Verification
def dan_ver(var):
    print("Validating Sequence...")
    check = 0
    for i in var:
        if i  == "A" :
            check = +1
        elif i == "G" :
            check = +1
        elif i == "T" :
            check = +1
        elif i == "C" :
            check = +1
    print(f"The percentage of nucleotides in the sequence is {check/len(var)*100}%")


# Sequence Nucleotide Count
def count_dna(var):
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

dna_gen(b)
count_dna(b)

dna_gen(a)
count_dna(a)

# Locate the Start Code in a Sequence
def start_locate(var):
    Start_Code_gene=('A','T','G')
    for i in var:
        if Start_Code_gene in var:
            print(f"Start point of the gene is at the {var.index(Start_Code_gene)} vaule")

loc = ['G','T','A','T','G','A','A']

start_locate(loc)
