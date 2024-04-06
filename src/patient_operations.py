import os
from db_connection import db
from fileOperations.handle_JSON import handle_json_files
from fileOperations.handle_CSV import handle_csv_files
from fileOperations.handle_HL7 import handle_hl7_files
from fileOperations.createHL7 import create_hl7_file
from db_operations import get_all_patients, get_patient_by_ID

def list_all_patients():
  patients = get_all_patients()
  if patients:
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
  patient = db.patients.find_one({"ID": id})
  if patient:
    print(patient)
    new_name = input("Enter the new name: \n")
    db.patients.update_one({"ID": id}, {"$set": {"name": new_name}})
    print("Patient updated successfully \n")
  else:
    print("Patient not found \n")
    