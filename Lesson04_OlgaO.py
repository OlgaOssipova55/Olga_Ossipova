'''x=int(input("Введите число:"))
if x > 0:
    print("Положительное число")
    if x < 0:
        print ("Отрицательное число")
        if x == 0:
            print ("Ноль")'''

'''x=int(input('Введите первое число:'))
y=int(input('Введите второе число:'))
if x>y:
    print(f'Число {x} больше чем {y}')
elif x<y:
    print(f'Число {x} меньше чем {y}')
else:
    print(f'Числа {x} и {y} равны')5'''

'''x= int(input("Enter your age:"))
if x> 18:
    print("You can drive a car1")
else:
    print(" You can not drive a car")'''

'''a=int(input("Введите число"))
if a >= 10 and a <=20:
     print("Число входит в диапазон от 10 до 20")
else:
     print("Число не входит в диапазон от 10 до 20")'''
#часть 2

'''x=int(input('Введите оценку от 1 до 5:'))
if x>=1 and x<=5:
    if x==5:
        print('Отлично')
    elif x==4:
        print('Хорошо')
    elif x==3:
        print('Удовлетворительно')
    else:
        print('Неудовлетворительно')
else:
    print('Некорректная оценка')'''

'''age=int(input('Введите возраст:'))
if age<=2:
    print('Младенец')
elif age>2 and age<12:
    print('Ребенок')
elif age>=12 and age<18:
    print('Подросток')
elif age>=18 and age<35:
    print('Молодежь')
elif age>=35 and age<60:
    print('Взрослый человек')
elif age>=60:
    print('Пожилой человек')'''

'''x=int(input('Введите оценку:'))
if x>1 and x<5:
    if x==5:
        print('Ваша оценка - пять, отлично!')
    elif x==4:
        print('Ваша оценка - четыре, хорошо!')
    elif x==3:
        print('Ваша оценка - три, удовлетворительно')
    elif x==2:
        print('Ваша оценка - два, неудовлетворительно')
    elif x==1:
        print('Ваша оценка - один, неудовлетворительно')
else:
    print('Некорректная оценка')'''

'''x=int(input('введите число от 1 до 4:'))
if x>=1 and x<=4:
    if x==1:
        print('Первая четверть')
    elif x==2:
        print('Вторая четверть')
    elif x==3:
        print('Третья четверть')
    elif x==4:
        print('Четвертая четверть')
else:
    print('Некорректное число')'''

'''x=int(input('Введите число:'))
y=x%2
if y==0:
    z=x%4
    print('четное')
    if z==0:
        print('делится на 4 без остатка')
    else:
        print('не делится на 4')
else:
    print('нечетное')'''

'''year=int(input('enter year:'))
q=year%4
w=year%100
if q==0 and w!=0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')'''
