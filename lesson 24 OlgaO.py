
'''import tkinter as tk

def select_color(color):
    selected_color.set(color)

root = tk.Tk()
root.title('Выбор цвета машины')
root.geometry('300x200')

colors = ['Красный', 'Синий', 'Зеленый', 'Желтый']

selected_color = tk.StringVar()

for i, color in enumerate(colors):
    check_button = tk.Button(root, text=color, command=lambda color=color: select_color(color))
    check_button.place(relx=0.1, rely=0.2 + i*0.1, relwidth=0.3, relheight=0.1)

selected_label = tk.Label(root, textvariable=selected_color)
selected_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()'''

'''import tkinter as tk

def select_color(color):
    selected_color.set(color)

root = tk.Tk()
root.title('Выбор цвета машины')
root.geometry('300x200')

colors = {
    'Основной цвет': ['Красный', 'Синий', 'Зеленый'],
    'Дополнительный цвет': ['Желтый', 'Оранжевый', 'Фиолетовый']
}

selected_color = tk.StringVar()

for group, group_colors in colors.items():
    group_label = tk.Label(root, text=group)
    group_label.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.05)

    for i, color in enumerate(group_colors):
        check_button = tk.Button(root, text=color, command=lambda color=color: select_color(color))
        check_button.place(relx=0.1, rely=0.25 + i*0.1, relwidth=0.3, relheight=0.1)

selected_label = tk.Label(root, textvariable=selected_color)
selected_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()'''


import tkinter as tk

def select_color():
    selected_color.set(var.get())
    # Добавьте свою логику обработки выбора цвета здесь
    # В этом примере просто выводим выбранный цвет в консоль
    print(f"Выбран цвет: {selected_color.get()}")

root = tk.Tk()
root.title('Выбор цвета машины')
root.geometry('300x200')

colors = {
    'Основной цвет': ['Красный', 'Синий', 'Зеленый'],
    'Дополнительный цвет': ['Желтый', 'Оранжевый', 'Фиолетовый']
}

selected_color = tk.StringVar()
var = tk.StringVar()

for group, group_colors in colors.items():
    group_label = tk.Label(root, text=group)
    group_label.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.05)

    for i, color in enumerate(group_colors):
        check_button = tk.Radiobutton(root, text=color, variable=var, value=color)
        check_button.place(relx=0.1, rely=0.25 + i*0.1, relwidth=0.3, relheight=0.1)

select_button = tk.Button(root, text="Выбрать", command=select_color)
select_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

selected_label = tk.Label(root, textvariable=selected_color)
selected_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

root.mainloop()

