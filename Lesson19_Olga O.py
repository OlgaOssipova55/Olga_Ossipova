#Создайте простое окно Tkinter с заголоком и кнопкой Выход.При нажатии на кнопку приложение должно закрываться.
'''import tkinter as tk

def закрыть_приложение():
    окно.destroy()

окно = tk.Tk()
окно.title("Простое окно с кнопкой")

метка = tk.Label(окно, text="Добро пожаловать в Tkinter!")
метка.pack(pady=10)

кнопка_выхода = tk.Button(окно, text="Выход", command=закрыть_приложение)
кнопка_выхода.pack(pady=5)

окно.mainloop()'''

# создайте простое окно Tkinter с заголовком и выводом Анкеты о себе с помощью виджета Label
'''import tkinter as tk

окно = tk.Tk()
окно.title("Анкета о себе")

# Используем стандартный шрифт Tkinter
заголовок = tk.Label(окно, text="Анкета о себе", font=("TkDefaultFont", 32))
заголовок.pack(pady=10)

анкета = tk.Label(окно, text="Имя: Olga\nВозраст: 32\nПрофессия: Менеджер")
анкета.pack(pady=10)

окно.mainloop()'''

