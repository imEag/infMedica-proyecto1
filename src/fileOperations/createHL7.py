def JSON_to_HL7(patient):
    hl7_message = []

    # MSH segment
    msh_segment = f"MSH|^~\&||||{patient['fecha']}|||ADT^A01|||2.6"
    hl7_message.append(msh_segment)

    # PID segment
    pid_segment = f"PID|||{patient['ID']}|||{patient['fecha']}|{patient['sexo']}||{patient['apellidos']}^{patient['nombres']}"
    hl7_message.append(pid_segment)

    # OBR segment
    for i, examen in enumerate(patient['examenes'], start=1):
      obr_segment = f"OBR|{i}|{examen['examen']}|||{examen['resultado']}"
      hl7_message.append(obr_segment)

    return '\n'.join(hl7_message)

def create_hl7_file(patient, path, file_name):
  hl7_message = JSON_to_HL7(patient)
  with open(f"{path}/{file_name}.txt", 'w') as file:
      file.write(hl7_message)
        