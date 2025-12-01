# Vailidate Sequence 
def val(seq):
    SEQ=seq.upper()
    for i in SEQ:
        if i != "A" or "C" or "G" or "T":
            return "Error Validating Sequence"
        
#DNA Sequence in Python
import random
# Sequence Generator
def dna_gen():
    print("Generating Sequence...")
    Nuc = ['A', 'G', 'T', 'C']
    Ran = random.choices(Nuc, k=10)
    print(Ran)


# Sequence Verification
def dna_ver(var):
    print("Validating Sequence...")
    check = 0
    nuc = ['A', 'G', 'T', 'C']
    for i in var:
        if i  in nuc:
            check += 1 
    per = (check)/len(var) *100
    print(f"The percentage of nucleotides in the sequence is {per}%")
    if per > 45:
        print("Sequence is Valid")
    else:
        print("Sequence might not be valid, please recheck sequence")


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
              
# Locate the Start Code in a Sequence
def start_locate(var):
    Start_Code_gene=('A','T','G')
    for i in var:
        if Start_Code_gene in var:
            print(f"Start point of the gene is at the {var.index(Start_Code_gene)} vaule")

