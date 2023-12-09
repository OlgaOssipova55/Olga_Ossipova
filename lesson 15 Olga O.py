'''class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Меня зовут: {self.name}, мне {self.age} лет"

# Corrected variable names and removed spaces
person1 = Person("Python", 32)
person2 = Person("Ирина", 25)

greet1 = person1.introduce()
greet2 = person2.introduce()

print(greet1)
print(greet2)'''


'''class Product:
    def __init__(self, name) :
        self.name=name

    def set_desc(self,desc):
        self.desc=desc

    def set_price(self,price):
        self.price=price


prod1=Product("Шампун")
prod2=Product("Вата")
print(prod1.name)'''

'''class Book:
    def __init__(self, titile,author,pub_year,is_av) :
        self.titile=titile
        self.author=author
        self.pub_year=pub_year
        self.is_av=is_av


    def checkout(self):
        self.is_av=False

    def checkin(self):
        self.is_av=True

    def display_info(self,):
        text="Есть в наличии" if self.is_av else "Нету в наличии"
        print(f"Книга {self.titile} под автоором {self.author}, {self.pub_year}\n{text}")


book1=Book("Пп", "пуш", 2021, True)
book2=Book("рр", "пвапва", 2023, False)


book1.display_info()
book1.checkout()
book1.display_info()'''


