'''Вычисение факториала
def factorial(number):
    factorial=1
    for i in range(1,number+1):
        factorial *=i
    return print (f"Факториал числа {number} равен {factorial}")
number=int(input("Пожалуйста, введите число для вычисления факториала: "))
factorial(number)'''


'''Перевод цельсия в Фаренгейт
def celcium_to_fahrengeit():
    cel=int(input("Сколько градусов по Цельсию сейчас в комнате? "))
    fah = cel*1.8+32
    return print(f'{cel} градусов по Цельсию, {fah} градусов по Фаренгейту')

def fahrengeit_to_celcium():
    fah=int(input("Сколько градусов по Фаренгейту сейчас в комнате? "))
    cel = (fah-32)/1.8
    return print(f'{cel} градусов по Цельсию, {fah} градусов по Фаренгейту')

choise = input("Выберите какую градусную шкалу вы хотите использовать для перевода градусов (Ц - Цельсия в Фаренгейт, Ф - Фаренгейта в Цельсия): ")
if choise =="Ц": celcium_to_fahrengeit()
elif choise =="Ф": fahrengeit_to_celcium()
else: (choise)'''


'''Нахождение НОК
def lcm (a,b):
    import math
    return print ((a*b) // math.gcd (a,b))
a=int(input("a="))
b=int(input("b="))
lcm(a,b)'''



'''Проверка палиндрома
def is_palindrome_number(n):
    n_rev=n[::-1]
    if n == n_rev: print(f"Число {n} является палиндромом")
    else: print(f"Число {n} не является палиндромом")
n=input("Пожалуйста, введите свое число:\n")
is_palindrome_number(n)'''

'''кредит
def credit(pcty):
    pctm=pcty/12
    c=s+(s*pctm*m/100)
    cm=c/m
    print(f"Общая сумма кредита без процентов равна {s}, с процентами {c}, ежемесячный платеж {cm}")
s=int(input("Какую сумму Вы планируете взять в кредит? \n"))
m=int(input("На сколько месяцев Вы планируете взять кредит? \n"))
pcty=int(input("Введите процент годовых отчислений? \n"))
credit(pcty)'''