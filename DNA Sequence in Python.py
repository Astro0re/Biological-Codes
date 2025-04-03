#DNA Sequence in Python
import random

Nuc=['A','G','T','C']

# Sequence Generator
def DNA_Gen(self):
    Nuc = int(['A', 'G', 'T', 'C'])
    Ran = random.randint (Nuc, k = 10)
    print(Ran)


# Sequence Verification
def DNA(var):
    seq=['A','G','T','C']
    for i in var:
        if i not in seq :
            print('Error')
        else:
            return var

# Sequence Nucleotide Count
def Count_DNA(var):
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
DNA(b)
Count_DNA(b)
