# Punnett Squares Code
# To predict distribution of parent genotype across a single generation
from numpy.ma.core import append


def punn(var1,var2):
    chan1 = var1[0],var2[0]
    chan2 = var1[0],var2[1]
    chan3 = var1[1],var2[0]
    chan4 = var1[1],var2[1]

#2nd gen
    for _ in chan1:

    for _ in chan2

    for _ in chan3

    for _ in chan4

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
    print("Possible Combinations", chan1, chan2, chan3, chan4)
    print(f"Proceding Generations {gen1_2},{gen2_2},{gen3_2},{gen4_2},"
          f"{gen5_2},{gen6_2},{gen7_2},{gen8_2},{gen9_2},{gen10_2},{gen11_2},"
          f"{gen12_2},{gen13_2},{gen14_2},{gen15_2},{gen16_2}")

# Genotype of male and female 
M=["A","a"]
F= ["A","a"]
print( punn(M,F))



# Future generation code
def punn_1(var):
    print("Possible Combinations", chan1_,chan2_,chan3_,chan4_,chan5_,chan6_ )


# Medical Form For Patients
def BIO_Form():
    print("Please input the necessary information...")
    name = input("Name: ")
    sex = input("Sex: ")
    age = input("Age: ")
    blood_group = input("Blood Group: ")
    genotype = input("Genotype: ")
    ill = input("Known Illneses: ")
    print(f"Welcome {name}, Thank you for your information, an employee will attend to you shortly.")

BIO_Form()