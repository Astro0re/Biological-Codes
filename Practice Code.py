# Punnett Squares Code
def punn(Var1,Var2):
    chan1 = Var1[0],Var2[0]
    chan2 = Var1[0],Var2[1]
    chan3 = Var1[1],Var2[0]
    chan4 = Var1[1],Var2[1]
    print("Possible Combinations", chan1, chan2, chan3, chan4)

M=["A","a"]
F= ["A","a"]
punn(M,F)