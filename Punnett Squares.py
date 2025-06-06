# Punnett Squares Code
# To predict distribution of parent genotype across a single generation
from numpy.ma.core import append

def punn_simple(var1,var2):
    print("Matching Genes...")
    print("Sorting possible combinations...")
    chan1 = var1[0],var2[0]
    chan2 = var1[0],var2[1]
    chan3 = var1[1],var2[0]
    chan4 = var1[1],var2[1]
    print("Possible Combinations", chan1, chan2, chan3, chan4)

def punn_multi(var1,var2):
    print("Matching Genes...")
    print("Sorting possible combinations...")
    chan1 = var1[0],var2[0]
    chan2 = var1[0],var2[1]
    chan3 = var1[1],var2[0]
    chan4 = var1[1],var2[1]

# Futher Possible genrations

    gen1_2 = chan1[0],chan2[0]
    gen2_2 = chan1[0], chan2[1]
    gen3_2 = chan1[1], chan2[0]
    gen4_2 = chan1[1], chan2[1]
    gen5_2 = chan3[0], chan4[0]
    gen6_2 = chan3[0], chan4[1]
    gen7_2 = chan3[1], chan4[0]
    gen8_2 = chan3[1], chan4[1]
    gen9_2 = chan1[0], chan3[0]
    gen10_2 = chan1[0], chan3[1]
    gen11_2 = chan1[1], chan3[0]
    gen12_2 = chan1[1], chan3[1]
    gen13_2 = chan2[0], chan4[0]
    gen14_2 = chan2[0], chan4[1]
    gen15_2 = chan2[1], chan4[0]
    gen16_2 = chan2[1], chan4[1]
    print(f"Proceeding Generations {gen1_2},{gen2_2},{gen3_2},{gen4_2},"
          f"{gen5_2},{gen6_2},{gen7_2},{gen8_2},{gen9_2},{gen10_2},{gen11_2},"
          f"{gen12_2},{gen13_2},{gen14_2},{gen15_2},{gen16_2}")

# Genotype of male and female 
M=["A","a"]
F= ["A","a"]
print( punn_simple(M,F))
print( punn_multi(M,F))


