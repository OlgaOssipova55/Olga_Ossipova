# создать простой интерфейс с текстовой  меткой и кнопкой. При нажатии на кнопку, текст на метке должен изменяться
'''import tkinter as tk

def изменить_текст():
    метка.config(text="Новый текст!")


окно = tk.Tk()
окно.title("Пример GUI")


метка = tk.Label(окно, text="Исходный текст")
метка.pack(pady=10)


кнопка = tk.Button(окно, text="Изменить текст", command=изменить_текст)
кнопка.pack()

окно.mainloop()'''

# создай интерыейс с тексовым полем и кнопкой Очистить.При нажатии на кнопку, текстовое поле должно очищаться.Также добавьте возможность ввода текста ис клавиатуры и кнопку, которая будет выполнять действи е при нажатии на клавишу Enter
'''import tkinter as tk

def очистить_поле():
    текстовоеПоле.delete(1.0, tk.END)

def обработать_ввод(event):
  
    if event.keysym == "Return":
        очистить_поле()

окно = tk.Tk()
окно.title("Пример с текстовым полем")

текстовоеПоле = tk.Text(окно, height=5, width=30)
текстовоеПоле.pack(pady=10)

кнопкаОчистить = tk.Button(окно, text="Очистить", command=очистить_поле)
кнопкаОчистить.pack()

текстовоеПоле.bind("<KeyPress>", обработать_ввод)

окно.mainloop()'''
