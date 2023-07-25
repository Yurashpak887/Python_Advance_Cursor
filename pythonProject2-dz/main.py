class Animals:
    """
    Батьківський клас, має методи eat, sleep
    """

    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")

class Lion(Animals):
    """
    Тварина "Лев" з додатковими методами
    """

    def roar(self):
        print("Lion is roaring")

class Elephant(Animals):
    """

    """

    def spray_water(self):
        print("Elephant is spraying water")

# Створення екземплярів тварин і виклик їх унікальних методів
lion = Lion()
lion.roar()  # Виведе: Lion is roaring

elephant = Elephant()
elephant.spray_water()  # Виведе: Elephant is spraying water

# Визначення, чи є кожна з тварин екземпляром класу Animals
print(isinstance(lion, Animals))  # Виведе: True
print(isinstance(elephant, Animals))  # Виведе: True





class Human:
    """
    Клас Human, має методи eat, sleep, study, work
    """

    def eat(self):
        print("Human is eating")

    def sleep(self):
        print("Human is sleeping")

    def study(self):
        print("Human is studying")

    def work(self):
        print("Human is working")

class Centaur(Human, Animals):
    """
    Клас Centaur успадковується від Human і Animals та має унікальний метод
    """

    def run(self):
        print("Centaur is running")

# Створення екземпляру класу Centaur та виклик загального і унікального методів
centaur = Centaur()
centaur.eat()  # Виведе: Human is eating
centaur.run()  # Виведе: Centaur is running

class Profile:

    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __str__(self):
        return f"Profile: [{self.name}, {self.last_name}, {self.phone_number}, {self.address}, {self.email}, {self.birthday}, {self.age}, {self.sex}]"

# Створення екземпляру класу Profile та виведення рядкового представлення
profile = Profile("John", "Doe", "123456789", "123 Main St", "john@example.com", "1990-01-01", 33, "Male")
print(profile)  # Виведе: Profile: [John, Doe, 123456789, 123 Main St, john@example.com, 1990-01-01, 33, Male]
