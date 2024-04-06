import os
from fileOperations.handle_JSON import handle_json_files
from fileOperations.handle_CSV import handle_csv_files
from fileOperations.handle_HL7 import handle_hl7_files
from fileOperations.createHL7 import create_hl7_file
from db_operations import get_all_patients, get_patient_by_ID, delete_patient_by_ID, update_patient_by_ID

def list_all_patients():
  patients = get_all_patients()
  if patients and patients.count() > 0:
    for patient in patients:
      print("Patient: \n")
      print(patient)
      print("\n")
  else:
    print("No patients found \n")
    
def search_patient_by_id():
  id = input("Enter the ID of the patient: \n")
  patient = get_patient_by_ID(id)
  if patient:
    print("Patient found: \n")
    print(patient)
    create_hl7_file(patient, "assets/data", f"patient{patient['ID']}")
    print("\n")
  else:
    print("Patient not found \n")
    
def save_patients():
  path = "assets/dataToUpload"
  for file in os.listdir(path):
    if file.endswith(".json"):
      handle_json_files(path, file)
    if file.endswith(".csv"):
      handle_csv_files(path, file)
    if file.endswith(".txt"):
      handle_hl7_files(path, file)
    
def update_patient_by_id():
  id = input("Enter the ID of the patient: \n")
  patient = get_patient_by_ID(id)
  if patient:
    print("Patient found: \n")
    print(patient)
    print("\n")
    print("What field do you want to update? \n")
    option = update_menu()
    """ create a copy of the patient dictionary to update the fields """
    new_patient = patient.copy()
    while True:
      if option == "1":
        new_patient["nombres"] = input("Enter the new name: \n")
      elif option == "2":
        new_patient["apellidos"] = input("Enter the new last name: \n")
      elif option == "3":
        new_patient["edad"] = input("Enter the new age: \n")
      elif option == "4":
        new_patient["sexo"] = input("Enter the new genre: \n")
      elif option == "5":
        new_patient["fecha"] = input("Enter the new date: \n")
      elif option == "6":
        new_patient["equipo"] = input("Enter the new equipment: \n")
      elif option == "7":
        new_patient["modelo"] = input("Enter the new model: \n")
      elif option == "8":
        new_patient["responsable"] = input("Enter the new responsible: \n")
      elif option == "9":
        new_patient["profesion"] = input("Enter the new profession: \n")
      elif option == "10":
        new_patient["serial"] = input("Enter the new serial: \n")
      elif option == "11":
        new_patient["dx"] = input("Enter the new diagnosis: \n")
      elif option == "12":
        new_patient["medico"] = input("Enter the new doctor: \n")
      elif option == "13":
        new_patient["especialidad"] = input("Enter the new specialty: \n")
      elif option == "14":
        new_patient["ingreso"] = input("Enter the new income: \n")
      elif option == "15":
        update_patient_by_ID(id, new_patient)
        break
      elif option == "16":
        break
      else:
        print("Invalid option")
      option = update_menu()
  else :
    print("Patient not found \n")
    
    
def update_menu():
  print("1. nombres")
  print("2. apellidos")
  print("3. edad")
  print("4. sexo")
  print("5. fecha")
  print("6. equipo")
  print("7. modelo")
  print("8. responsable")
  print("9. profesion")
  print("10. serial")
  print("11. dx")
  print("12. medico")
  print("13. especialidad")
  print("14. ingreso")
  print("15. Save changes")
  print("16. Exit")
  option = input("Choose an option:")
  return option

def delete_patient_by_id():
  id = input("Enter the ID of the patient: \n")
  delete_patient_by_ID(id)
  print("\n")
  
  