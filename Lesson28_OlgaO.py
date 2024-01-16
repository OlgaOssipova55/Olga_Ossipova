import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Иcпользование SAVEPOINT
cursor.execute('SAVEPOINT sp1')

# Создание транзакции с использованием Commit
try:
    cursor.execute("UPDATE Employees SET Salary = Salary + 3000 WHERE Last_name='Air'")
    conn.commit()

except Exception as e:
# Применение ROLLBACK TO SAVEPOINT
    conn.execute('ROLLBACK TO SAVEPOINT sp1')
    print(f"Error: {e}")

# Иcпользование SAVEPOINT
cursor.execute('SAVEPOINT sp2')

try:
    cursor.execute("UPDATE Employees SET First_name = 'John' WHERE Last_name='Pitt'")
    conn.commit()

except Exception as e:
# Применение ROLLBACK TO SAVEPOINT
    conn.execute('ROLLBACK TO SAVEPOINT sp2')
    print(f"Error: {e}")

finally:
    conn.close()
