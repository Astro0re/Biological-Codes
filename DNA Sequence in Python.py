#DNA Sequence in Python
Nuc=['A','G','T','C']

def DNA(var):
    seq=['A','G','T','C']
    for i in var:
        if i not in seq :
            print('Error')
        else:
            return var

b= ['A', 'T']
DNA(b)
