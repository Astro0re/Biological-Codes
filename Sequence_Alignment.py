#Sequence Alignment, not entirely sure if this is correct
def s_a(seq1,seq2):
    print("Loading Sequences...")
    min_len = min(len(seq1), len(seq2))
    same = 0
    for i in range(min_len):
        if seq1[i] == seq2[i]:
            same += 1
    same_per = (same / min_len) * 100
    print( "The percentage of similarity is", same_per)
    if same_per >= 40:
        print( "Sequences are Homologous")
    elif  20 <= same_per < 40:
        print( "Sequences are in the Twilight Zone of Homology")
    elif same_per < 20:
        print( "Sequences are in the Midnight Zone of Homology")

# Sequence difference function
def diff_s_a(seq1,seq2):
    print("Comparing Sequences...")
    diff1=[]
    diff2=[]
    min_len = min(len(seq1), len(seq2))
    for i in range(min_len):
        if seq1[i] != seq2[i]:
            diff1.append(seq1[i])
            diff2.append(seq2[i])
    diff = 0 
    for i in range(len(diff1)):
        if diff1[i] != diff2[i]:
            diff += 1
    

# Code to test relationality 
def relational(seq1,seq2):
    print("Comparing Sequences...")
    if len(seq1) == len(seq2):
        print("Sequence is relational")
    elif len(seq1) - len(seq2) >= 20 or -20 :
        print("Sequence is not relational")

x = ['a','d','f','e','p','w','r']
y = ['a','d','f','e','b','w','r']

s_a(x,y)

relational(x,y)

