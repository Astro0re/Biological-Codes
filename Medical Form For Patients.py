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
