'''text = "Закадровый"
first_char = text[0]
print (first_char)'''

'''text = 'доброе утро, мои родные люди'
text2 = '    доброе утро, мои родные люди   '
first_char = text[0]

substring = text[0:7]
part_of_string = text[7:]
every_secong_char = text[::3]
mixed = text[2:6:2]

lenght = len(text)

upper_text = text.upper()
lower_text = text.lower()
upper_text_test = text.upper()

stripped_text = text.strip()
new_text = text.replace("родные", "малознакомые")
splitted_sentence = text.split()

print (splitted_sentence)'''

'''text = 'red,green,blue'
splitted_text = text.split (',')
print (splitted_text)'''

'''text = ['доброе', 'утро,', 'мои', 'родные', 'люди']
line1 = "_".join(text)
line2 = " ".join(text)
line3 = "\n".join(text)
print (line3)'''

'''text = 'доброе утро, мои родные люди'
position=text.find("утро")
position2=text.find("вечер")
print(position2)'''

'''text='apple is red apple is green'
count=text.count('apple')
print(count)'''

'''text = 'доброе утро, мои родные люди'
start_with = text.startswith("доброе")
ends_with = text.endswith("родные")
print(start_with)
print(ends_with)'''

Домашнее задание: количество символов
text = "Olga"
lenght = len(text)
print (lenght)

Домашнее задание: разделение слов
text2 = 'red<green<blue'
splitted_text = text2.split ('<')
print (splitted_text)

Домашнее задание: замена слова
text3 = 'доброе утро, мои родные люди'
new_text = text3.replace("мои родные", "малознакомые")
print (new_text)

Домашнее задание: калькулятор
a=1
b=5
result=f'{a}+{b}={a+b} \n{a}-{b}={a-b} \n{a}*{b}={a*b} \n{a}/{b}={a/b}'
print(result)

Домашнее задание: выделение имени из почтового адреса
mail = "olga@mail.ru"
name = mail.split("@")[0]
print("Имя:", name)