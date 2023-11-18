'''# 1 Вывод списка, удаление по имени
dictionary={"Фролов":"Александр","Беляев":"Алик","Прушинский":"Евгений","Добролюбов":"Сергей"}
print(dictionary)
del dictionary["Фролов"]
print(dictionary)'''

'''#2 инвентарь с информацией о товарах
aaa={1001:["мука","2 кг","1000 тг"], 1002:["хлеб","2 булки ","200 тг"], 1003:["молоко"," 2 л","400 тг"], 1004:["яблоки","1 кг ","600 тг"]}
print(aaa)
for number in aaa.keys():
        print(f"{number}: товар {aaa[number][0]}, количество {aaa[number][1]}, стоимость {aaa[number][2]}")'''


'''# 3,4 создание двух множеств и их пересечение
list1={1,2,3,4,5,6,7,8,9}
list2={1,12,3,4,67,35,8,9}
print("difference: ",list1.difference(list2))
print("union: ", list1.union(list2))'''

'''# 5 Поиск товара
aaa={
    1001:"мука", 
    1002:"хлеб", 
    1003:"молоко", 
    1004:"яблоки"
    }
ID=int(input("Input ID: "))
if ID in aaa:
    print(f"Товар под номером ID {ID} - {aaa[ID]}")
else:
    print ('Not found')'''

'''# 6 Нахождение пересечения
list1={1,2,3,4,5,6,7,8,9}
list2={1,12,3,4,67,35,8,9}
print(list1.intersection(list2))'''

'''#7 Список стран и городов
World={"Казахстан":["Астана","Алмата","Караганда"]}
new_country = input("Пожалуйста, введите добавляемую страну: ")
cities = input("Пожалуйста, введите города через запятую: ").split(',')
World[new_country]=cities
print(World)'''

'''#8 подсчет стоимости
list={"мука":1000, "хлеб":200, "молоко":400, "яблоки":600}
prices=list.values()
sum=0
i=int
for i in list.values():
    sum=sum+i
print(sum)'''

'''#9 Нахождение объединения
list1={1,2,3,4,5,6,7,8,9}
list2={1,12,3,4,67,35,8,9}
print(list1.symmetric_difference(list2))'''