from pymongo import MongoClient, errors
from db_connection import db

def save_patient_to_db(patient):
  try:
    if db.patients.find_one({"ID": patient["ID"]}):
      print(f"Patient {patient['ID']} already exists in the database. Skipping save operation.")
    else:
      db.patients.insert_one(patient)
      print(f"Patient {patient['ID']} saved successfully")
  except errors.PyMongoError as e:
    print(f"An error occurred while saving patient {patient['ID']}: {str(e)}")
    
def get_all_patients():
  try:
    patients = db.patients.find()
    return patients
  except errors.PyMongoError as e:
    print(f"An error occurred while getting all patients: {str(e)}")
    return None

def get_patient_by_ID(ID):
  try:
    patient = db.patients.find_one({"ID": ID})
    return patient
  except errors.PyMongoError as e:
    print(f"An error occurred while getting patient {ID}: {str(e)}")
    return None
  
def delete_patient_by_ID(ID):
  try:
    patient = db.patients.find_one({"ID": ID})
    if patient:
      db.patients.delete_one({"ID": ID})
      print(f"Patient {ID} deleted successfully")
    else:
      print(f"Patient {ID} not found")
  except errors.PyMongoError as e:
    print(f"An error occurred while deleting patient {ID}: {str(e)}")
    
def update_patient_by_ID(ID, new_patient):
  try:
    patient = db.patients.find_one({"ID": ID})
    if patient:
      db.patients.update_one({"ID": ID}, {"$set": new_patient})
      print(f"Patient {ID} updated successfully")
    else:
      print(f"Patient {ID} not found")
  except errors.PyMongoError as e:
    print(f"An error occurred while updating patient {ID}: {str(e)}")
    