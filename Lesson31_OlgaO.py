'''import csv

def filter_csv(csv_file_path):
    with open(csv_file_path, 'r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['Production'].startswith('P'):
                print(row)

csv_file_path = 'C:\\Users\\Dell\\Desktop\\Python\\OlgaOssipova55\\Olga_Ossipova\\Lesson_31_OlgaO.csv'
filter_csv(csv_file_path)'''

import csv

def add_book(title, author, year, csv_file_path='C:\\Users\\Dell\\Desktop\\Python\\OlgaOssipova55\\Olga_Ossipova\\Lesson31_books_OlgaO.csv'):
    with open(csv_file_path, 'a', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([title, author, year])
    print("Книга успешно добавлена в файл CSV.")
    
def open_book(csv_file_path='C:\\Users\\Dell\\Desktop\\Python\\OlgaOssipova55\\Olga_Ossipova\\Lesson31_books_OlgaO.csv'):
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        print("Список книг в файле CSV:")
        for row in csv_reader:
            print(f"Название: {row[0]}, Автор: {row[1]}, Год издания: {row[2]}")

              
book_title = input("Введите название книги: ")
book_author = input("Введите автора книги: ")
book_year = input("Введите год издания книги: ")

add_book(book_title, book_author, book_year)
open_book()