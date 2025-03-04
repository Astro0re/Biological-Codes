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
        if len(chan1) >3 :
            break

    for _ in chan2:
        if len(chan2) >3 :
            break

    for _ in chan3:
        if len(chan3) >3 :
            break

    for _ in chan4:
        if len(chan4) >3 :
            break

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
    print(f"Proceeding Generations {gen1_2},{gen2_2},{gen3_2},{gen4_2},"
          f"{gen5_2},{gen6_2},{gen7_2},{gen8_2},{gen9_2},{gen10_2},{gen11_2},"
          f"{gen12_2},{gen13_2},{gen14_2},{gen15_2},{gen16_2}")

# Genotype of male and female 
M=["A","a"]
F= ["A","a"]
print( punn(M,F))


# Medical Form For Patients
# For more convenient and easy to use management of medical records
def BIO_Form():
    Sickel_Cell = []
    print("Please input the necessary information...")
    name = input("Name: ")
    sex = input("Sex: ")
    age = input("Age: ")
    blood_group = input("Blood Group: ")
    genotype = input("Genotype: ")
    ill = input("Known Illnesses: ")
    comp = input("Complaint?: ")
    blood_pressure = input("Blood Pressure: ")
    first_observed = input("First Observation: ")
    appointment =input("Appointment: ")
    if appointment == "Yes" or "yes" or "Y":
        print("Please Wait.")
    else:
        print("Please Make An Appointment.")
        print("Your Information will be stored and used when you return during your appointment.")
    print(f"Welcome {name}, Thank you for your information, an employee will attend to you shortly.")
    if genotype == "SS" or "SC":
        Sickel_Cell.append(name)
    

BIO_Form()


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

# Relational Skeletal System Data Base(Connect Searched for bone to every other bone in articulation)
# Duplicate for Organs?
Shoulder =['Clavicle','Scapula','Acromion']
Arm =['Humerus','Radius','Ulna']
Phalanges =['Proximal','Middle','Distal']
Carpals =['Scaphoid','Lunate','Triquetrum','Pisiform','Trapezium','Trapezoid','Capitate','Hamate']
Hand=['Metacarpals', Phalanges, Carpals]
leg =['Femur','Patella','Tibia','Fibula']
Ankle =['Talus','Calcaneus','Navicular','Cuboid','Cuneiforms']
Foot =[Ankle, 'Metatarsals', Phalanges]  
Neo_Cranium =['Frontal','Parietal','Temporal','Occipital','Sphenoid','Ethmoid']
Viscero_Cranium =[ 'Maxilla','Mandible','Zygomatic','Nasal','Lacrimal','Palatine','Inferior Nasal Concha','Vomer','Turbinate bones']
Aditory_Ossicles =['Malleus','Incus','Stapes']
Skull =[Neo_Cranium,Viscero_Cranium,Aditory_Ossicles]
Neck =['Cranial Vertebrae','Cervical Vertebrae']
Sternum =['Manubrium','Body','Xiphoid Process']
Ribs =['True Ribs','False Ribs','Floating Ribs']
Thoracic =[Sternum, Ribs,'Thoracic Vertebrae','Lumbar Vertebrae']
Pelvis =['Ilium','Ischium','Pubis','Sacrum','Coccyx']

Upper_Limb =[Shoulder,Arm,Hand]

Lower_Limb =[leg,Foot]

Head_Neck =[Skull,Neck]

Thoracic_Pelvis =[Thoracic,Pelvis]

Skeletal_System =[Upper_Limb,Lower_Limb,Head_Neck,Thoracic_Pelvis]


def identify_bone(bone):
    input("Enter Bone: ")
    articulation_count =int(input("How Many Bone's Articulate with this: "))
    input("List the Articulations: ")
    for i in Skeletal_System:
        for j in i:
            for k in j:
                if bone in i or j or  k:
                    return "Bone Found"
                else:
                    return "Bone Not Found"
## Might have to turn the list into a dictionary to make it easier to search for the bone      
        
    for i in Skeletal_System:
        if len(Skeletal_System) == articulation_count:
            return i, "Correct"
        else:
            return "Incorrect"


#Sequence Alignment, not entirely sure if this is correct
def s_a(seq1,seq2):
    same=[]
    for i in seq1:
        for j in seq2:
            if i == j:
                same.append(i)
                same_per = len(same)/(len(seq1)+len(seq2)) * 100
                return same_per
                print ("The percentage of similarity is", same_per)
            if same_per >= 40:
                return "Sequences are Homologous"
            if  20 <= same_per < 40:
                return "Sequences are in the Twilight Zone of Homology"
            if same_per < 20:
                return "Sequences are in the Midnight Zone of Homology"




def relational(seq1,seq2):
    if len(seq1) != len(seq2):
        return "Sequence not relational"
    else:
        return "Sequence is relational"