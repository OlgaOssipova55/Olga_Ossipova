'''# площадь круга
import math
R=int(input("Input your radius: "))
p=math.pi
S = p*R*R
print (f'Square is {S}')'''

'''# простое число
import math
num=int(input("Input your number: "))
if num<=1: prime=False
else: prime=True
i=2
while i<=math.sqrt(num):
    if num % i == 0:
        prime=False
        break
    i +=1
if prime: print (f"Ваше число {num} является простым")
else :
    print (f"Ваше число {num} не является простым")'''

'''# площадь треугольника через высоту
a=int(input("Введите длину основания: "))
h=int(input("Введите опущенную высоту: "))
S=a*h/2
print (f"Площадь треугольника равна {S}")'''

'''# дата через 7 дней
import datetime
cur_date=datetime.date.today()
date_in_7days=cur_date+datetime.timedelta(days=7)
print(f"Сегодня {cur_date}, через 7 дней будет {date_in_7days}")'''

'''# вычисление количества дней
import datetime
datetime1=input("Введите первую дату в формате ДД/ММ/ГГГГ \n")
date1=datetime.datetime.strptime(datetime1, "%d/%m/%Y")
datetime2=input("Введите вторую дату в формате ДД/ММ/ГГГГ \n")
date2=
days=date1-date2
print(f"Разница между датой {datetime1} и {datetime2} составляет {days.days} дней")'''

'''# вывод дня недели
import datetime
date=input("Please, input your date in format DD/MM/YYYY \n")
date1=datetime.datetime.strptime(date, "%d/%m/%Y")
if date1.weekday()==0:
    print('MONDAY')
elif date1.weekday()==1:
    print('TUESDAY')
elif date1.weekday()==2:
    print('WEDNESDAY')
elif date1.weekday()==3:
    print('THURSDAY')
elif date1.weekday()==4:
    print('FRIDAY')
elif date1.weekday()==5:
    print('SATURDAY')
else:
    print('SUNDAY')'''

'''# Игральная кость
import random
lot=random.randint(1,6)
your_num=int(input("Загадайте Ваше число: "))
if lot==your_num:
    print(f"Загаданное число {your_num},выпавшее число {lot}")
    print("Поздравляю")
else:
    print(f"Загаданное число {your_num},выпавшее число {lot}")
    print('Попробуйте еще раз')'''

'''# Генерация имени/выдает только 1 букву для имени, не пойму почему
import random, string
symb=int(input("Введите количество букв в имени: \n"))
a=int(input("Введите число от которого хотите начать отчет: \n"))
b=int(input("Введите число до которого хотите закончить отчет: \n"))
name=string
for i in range(symb):
    name=random.choices(string.ascii_letters)
num=random.randint(a,b)
fin_name=(f"{name}{num}")
print(f'YOUR NAME IS {fin_name}')'''

'''# Выбр из списка участников
import random
list=['Jin', 'Grigori','Leo','Nick','Richard','Mick','Ken','Elise','Olga','Eugene','Fedor','Maxim','Helen']
lot=random.choice(list)
print(f'{lot} has been chosen')'''

'''# Каждая секунда в течение минуты
import datetime, time
for i in range(1,60):
    sec=datetime.datetime.now()
    sec_60=sec.time()
    print(sec_60.strftime("%H:%M:%S"))
    time.sleep(1)'''

'''# Текущее время в АМ/РМ и 24 часовом формате
import time
cur_time=time.strftime('%H:%M:%S', time.localtime())
cur_time2=time.strftime('%I:%M:%S %p', time.localtime())
print(f"Сейчас {cur_time} или {cur_time2}")'''

'''# случайное время
import random
import datetime
custom_time=datetime.time(random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))
formatted_time1=custom_time.strftime('%H:%M:%S')
formatted_time2=custom_time.strftime('%I:%M:%S %p')
print(f'Time is {formatted_time1} OR {formatted_time2}')'''