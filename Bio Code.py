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
og = punn(M,F)

# Future generation code
def punn_1(var):
    chan1_= punn(og[0],og[1])
    chan2_= punn(og[2],og[3])
    chan3_= punn(og[0],og[2])
    chan4_= punn(og[1],og[3])
    chan5_= punn(og[1],og[2])
    chan6_= punn(og[0],og[3])
    print("Possible Combinations", chan1_,chan2_,chan3_,chan4_,chan5_,chan6_ )

punn_1(og)