# Relational Skeletal System Data Base(Connect Searched for bone to every other bone in articulation)
# Duplicate for Organs?s


def identify_bone():
    bone = input("Enter Bone: ").strip().title()
    
    bones = { "Shoulder" ; ['Clavicle', 'Scapula', 'Acromion'],

    "Arm" ; ['Humerus', 'Radius', 'Ulna'],

    "Phalanges" : ['Proximal', 'Middle', 'Distal'] ,

    "Carpals" : ['Scaphoid', 'Lunate', 'Triquetrum', 'Pisiform', 'Trapezium', 'Trapezoid', 'Capitate', 'Hamate'],

    "Hand" : ['Metacarpals', Phalanges, Carpals],

    "leg" : ['Femur', 'Patella', 'Tibia', 'Fibula'],

    "Ankle" : ['Talus', 'Calcaneus', 'Navicular', 'Cuboid', 'Cuneiforms'],

    "Foot" : [Ankle, 'Metatarsals', Phalanges],

    "Neo_Cranium" : ['Frontal', 'Parietal', 'Temporal', 'Occipital', 'Sphenoid', 'Ethmoid'],

    "Viscero_Cranium" : ['Maxilla', 'Mandible', 'Zygomatic', 'Nasal', 'Lacrimal', 'Palatine', 'Inferior Nasal Concha', 'Vomer', 'Turbinate bones'],

    "Auditory_Ossicles" : ['Malleus', 'Incus', 'Stapes'],

    "Skull" : [Neo_Cranium, Viscero_Cranium, Auditory_Ossicles],

    "Neck" : ['Cranial Vertebrae', 'Cervical Vertebrae'],

    "Sternum" : ['Manubrium', 'Body', 'Xiphoid Process'],

    "Ribs" : ['True Ribs', 'False Ribs', 'Floating Ribs'],

    "Thoracic" : [Sternum, Ribs, 'Thoracic Vertebrae', 'Lumbar Vertebrae'],

    "Pelvis" : ['Ilium', 'Ischium', 'Pubis', 'Sacrum', 'Coccyx'],

    "Upper_Limb" : [Shoulder, Arm, Hand],

    "Lower_Limb" : [leg, Foot],

    "Head_Neck" : [Skull, Neck],

    "Thoracic_Pelvis" : [Thoracic, Pelvis],

    "Skeletal_System" : [Upper_Limb, Lower_Limb, Head_Neck, Thoracic_Pelvis]
    }

    Found = []
    print("Searching Database...")
    for i in Skeletal_System :
        if bone in set(i):
            Found.append(bone)
            print(f"Found {Found}")
        else:
            print(f"Not Found, Wrong Input Entered ")




identify_bone()

# review code
# Not Found output not working