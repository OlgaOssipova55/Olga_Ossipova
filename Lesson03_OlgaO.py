'''Name = 'Python'
Age = '32'
cities = ['Almaty', 'Karaganda', 'Astana']
print(f'Name: {Name}, Age:{Age}, cities: {cities}', sep=',',end='\n')'''

'''import sys
print("Hello world!", file=sys.stdout)'''

'''name=input("please,input your name ")
print(f"Hello, {name}")'''

'''age=int(input("How old are you? "))
was_born= 2023-age
print(f"Ты родился/ась в {was_born}")'''

'''name, age=input("Введите имя и возраст через пробел: ").split()
print (f"Имя: {name}, Возраст: {age}")'''

'''name, age=input("Введите имя и возраст через пробел: ").split()
text= "My name is {}, my age is {}".format(name, age)
print (text)'''

'''ДОМАШНЕЕ ЗАДАНИЕ'''

'''Приветствие
name=input("Введите имя ")
print(f'Hello, {name}')'''

'''Вычисление средней оценки
name1=int(input("Введите первую оценку "))
name2=int(input("Введите вторую оценку "))
name3=int(input("Введите третью оценку "))
average=(name1+name2+name3)/3
print(average)'''

'''средняя оценка и сравнение
math1=int(input("Введите Вашe первую оценку по математике (первая): "))
math2=int(input("Введите Вашe вторую оценку по математике (вторая): "))
math3=int(input("Введите Вашe третью оценку по математике (третья): "))
chem1=int(input("Введите Вашe первую оценку по химии (первая): "))
chem2=int(input("Введите Вашe вторую оценку по химии (вторая): "))
chem3=int(input("Введите Вашe третью оценку по химии (третья): "))
paint1=int(input("Введите Вашe первую оценку по рисованию (первая): "))
paint2=int(input("Введите Вашe вторую оценку по рисованию (вторая): "))
paint3=int(input("Введите Вашe третью оценку по рисованию (третья): "))
math_aver=(math1+math2+math3)/3
chem_aver=int((chem1+chem2+chem3)/3)
paint_aver=int((paint1+paint2+paint3)/3)
print (f"Ваша средняя оценка по математике {math_aver}, по химии {chem_aver}, по рисованию {paint_aver}")
print(math_aver>chem_aver)'''

'''Вывод личной карточки
name=input("Введите Ваше имя и фамилию через пробел: ").split()
age=input("Введите Вашу дату рождения (дд/мм/гггг): ")
city=input("Введите Ваш город проживания: ")
print(f"Name:{name}, Age:{age}, city: {city}", sep='\n', end='\n')'''