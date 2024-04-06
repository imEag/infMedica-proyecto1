from menu import menu
from patient_operations import list_all_patients, search_patient_by_id, save_patients, update_patient_by_id

while True:
  option = menu()
  if option == "1":
    list_all_patients()
  elif option == "2":
    search_patient_by_id()
  elif option == "3":
    save_patients()
  elif option == "4":
    update_patient_by_id()
  elif option == "5":
    break
  else:
    print("Invalid option")
    
print("Goodbye!")