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