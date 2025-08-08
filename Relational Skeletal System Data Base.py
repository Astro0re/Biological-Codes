# Relational Skeletal System Data Base(Connect Searched for bone to every other bone in articulation)
# Duplicate for Organs?s


def identify_bone():
    bone = input("Enter Bone: ").strip().title()
    
    bones = {
        "Shoulder": ['Clavicle', 'Scapula', 'Acromion'],
        "Arm": ['Humerus', 'Radius', 'Ulna'],
        "Phalanges": ['Proximal', 'Middle', 'Distal'],
        "Carpals": ['Scaphoid', 'Lunate', 'Triquetrum', 'Pisiform', 'Trapezium', 'Trapezoid', 'Capitate', 'Hamate'],
        "Hand": ['Metacarpals', 'Phalanges', 'Carpals'],
        "Leg": ['Femur', 'Patella', 'Tibia', 'Fibula'],
        "Ankle": ['Talus', 'Calcaneus', 'Navicular', 'Cuboid', 'Cuneiforms'],
        "Foot": ['Ankle', 'Metatarsals', 'Phalanges'],
        "Neo_Cranium": ['Frontal', 'Parietal', 'Temporal', 'Occipital', 'Sphenoid', 'Ethmoid'],
        "Viscero_Cranium": ['Maxilla', 'Mandible', 'Zygomatic', 'Nasal', 'Lacrimal', 'Palatine', 'Inferior Nasal Concha', 'Vomer', 'Turbinate bones'],
        "Auditory_Ossicles": ['Malleus', 'Incus', 'Stapes'],
        "Skull": ['Neo_Cranium', 'Viscero_Cranium', 'Auditory_Ossicles'],
        "Neck": ['Cranial Vertebrae', 'Cervical Vertebrae'],
        "Sternum": ['Manubrium', 'Body', 'Xiphoid Process'],
        "Ribs": ['True Ribs', 'False Ribs', 'Floating Ribs'],
        "Thoracic": ['Sternum', 'Ribs', 'Thoracic Vertebrae', 'Lumbar Vertebrae'],
        "Pelvis": ['Ilium', 'Ischium', 'Pubis', 'Sacrum', 'Coccyx'],
        "Upper_Limb": ['Shoulder', 'Arm', 'Hand'],
        "Lower_Limb": ['Leg', 'Foot'],
        "Head_Neck": ['Skull', 'Neck'],
        "Thoracic_Pelvis": ['Thoracic', 'Pelvis'],
        "Skeletal_System": ['Upper_Limb', 'Lower_Limb', 'Head_Neck', 'Thoracic_Pelvis']
    }

    def flatten_bones(key, bones_dict, seen=None):
        if seen is None:
            seen = set()
        items = []
        for item in bones_dict.get(key, []):
            if item in bones_dict and item not in seen:
                seen.add(item)
                items.extend(flatten_bones(item, bones_dict, seen))
            else:
                items.append(item)
        return items

    print("Searching Database...")
    found = False
    all_bones = set(flatten_bones('Skeletal_System', bones))
    if bone in all_bones:
        print(f"Found: {bone}")
        found = True
    if not found:
        print("Not Found, Wrong Input Entered")

identify_bone()

# review code
# Not Found output not working