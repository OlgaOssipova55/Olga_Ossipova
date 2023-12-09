# Создайте программу, которая запрашивает у пользователя ввод 2х чисел и пытается выполнить арифметические действия одного числа на другое. 
# Обработайте исключения ZeroDivisionError и предоставьте информативное сообщение об ошибке.

'''class Calculator:
    def __init__(self):
        pass

    def calculate(self):
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            sum_result = num1 + num2
            difference_result = num1 - num2
            product_result = num1 * num2

            try:
                quotient_result = num1 / num2



                print(f"Сумма: {sum_result}")
                print(f"Разность: {difference_result}")
                print(f"Произведение: {product_result}")
                print(f"Частное: {quotient_result}")
            except ZeroDivisionError:
                print("На ноль делить нельзя")
        except ValueError:
            print("Введите то, что является числом")


calculator = Calculator()
calculator.calculate()'''


# Создайте пользовательское исключение ValidationError, которое может возникнуть при проверке валидности данных пользователя. 
# Затем создайте программу, которая проверяет, является ли введенное имя пользователя допустимым 
# (например, не пустым и не содержащим специальные символы). Если введенное имя недопустимо, возбуждайте исключение ValidationError 
# соответствующим сообщением.
'''class ValidationError(Exception):
    def __init__(self, message="Ошибка ValidationError"):
        self.message = message
        super().__init__(self.message)

def validate_username(username):
    if not username:
        raise ValidationError("Имя пользователя не должно быть пустым")
    if not username.isalnum():
        raise ValidationError("Имя пользователя должно содержать только буквы и цифры")

def name():
    try:
        username = input("Введите имя пользователя: ")

        validate_username(username)

        print(f"Имя пользователя принято '{username}'.")
    except ValidationError as VE:
        
        print(f"Ошибка: {VE}")

name()'''

# СОздайте контекстный менеджер, который измеряет время выполнения блока кода, затем используйте его для имерения времени выполнения 
# операции ввода-вывода и вывда этого времени на милисекундах.

from contextlib import contextmanager
import time

@contextmanager
def measure_execution_time():
    start_time = time.time()
    yield
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # в миллисекундах
    print(f"Время выполнения составило {elapsed_time:.2f} миллисекунд")

with measure_execution_time():
    input("Введите данные: ")
