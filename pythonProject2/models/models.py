import json
from framework.models import Model
class Plant(Model):
    file = 'plants.json'
    def __init__(self, name, location):
        self.name = name
        self.location = location




class Employee(Model):
    file = 'employee.json'

    def __init__(self, name, object_id, type_of_work):
        self.name = name
        self.object_id = object_id
        self.type_of_work = type_of_work

    def get_work(self):
        if self.type_of_work == 'plant':
            return Plant.get_by_id(self.object_id)
        elif self.type_of_work == 'salon':
            return Saloon.get_by_id(self.object_id)
        else:
            return

    @classmethod
    def get_by_id(cls, id):
        employee_dict = super().get_by_id(id)
        print(employee_dict)
        employee = Employee(employee_dict["name"], int(employee_dict['object_id']), employee_dict["type_of_work"])
        work_of_employee = employee.get_work()

        cls.print_object([employee_dict])
        print("Work on")
        cls.print_object([work_of_employee])

    @classmethod
    def get_employees_in_salons_and_plants(cls):
        data = cls.get_data()
        employees = []
        for el in data:
            if el['type_of_work'] in ['salon', 'plant']:
                employees.append(el)
        return employees



class Saloon(Model):
    file = "salons.json"
    def __init__(self, name, address, size):
        self.name = name
        self.address = address
        self.size = size
