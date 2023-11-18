'''import math_operation

a=int(input("Введите первое число:"))
b=int(input("Введите второе число:"))
ans =input("Какую операцию желаете выполнить:")
if ans == "сложение":
    summary =math_operation.summ(a,b)2
    print ("Сумма:",summary)
elif ans =="разность":
    subtraction = math_operation.raz(a,b)
    print ("Разность",subtraction)
elif ans =="умножение":
    multiolication = math_operation.raz(a,b)
    print ("умножение",multiolication)
else:
    division=math_operation.dell(a,b)
    print ("Деление:",division)'''

'''def count_words(text):
    words = text.split()
    return len(words)

def usage():
    text = "Если мы сталкиваемся лицом к лицу с преградами, следуя в правильном направлении, все, что нам нужно сделать — это продолжить свой путь."
    
    word_count = count_words(text)
    print(f"Количество слов в тексте: {word_count}")
if __name__ == "__main__":
    usage()'''

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Student: {self.name}, Age: {self.age}")

student1 = Student("Anna", 33)

student1.display_info()