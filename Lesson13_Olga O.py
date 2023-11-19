'''my_car = Car("Toyota","Camry",2022)
print (f"My car is a {my_car.year}{My_car.make}
{my_car.model}.")'''


# Инфо об автомобиле
'''class Car:
    def __init__ (self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def description(self):
        print (f"Автомобиль марки:{self.brand},модели:{self.model},года выпуска:{self.year}")

car1=Car ("Toyota","Camry",2022)
car2=Car("Infinity","FX35",2007)

car1.description()
car2.description()
'''

# Информация о сотруднике
'''
class Person:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
class Employee (Person):
    def __init__ (self, name,age,salary):
        Person.__init__ (self, name, age)
        self.salary=salary
    def get_info(self):
        print (f"Сотрудник {self.name} зарабатывает {self.salary} долларов в свои {self.age} лет")

E1=Employee ("Аркадий",35,21000)
E2=Employee ("Мария",50,35000)

E1.get_info()
E2.get_info()
'''

#Животные-Кошки-Собаки
'''class Animal:
    def __init__ (self,name):
        self.name = name
    def speak(self):
        pass

class Dog (Animal):
    def speak(self):
        return f"{self.name} говорит Гав!"
    
class Cat (Animal):
    def speak(self):
        return f"{self.name} говорит Мяу!"

def animal_speak(Animal):
    return Animal.speak()

dog=Dog("Барбос")
cat=Cat("Мурчелло")

print(animal_speak(dog))
print(animal_speak(cat))
'''

# Bank account

class Bank_Account:
    def __init__(self, balance, account_number):
        self.balance=balance
        self.account_number=account_number

    def account_info(self):
        print (f"Your account ID: {self.account_number} \nYour total balance: {self.balance}")
        
    def deposit(self):
        add=int(input(f"Your balance,$: {self.balance}\nInput deposit summ, $: \n"))
        self.balance +=add
        return f"Your ID: {self.account_number}\n You add ${add} on your account \n Your new balance: ${self.balance} "
    
    def withdraw(self):
        out=int(input(f"Your balance,$: {self.balance}\nInput withdraw summ, $: \n"))
        self.balance -=out
        print (f"Your ID: {self.account_number}\n You take ${out} from your account \n Your new balance: ${self.balance} ")

class Saving_account(Bank_Account):
    def __init__ (self, balance, account_number, interest_rate):
        Bank_Account.__init__(self,balance,account_number)
        self.interest_rate=interest_rate
        benefit=(self.balance*self.interest_rate*0.01)
        self.balance +=benefit
    def SA(self):
        return f"Your ID: {self.account_number}\nYour new balance: ${self.balance} according to your Interest rate {self.interest_rate}%"


Client1= Bank_Account(1300, '120785634587')
Client2= Saving_account(2200, '120785634587',10)

Operation=int(input("1 - BANK ACCOUNT \n2 - SAVING ACCOUNT \n"))
if Operation==1:
    print(Client1.account_info())
    BA = int(input("1 - for add money \n2 = for withdraw money \n3 - CANCEL OPERATION \n"))
    if BA==1:
        print(Client1.deposit())
    elif BA==2:
        print (Client1.withdraw())
    else:
        print ("Stop operations")
else:
    Client2.account_info()
    print (Client2.SA())
    






