import csv
from db_operations import save_patient_to_db

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

  return dataToSave

