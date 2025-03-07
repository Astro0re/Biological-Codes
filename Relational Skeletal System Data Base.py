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
Auditory_Ossicles =['Malleus','Incus','Stapes']
Skull =[Neo_Cranium,Viscero_Cranium,Auditory_Ossicles]
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
