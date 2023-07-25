from models.models import Plant, Employee
from models.framework import Model
while True:
    print("1. Add new plant\n2.Get all plant's \n 3. Get plant by id \n 4. New employee \n 5. Get all employees"
          "s\n6. Get empl by id \n7. New salon\n8. Get all saloon. \n9. Get salon by id ")
    flag = int(input("Choose menu item"))
    if flag == 1:
        name = input("Name of plant")
        location = input("Locatino of plant")
        plant = Plant(name, location)
        plant.save()
    elif flag == 2:
        Plant.get_all_elements()
    elif flag == 3:
        idishka = int(input("Id:"))
        Plant.get_by_id(idishka)
    elif flag == 4:
        name = input("Name of your employee?:")
        surname = input("Surname?:")
        type_of_work = input("Type of work?:")
