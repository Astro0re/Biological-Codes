#Sequence Alignment, not entirely sure if this is correct
def s_a(seq1,seq2):
    same=[]
    for i in seq1:
        for j in seq2:
            if i == j:
                same.append(i)
    same_per = len(same)/(len(seq1)+len(seq2)) * 100
    print( "The percentage of similarity is", same_per)
    if same_per >= 40:
        print( "Sequences are Homologous")
    elif  20 <= same_per < 40:
        print( "Sequences are in the Twilight Zone of Homology")
    elif same_per < 20:
        print( "Sequences are in the Midnight Zone of Homology")




def relational(seq1,seq2):
    if len(seq1) != len(seq2):
        print("Sequence is not relational")
    elif len(seq1) - len(seq2) >= 20 or -20 :
        print("Sequence is not relational")
    else:
        print("Sequence is relational") 

x = ['a','d','f','e','p','w','r']
y = ['a','d','f','e','b','w','r']

s_a(x,y)

relational(x,y)

# Output incorrect review code
# Layout Problem Fixed