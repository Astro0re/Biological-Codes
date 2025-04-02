#DNA Sequence in Python
Nuc=['A','G','T','C']

def DNA(var):
    seq=['A','G','T','C']
    for i in var:
        if i not in seq :
            print('Error')
        else:
            return var

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
    print(f' A = {len(A)} , G = {len(G_Cou)}, T = {len(T_Cou)}, C = {len(C_Cou)}')


b= ['A', 'T']
DNA(b)
Count_DNA(b)