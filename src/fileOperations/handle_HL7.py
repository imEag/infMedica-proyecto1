from db_operations import save_patient_to_db

def handle_hl7_files(path, file):
  with open(f"{path}/{file}", 'r', encoding='utf-8') as txt_file:
    # Read the content of the file line by line
    lista = txt_file.readlines()

  patient = format_patient_data(lista)
  print(patient)
  save_patient_to_db(patient)

def format_patient_data(lista):
  fecha = lista[0].split("|")[-1].split("\n")[0]
  cedula = lista[4].split('|')[2]
  edad = lista[4].split('|')[4].split('^')[3]
  nombre = lista[4].split('|')[12]
  apellidos = lista[4].split('|')[13]
  sexo = lista[4].split('|')[27].split('\n')[0]

  dataToSave = {
    "fecha": fecha,
    "ID": cedula,
    "edad": edad,
    "nombres": nombre,
    "apellidos": apellidos,
    "sexo": sexo
  }

  examenes = []
  for position, i in enumerate(lista[10:28:2]):
    nombre_examen = i.split("|")[2].split("^")[3]
    resultado = i.split("|")[3]

    examen = {
      "examen": nombre_examen,
      "resultado": resultado
    }
    if (position == 0 or position == 2 or position == 8):
      examenes.append(examen)

  dataToSave['examenes'] = examenes

  return dataToSave
