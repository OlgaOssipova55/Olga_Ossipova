'''import numpy as np

def sum_rows (arr):
    row_sums=np.sum(arr,axis=1)
    return row_sums

arr1 = np.random.randint (1,10,size=(3,3))
arr2 = np.random.randint (1,10,size=(3,3))

result = np.multiply (arr1, arr2)

print (f"Array1:{arr1}")
print (f"Array2:{arr2}")


sum_row1=sum_rows (arr1)
sum_row2=sum_rows (arr2)

print (f"\n result {result}")

print (f"Summa1{sum_row1}")
print (f"Summa2{sum_row2}")'''


import numpy as np

data = np.random.rand(100)

avg_value = np.mean(data)

median_value = np.median(data)

std_deviation = np.std(data)

print("Среднее значение:", avg_value)
print("Медиана:", median_value)
print("Стандартное отклонение:", std_deviation)
