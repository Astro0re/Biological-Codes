# Relational Skeletal System Data Base(Connect Searched for bone to every other bone in articulation)
# Duplicate for Organs?


def identify_bone():
    bone = input("Enter Bone: ")
    Shoulder = set['Clavicle', 'Scapula', 'Acromion']
    Arm = set['Humerus', 'Radius', 'Ulna']
    Phalanges = set['Proximal', 'Middle', 'Distal']
    Carpals = set['Scaphoid', 'Lunate', 'Triquetrum', 'Pisiform', 'Trapezium', 'Trapezoid', 'Capitate', 'Hamate']
    Hand = set['Metacarpals', Phalanges, Carpals]
    leg = set['Femur', 'Patella', 'Tibia', 'Fibula']
    Ankle = set['Talus', 'Calcaneus', 'Navicular', 'Cuboid', 'Cuneiforms']
    Foot = set[Ankle, 'Metatarsals', Phalanges]
    Neo_Cranium = set['Frontal', 'Parietal', 'Temporal', 'Occipital', 'Sphenoid', 'Ethmoid']
    Viscero_Cranium = set[
        'Maxilla', 'Mandible', 'Zygomatic', 'Nasal', 'Lacrimal', 'Palatine', 'Inferior Nasal Concha', 'Vomer', 'Turbinate bones']
    Auditory_Ossicles = set['Malleus', 'Incus', 'Stapes']
    Skull = set[Neo_Cranium, Viscero_Cranium, Auditory_Ossicles]
    Neck = set['Cranial Vertebrae', 'Cervical Vertebrae']
    Sternum = set['Manubrium', 'Body', 'Xiphoid Process']
    Ribs = set['True Ribs', 'False Ribs', 'Floating Ribs']
    Thoracic = set[Sternum, Ribs, 'Thoracic Vertebrae', 'Lumbar Vertebrae']
    Pelvis = set['Ilium', 'Ischium', 'Pubis', 'Sacrum', 'Coccyx']

    Upper_Limb = set[Shoulder, Arm, Hand]

    Lower_Limb = set[leg, Foot]

    Head_Neck = set[Skull, Neck]

    Thoracic_Pelvis = set[Thoracic, Pelvis]

    Skeletal_System = set[Upper_Limb, Lower_Limb, Head_Neck, Thoracic_Pelvis]

    Found = []
    Not_Found = []
    # articulation_count =int(input("How Many Bone's Articulate with this: "))
    # input("List the Articulations: ")
    for i in Skeletal_System:
        for j in i:
            for k in j:
                if bone == i or j or k:
                    Found.append(bone)
                    print(f"Found {Found}")
                elif bone != i or j or k:
                    Not_Found.append(bone)
                    print(f"Did not find {Not_Found}")


## Might have to turn the list into a dictionary to make it easier to search for the bone

# for i in Skeletal_System:
#   if len(Skeletal_System) == articulation_count:
#      return i, "Correct"
# else:
#    return "Incorrect"


identify_bone()

# review code
# Not Found output not working