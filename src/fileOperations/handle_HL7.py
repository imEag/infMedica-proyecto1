
def handle_hl7_files(path, file):
  with open(f"{path}/{file}", 'r') as txt_file:
  # Leer el contenido del archivo línea por línea
    lista = txt_file.readlines()
    
  dic={}
  fecha=lista[0].split("|")[-1].split("\n")[0]
  cedula=lista[4].split('|')[2]
  edad=lista[4].split('|')[4].split('^')[3]
  nombre=lista[4].split('|')[12]
  apellidos=lista[4].split('|')[13]
  sexo=lista[4].split('|')[27].split('\n')[0]


  dic['Fecha']=fecha
  dic['Cedula']=cedula
  dic['Edad']=edad
  dic['Nombre']=nombre
  dic['Apellidos']=apellidos
  dic['Sexo']=sexo

  examenes = []
  for position, i in enumerate(lista[10:28:2]):
    nombre_examen=i.split("|")[2].split("^")[3]
    resultado=i.split("|")[3]

    examen={
        "examen": nombre_examen,
        "resultado": resultado
    }
    if (position == 0 or position == 2 or position == 8):
      examenes.append(examen)

  dic['Examenes']=examenes
  
  print(dic)

