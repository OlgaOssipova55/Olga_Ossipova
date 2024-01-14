import sqlite3
import csv

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS Employees (
    PersonID INTEGER PRIMARY KEY,
    First_name TEXT,
    Last_name TEXT,
    Birth_date DATE,
    DepartmentID INTEGER,
    Salary REAL
);
'''
cursor.execute(create_table_query)
conn.commit()


data_to_insert = [
    ('Billy', 'Jean', '1995-12-05', 101, 52000.0),
    ('Jane', 'Air', '1981-02-15', 102, 88000.0),
    ('Robert', 'De Niro', '1970-05-18', 101, 74000.0)
]
cursor.executemany('INSERT INTO Employees (First_name, Last_name, Birth_date, DepartmentID, Salary) VALUES (?, ?, ?, ?, ?)', data_to_insert)


with open ('C:\\Users\\Dell\\Desktop\\Python\\OlgaOssipova55\\Olga_Ossipova\\Lesson26_OlgaO.csv', 'r') as csvfile:
    csvreader = csv.reader (csvfile)
    next(csvreader)
    cursor.executemany ('INSERT INTO Employees (First_name, Last_name, Birth_date, DepartmentID, Salary) VALUES (?, ?, ?, ?, ?);', csvreader)
    


conn.commit()

cursor.execute('SELECT * FROM Employees')
rows = cursor.fetchall()

for row in rows:
    print(row)

with open('C:\\Users\\Dell\\Desktop\\Python\\OlgaOssipova55\\Olga_Ossipova\\Lesson26_OlgaO_new.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([desc[0] for desc in cursor.description])
    csvwriter.writerows(rows)
    
cursor.close()
conn.close()

