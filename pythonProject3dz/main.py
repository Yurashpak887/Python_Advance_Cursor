class Person:
    def __init__(self, name, age, money, has_home):
        self.name = name
        self.age = age
        self.money = money
        self.has_home = has_home

    def provide_information(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Money:", self.money)
        print("Has Home:", self.has_home)

    def make_money(self, amount):
        self.money += amount

    def buy_house(self, house):
        if self.money >= house.cost:
            self.money -= house.cost
            self.has_home = True
            print("Congratulations! You bought a house.")
        else:
            print("Sorry, you don't have enough money to buy this house.")


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def apply_purchase_discount(self, discount):
        self.cost -= discount


class Realtor:
    _instance = None

    def __new__(cls, name, houses, discount):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.name = name
            cls._instance.houses = houses
            cls._instance.discount = discount
        return cls._instance

    def provide_house_information(self):
        for house in self.houses:
            print("House Area:", house.area)
            print("House Cost:", house.cost)

    def give_discount(self, house):
        house.apply_purchase_discount(self.discount)

    def steal_money(self, person):
        chance = random.randint(1, 10)
        if chance == 1:
            amount = person.money * 0.1
            person.money -= amount
            print("Oops! The realtor stole", amount, "from you.")


# Creating a person
person = Person("John", 30, 50000, False)

# Creating houses
house1 = House(40, 200000)
house2 = House(60, 300000)

# Creating a realtor
realtor = Realtor("Bob", [house1, house2], 5000)

# Person's actions
person.provide_information()
person.make_money(10000)
person.buy_house(house1)

# Realtor's actions
realtor.provide_house_information()
realtor.give_discount(house2)
realtor.steal_money(person)

# Updated person's information
person.provide_information()
