# Создайте базовый класс Vehicle, представляющий транспортное средство, с атрибутами model и  year. 
# Затем создайте подскласс Car, который будет наследовать название от Vehicle, и добавьте в него дополнительный атрибус fuel_type.
'''class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, model, year, fuel_type):
        Vehicle.__init__(self, model, year)
        self.fuel_type = fuel_type

    def info(self):
        return f"Ваша машина: {self.model} произведена в {self.year} году, марка топлива {self.fuel_type}"

vehicle1 = Car("Toyota", 1999, 'Gasoline')

sum = vehicle1.info()

print(sum)'''


# Создайте классы Animal и Flyable (с абстрактными методами) и подкласс Bird, который наследует от обоих классов.
# Реализуйте методы абстрактного класса Flyable в подклассе Bird.
'''from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def anim_do(self):
        pass

class Flyable(ABC):
    @abstractmethod
    def fly_do(self):
        pass

class Bird(Animal, Flyable):
    def anim_do(self):
        return "Летучая мышь летает"
    
    def fly_do(self):
        return "Альбатрос летает"
    
action = Bird()

print(action.anim_do())
print(action.fly_do())'''



# Расширьте класс Car из предыдущей практики (по созданию базового класса Vehicle) с добавлением новых подклассов, 
# представляющиех разные марки автомобилей, такие как Toyota, Ford, Tesla. Каждый подкласс должен иметь дополнительные атрибуты, 
# такие как model_name и fuel_efficience. Предопределите методы базового класса для педставления специфической информации 
# о каждой марке автомобиля.

'''from abc import ABC, abstractmethod

class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year

class Car(Vehicle, ABC):
    def __init__(self, model, year, fuel_type):
        Vehicle.__init__(self, model, year)
        self.fuel_type = fuel_type

    def info(self):
        return f"Ваша машина: {self.model} произведена в {self.year} году, марка топлива {self.fuel_type}, модель {self.model_name}, эффективность топлива {self.fuel_efficience}"
    
    
class Toyota(Car):
    def __init__(self, model, year, fuel_type, model_name, fuel_efficience):
        Car.__init__(self, model, year, fuel_type)
        self.model_name = model_name
        self.fuel_efficience = fuel_efficience

class Ford(Car):
    def __init__(self, model, year, fuel_type, model_name, fuel_efficience):
        Car.__init__(self, model, year, fuel_type)
        self.model_name = model_name
        self.fuel_efficience = fuel_efficience

class Tesla(Car):
    def __init__(self, model, year, fuel_type, model_name, fuel_efficience):
        Car.__init__(self, model, year, fuel_type)
        self.model_name = model_name
        self.fuel_efficience = fuel_efficience

vehicle1 = Toyota("Camry", 2005, 'Gasoline', "T-Camry", "40%")
vehicle2 = Ford("Mustang", 1975, 'Diesel', "Ford", "50%")
vehicle3 = Tesla("Roadster", 2022, 'Electric', "Tesla Model Y", "N/a")

info1 = vehicle1.info()
info2 = vehicle2.info()
info3 = vehicle3.info()

print(info1)
print(info2)
print(info3)'''