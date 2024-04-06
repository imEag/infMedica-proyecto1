import json
from db_connection import db
from pymongo import errors

def handle_json_files(path, file):
  with open(f"{path}/{file}", encoding='utf-8') as f:
    data = json.load(f)
    for patient in data:
      formatted_patient = format_patient_data(patient)
      save_patient_to_db(formatted_patient)
      
def format_patient_data(patient):
  examenesToSave = []
  for key in patient['examen']:
    examen = {
      "examen": key,
      "resultado": patient['examen'][key]
    }
    examenesToSave.append(examen)
  
  dataToSave = {
    "ID": patient.get('id', ''),
    "nombres": patient.get('nombre', ''),
    "apellidos": patient.get('apellido', ''),
    "fecha": patient.get('fecha', ''),
    "sexo": patient.get('sexo', ''),
    "equipo": patient.get('equipo', ''),
    "modelo": patient.get('modelo', ''),
    "responsable": patient.get('responsable', ''),
    "profesion": patient.get('profesión', ''),
    "serial": patient.get('serial', ''),
    "dx": patient.get('dx', ''),
    "ips": patient.get('ips', ''),
    "medico": patient.get('médico', ''),
    "especialidad": patient.get('especialidad', ''),
    "ingreso": patient.get('ingreso', ''),
    "comorbilidades": patient.get('Comorbilidades', ''),
    "examenes": examenesToSave
  }
  
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