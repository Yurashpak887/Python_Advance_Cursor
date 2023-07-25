from abc import ABC
import json
class Model(ABC):

    @classmethod
    def get_data(cls):
        file = open("database/" + cls.file)
        file_writing = file.read()
        data = json.loads(file_writing)
        file.close()
        return data


    @classmethod
    def print_object(cls, ob: list):
        a = ob
        if len(a) > 0:
            fields = a[0].keys()
            for a1 in a:
                for field in fields:
                    print(a1[field])

    @classmethod
    def get_all(cls):
        data = cls.get_data()
        if len(data) > 0:
            fields = data[0].keys()
            for el in data:
                for field in fields:
                    if field == "id":
                        continue
                    print(el[field])
            return data

    def generate_dict(self):
        return self.__dict__

    @staticmethod
    def save_to_file(path_to_file, data):
        file = open(path_to_file, "w")
        data_for_json = json.dumps(data)
        file.write(data_for_json)


    def save(self):
        data = self.get_data()
        new_el = self.generate_dict()
        if len(data) > 0:
            new_el['id'] = data[-1]['id'] + 1
        else:
            new_el['id'] = 1
        data.append(new_el)
        self.save_to_file('database/' + self.file, data)

    @classmethod
    def get_by_id(cls, id):
        data = cls.get_data()
        counter = 0
        if len(data) > 0:
            fields = data[0].keys()
            for el in data:
                if id == el['id']:
                    return el
                counter +=1
            if counter == len(el):
                print("Not found plants with this id")
