# Medical Form For Patients
# For more convenient and easy to use management of medical records
import random

def BIO_Form():
    print("Welcome...")
    print("Please fill tbis form with accurate infromation...")
    pt_info = {
        'name' : str,
        'sex' : str,
        'age'  : int ,
        'genotype'  : str,
        'blood_group' : str,
        'known_illness' : str, 
        'complaint' : str 
    }

    check_up_stats = {
        'height' : int, 
        'weight' : int,
        'blood_pressure' : int,
        'heart_rate' : int,
        'notes' : str,
        'urgent' : bool
    }
    Sickel_Cell = []
    
    patient_id = random.randint(1-9999, 0) #+ ("_MED")
    print("Please input the necessary information...")
    pt_info['name'] = input("Name: ")
    pt_info['sex'] = input("Sex: ")
    pt_info['age'] = int(input("Age: "))
    pt_info['genotype'] = input("Genotype: ")
    pt_info['blood_group'] = input("Blood Group: ")
    pt_info['known_illness'] = input("Known Illnesses: ")
    pt_info['complaint'] = input("Complaint?: ")


    check_up_stats['blood_pressure'] = int(input("Blood Pressure(Bps): "))
    check_up_stats['heart_rate'] = int(input("Heart Rate(Hr): "))
    check_up_stats['height']=int(input("Height(Meters): "))
    check_up_stats['weight']=int(input("Weight(Kilogram): "))
    BMI= (check_up_stats['height']/(check_up_stats['weight']*check_up_stats['weight']))*703

    #first_observed = input("First Observation: ")
    #appointment =input("Appointment: ")
    #if appointment == "Yes" or "yes" or "Y":
     #   print("Please Wait.")
    #else:
     #   print("Please Make An Appointment.")
      #  print("Your Information will be stored and used when you return during your appointment.")
    print(f"Welcome {pt_info['name']}, Thank you for your information, you will attend to you shortly.")
    print(f"Please note your patient identification number is {patient_id}")
    if pt_info['genotype'].upper() == "SS" or "SC":
        Sickel_Cell.append(patient_id)
    if int(check_up_stats['blood_pressure']) > 170 :
        check_up_stats['urgent'] = True
        print(f'This Patient requires urgent treatment')
    
    if check_up_stats['heart_rate'] > 70:
        print('Emergency!!')
    if pt_info['complaint'] == "Emergency":
        print('You will be attended to immediately')

BIO_Form()
