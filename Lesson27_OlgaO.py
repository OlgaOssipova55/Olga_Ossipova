#1.1Выбор всех столбцов из Orders
'''
import sqlite3
import csv

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

#CREATE
create_table_query_orders = '''
CREATE TABLE IF NOT EXISTS orders (
    OrderID INTEGER PRIMARY KEY,
    Category TEXT
);
'''
cursor.execute(create_table_query_orders)
conn.commit()

#DELETE
drop_table_query_profile = '''
DROP TABLE IF EXISTS Profile;
'''
cursor.execute(drop_table_query_profile)
conn.commit()

cursor.execute(create_table_query_orders)
columns_info = cursor.fetchall()
print("Orders:")

for column_info in columns_info:
    print(column_info)

cursor.close()
conn.close()
'''

#1.2Выбор всех столбцов из Orders
'''
import sqlite3
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

query_unique = "SELECT DISTINCT category FROM products;"
cursor.execute(query_unique)

unique_categories = cursor.fetchall()

print("Unique:")
for category in unique_categories:
    print(category[0])

cursor.close()
conn.close()
'''
#1.3 Имена и фамилии клиентов с балансом на счете выше 1000
'''
import sqlite3
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

query_more1000 = "SELECT * FROM clients WHERE client.balance > 1000;"
cursor.execute(query_more1000)

more_than_1000 = cursor.fetchall()

print("MORE THAN 1000:")
for rows in more_than_1000:
    print(row)

cursor.close()
conn.close()
'''

#1.4 Данные Employees отсортированные по зарплате в убывающем порядке
'''
import sqlite3
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

query_emp_by_salary = "SELECT * FROM Employees ORDER BY Salary DESC;"
cursor.execute(query_emp_by_salary)

sorted_by_salary = cursor.fetchall()

print("Eployees list:")
for row in sorted_by_salary:
    print(row)

cursor.close()
conn.close()
'''
#2.1 запрос на увеличение зарплат на 5% в таблице Employees
'''
import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

inc5_salary_query = "SELECT salary*1.05 as salary_new FROM Employees;"
cursor.execute(inc5_salary_query)
new_salary = cursor.fetchall()

print("NEW_SALARIES:")
for row in new_salary:
    print(row)

cursor.close()
conn.close()
'''

#2.2 Запрос для обновления заказов ("Processing") с доставкой в страну США
'''import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

status_querry = "UPDATE orders SET Status = 'Shipped' WHERE Status = 'Processing' AND Country = 'USA';"
cursor.execute(status_querry)
conn.commit()

cursor.close()
conn.close()
'''

#2.3 Обновить таблицу Products, уменьшив цены на 10% для продуктов с запасом менее 20
'''
import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

price_for_less_20 = "UPDATE Products SET Price = Price * 0.9 as Prise_new WHERE Quantity < 20;"
cursor.execute(price_for_less_20)
conn.commit()

cursor.close()
conn.close()
'''

#2.4 Изменить статус клиентов в таблице Customer на "Active", если баланс выше 5000
'''
import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

update_status_query = "UPDATE Customer SET Status = 'Active' WHERE Balance > 5000;"
cursor.execute(update_status_query)
conn.commit()

cursor.close()
conn.close()
'''
