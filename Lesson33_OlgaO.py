import numpy as np

array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([2, 4, 6])

res1 = array1 * array2

res2 = array1 ** array2

scalar = 5
res3_array1 = array1 / scalar
res3_array2 = array2 / scalar

print("\n1. Поэлементное умножение:")
print(res1)

print("\n2. Возведение массива array1 в степень array2:")
print(res2)

print("\n3. Деление каждого массива на скаляр (5):")
print("\narray1/scal:", res3_array1)
print("\narray2/scal:", res3_array2)

# 4. Пример использования broadcasting с операцией на выбор (сложение массива с вектором)
res4 = array1 + array2

print("\n4. Пример с операцией сложения:")
print(res4)
