def menu():
  print("1. List all patients in the database")
  print("2. Search for a patient by ID")
  print("3. Save all patients in the files (.csv, .json or .txt) inside the 'assets/dataToUpload' folder")
  print("4. Update a patient's information by ID")
  print("5. Delete a patient by ID")
  print("6. Exit")
  option = input("Choose an option: ")
  return option