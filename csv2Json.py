import json
import csv

data = []

with open('assets/dataToUpload/paciente2.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)

    for row in reader:
        fecha = row[0]
        id = row[7]
        nombre = row[8]
        apellido = row[9]
        sexo = row[10]
        edad = row[11]
        dx_ppal = row[18]
        proc_tp = row[12]
        proc_ptt = row[13]
        proc_fib = row[14]
        
        fila = {
            'fecha': fecha,
            'id': id,
            'nombre': nombre,
            'apellido': apellido,
            'edad': edad,
            'genero': sexo,
            'diagnostico': dx_ppal,
            'proc_tp': proc_tp,
            'proc_ptt': proc_ptt,
            'proc_fib': proc_fib
        }
        data.append(fila)
    print(data)

with open('assets/data', 'w') as jsonfile:
    json.dump(data, jsonfile)


