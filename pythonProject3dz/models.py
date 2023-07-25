from abc import ABC

class Model(ABC):

    @staticmethod
    def generated_dict(self):
        return self.__dict__

    @staticmethod
    def cost_of_house(house):
        housing = Model.generated_dict(house)
        print(housing)
        value = housing['cost']
        return value




