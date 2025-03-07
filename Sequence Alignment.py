#Sequence Alignment, not entirely sure if this is correct
def s_a(seq1,seq2):
    same=[]
    for i in seq1:
        for j in seq2:
            if i == j:
                same.append(i)
                same_per = len(same)/(len(seq1)+len(seq2)) * 100
                return "The percentage of similarity is", same_per
                print ("The percentage of similarity is", same_per)
            if same_per >= 40:
                return "Sequences are Homologous"
            elif  20 <= same_per < 40:
                return "Sequences are in the Twilight Zone of Homology"
            elif same_per < 20:
                return "Sequences are in the Midnight Zone of Homology"




def relational(seq1,seq2):
    if len(seq1) != len(seq2):
        return "Sequence not relational"
    else:
        return "Sequence is relational"
