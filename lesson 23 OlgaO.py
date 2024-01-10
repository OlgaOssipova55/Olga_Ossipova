
import tkinter as tk 
from tkinter import ttk

def on_pressed(event):
    text=entry.get()
    label.config(text="Привет "+text+"!!! \n Для очистки нажммите кнопку \n 'Очистить'")

def delete():
    text=entry.get()
    label.config(text="Вы нажали на кнопу <Очистить>")
    entry.delete(0, tk.END)


def on_canvas_click(event):
    x,y = event.x,event.y
    print(f"Щелчок по координатам ({x},{y})")



root=tk.Tk()
root.geometry("400x200")

root.title("Тестовое окно")

listbox = ["one", "seecond", "third"]
combobox = ttk.Combobox(root,values = listbox)
label=tk.Label(root, text="Для привествия введите свое имя:\nЗатем нажмите клавишу Enter")
label.pack()
combobox.pack()

entry=tk.Entry(root, width='100')
entry.pack()
entry.bind("<Return>", on_pressed)

button=tk.Button(root,text="Очистить", command=delete)
button.pack()

canvas=tk.Canvas(root,width=400,height=200)
canvas.pack()
canvas.create_rectangle(100,0,200,300, fill="red")


canvas.bind("<Button-1>",on_canvas_click)

root.mainloop()