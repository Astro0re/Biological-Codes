# Punnett Squares Code
# To predict distribution of parent genotype across a single generation 
def punn(Var1,Var2):
    chan1 = Var1[0],Var2[0]
    chan2 = Var1[0],Var2[1]
    chan3 = Var1[1],Var2[0]
    chan4 = Var1[1],Var2[1]
    print("Possible Combinations", chan1, chan2, chan3, chan4)

# Genotype of male and female 
M=["A","a"]
F= ["A","a"]
punn(M,F)

# Future generation code
def punn_1():
    chan1_= punn(chan1)

    