# создайте несколько функций, которые выполняют арифметические операции (сложение,вычитаие умножение) 
# для разных типов данных (целые числа,дроби,строки).
# Используйте статический полиморфизм для обработки разных типов данных одним и тем же методом.

'''class Math_operations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

# Пример использования
integer_result = Math_operations.add(15, 33)
float_result = Math_operations.subtract(10.4, 22.3)
string_result = Math_operations.multiply("What_", 3)

print(f"Integer Result: {integer_result}")
print(f"Float Result: {float_result}")
print(f"String Result: {string_result}")'''


# создайте базовый класс Shape с методом area(),который вычисляет площадь фигуры.
# Затем создайте подклассы, представляющие разные геометрические фигуры, такие как Cicrcle, Rectangle и Triangle.
# Переопределите метод area в каждом подклассе для вычисления пощади соответствующей фигуры. 

import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle = Circle(12.3)
rectangle = Rectangle(10, 5)
triangle = Triangle(6, 9)


area_circle = circle.area()
area_rectangle = rectangle.area()
area_triangle = triangle.area()

print(f"Площадь круга: {area_circle}")
print(f"Площадь прямоугольника: {area_rectangle}")
print(f"Площадь треугольника: {area_triangle}")


# Создайте интерфейс Drawable, представляющей объекты, которые могут быть нарисованы.
# Затем создайте классы Circle и Rectangle,которые реализуют этот интерфейс.
# Каждый класс должен имеет метод draw, который реализует различную логику для рисования круга и прямоугольника

from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Drawable):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Рисую круг, используя радиус {self.radius}")

class Rectangle(Drawable):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print(f"Рисую прямоугольник, используя ширину {self.width} и высоту {self.height}")

circle = Circle(15)
rectangle = Rectangle(7, 3)

circle.draw()
rectangle.draw()
