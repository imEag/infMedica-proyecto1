import csv
from db_connection import db
from pymongo import errors

def handle_csv_files(path, file):
  with open(f"{path}/{file}", newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)  # Skip the header row

    for row in reader:
      patient = format_patient_data(row)
      save_patient_to_db(patient)

def format_patient_data(row):
  dataToSave = {
    "fecha": row[0],
    "ID": row[7],
    "nombres": row[8],
    "apellidos": row[9],
    "sexo": row[10],
    "edad": row[11],
    "dx": row[18],
    "examenes": [{
      "examen": "proc_tp",
      "resultado": row[12]
    },
                {
      "examen": "proc_ptt",
      "resultado": row[13]
    },
    {
      "examen": "proc_fib",
      "resultado": row[14]
    }]
  }
  print('Data to save:', dataToSave)
  return dataToSave

def save_patient_to_db(patient):
  try:
    if db.patients.find_one({"ID": patient["ID"]}):
      print(f"Patient {patient['ID']} already exists in the database. Skipping save operation.")
    else:
      db.patients.insert_one(patient)
      print(f"Patient {patient['ID']} saved successfully")
  except errors.PyMongoError as e:
    print(f"An error occurred while saving patient {patient['ID']}: {str(e)}")