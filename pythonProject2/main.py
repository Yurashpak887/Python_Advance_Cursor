from models.models import Plant, Employee, Saloon
while True:
    print("1. Add new plant\n2.Get all plant's \n 3. Get plant by id \n 4. New employee \n 5. Get all employees"
          "s\n6. Get empl by id \n7. New salon\n8. Get all saloon. \n9. Get salon by id ")
    flag = int(input("Choose menu item"))
    if flag == 1:
        name = input("name:")
        location = input("Location")
        plant = Plant(name, location)
        plant.save()
    elif flag == 2:
        Plant.get_all()

    elif flag == 3:
        id = int(input("Get id?"))
        plant = Plant.get_by_id(id)
        Plant.print_object([plant])

    elif flag == 4:
        name = input("Name employee")
        object_id = input("Employee work id")
        type_of_work = input("Type of work?")
        employee = Employee(name, object_id, type_of_work)
        employee.save()

    elif flag == 5:
        Employee.get_all()

    elif flag == 6:
        id = int(input("Type id to search"))
        emp = Employee.get_by_id(id)

    elif flag == 7:
        name = input("Name salon")
        address = input("Address ")
        size = input("Size")
        salon = Saloon(name, address, size)
        salon.save()

    elif flag == 8:
        Saloon.get_all()

    elif flag == 9:
        id = int(input("Input id:"))
        salon = Saloon.get_by_id(id)
        Saloon.print_object([salon])

    elif flag ==10:
        employees = Employee.get_employees_in_salons_and_plants()
        if len(employees) > 0:
            print("Employees in salons and plants:")
            Employee.print_object(employees)
        else:
            print("No employees found in salons and plants.")