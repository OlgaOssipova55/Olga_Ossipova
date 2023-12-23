import tkinter as tk
from tkinter import Menu, Frame, Label, Button, Checkbutton, filedialog, messagebox
from task_manager import TaskManager

class AddTaskDialog(tk.Toplevel):
    def __init__(self, parent, task_manager):
        super().__init__(parent)
        self.task_manager = task_manager
        self.title('Добавить задачу')
        self.geometry('300x200')
        self.center_on_screen()  # Центрирование окна на экране
        self.transient(parent)

        tk.Label(self, text='Название:', font=('Helvetica', 12)).grid(row=0, column=0)
        self.name_entry = tk.Entry(self, font=('Helvetica', 12))
        self.name_entry.grid(row=0, column=1)

        tk.Label(self, text='Сроки:', font=('Helvetica', 12)).grid(row=1, column=0)
        self.deadline_entry = tk.Entry(self, font=('Helvetica', 12))
        self.deadline_entry.grid(row=1, column=1)

        tk.Label(self, text='Описание:', font=('Helvetica', 12)).grid(row=2, column=0)
        self.desc_entry = tk.Entry(self, font=('Helvetica', 12))
        self.desc_entry.grid(row=2, column=1)

        tk.Button(self, text='Сохранить', command=self.save, font=('Helvetica', 12), bg='#4CAF50', fg='white').grid(row=3, column=0)
        tk.Button(self, text='Отмена', command=self.destroy, font=('Helvetica', 12), bg='#FF5733', fg='white').grid(row=3, column=1)

        self.grab_set()

    def save(self):
        name = self.name_entry.get()
        deadline = self.deadline_entry.get()
        description = self.desc_entry.get()
        if name and deadline and description:
            self.task_manager.add_task(name, deadline, description)
            self.destroy()
        else:
            messagebox.showwarning('Ошибка', 'Все поля должны быть заполнены')

    def center_on_screen(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()
        x = int((screen_width - window_width) / 2)
        y = int((screen_height - window_height) / 2)
        self.geometry(f'+{x}+{y}')

class ViewTasksDialog(tk.Toplevel):
    def __init__(self, parent, task_manager):
        super().__init__(parent)
        self.task_manager = task_manager
        self.title('Просмотр задач')
        self.geometry('400x400')  # Увеличим высоту для чек-баттона
        self.center_on_screen()
        self.transient(parent)

        self.checkboxes = []  # Список для хранения чек-баттонов

        self.listbox = tk.Listbox(self, font=('Helvetica', 12))
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.update_listbox()  # Первичное обновление списка

        tk.Button(self, text='Редактировать', command=self.edit, font=('Helvetica', 12), bg='#007BFF', fg='white').pack(side=tk.LEFT)
        tk.Button(self, text='Закрыть', command=self.destroy, font=('Helvetica', 12), bg='#FF5733', fg='white').pack(side=tk.RIGHT)

        self.grab_set()

    def edit(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            selected_task = self.task_manager.get_task(selected_index)
            EditTaskDialog(self, selected_task, self.task_manager, selected_index)
            self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        self.checkboxes = []  # Очищаем список чек-баттонов
        for i, task in enumerate(self.task_manager.tasks):
            frame = tk.Frame(self.listbox)
            frame.pack(side=tk.TOP, anchor='w')
            checkbox = tk.Checkbutton(frame, text=f"Задача: {task.name}   Срок: {task.deadline}", variable=tk.BooleanVar(value=True))
            checkbox.pack(side=tk.LEFT)
            self.checkboxes.append(checkbox)

    def center_on_screen(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()
        x = int((screen_width - window_width) / 2)
        y = int((screen_height - window_height) / 2)
        self.geometry(f'+{x}+{y}')

class EditTaskDialog(tk.Toplevel):
    def __init__(self, parent, task, task_manager, index):
        super().__init__(parent)
        self.task = task
        self.task_manager = task_manager
        self.index = index
        self.title('Редактировать задачу')
        self.geometry('300x200')
        self.center_on_screen()  # Центрирование окна на экране
        self.transient(parent)

        tk.Label(self, text='Название:', font=('Helvetica', 12)).grid(row=0, column=0)
        self.name_entry = tk.Entry(self, font=('Helvetica', 12))
        self.name_entry.grid(row=0, column=1)
        self.name_entry.insert(0, task.name)

        tk.Label(self, text='Сроки:', font=('Helvetica', 12)).grid(row=1, column=0)
        self.deadline_entry = tk.Entry(self, font=('Helvetica', 12))
        self.deadline_entry.grid(row=1, column=1)
        self.deadline_entry.insert(0, task.deadline)

        tk.Label(self, text='Описание:', font=('Helvetica', 12)).grid(row=2, column=0)
        self.desc_entry = tk.Entry(self, font=('Helvetica', 12))
        self.desc_entry.grid(row=2, column=1)
        self.desc_entry.insert(0, task.description)

        tk.Button(self, text='Сохранить', command=self.save, font=('Helvetica', 12), bg='#4CAF50', fg='white').grid(row=3, column=0)
        tk.Button(self, text='Отмена', command=self.destroy, font=('Helvetica', 12), bg='#FF5733', fg='white').grid(row=3, column=1)

        self.grab_set()

    def save(self):
        new_name = self.name_entry.get()
        new_deadline = self.deadline_entry.get()
        new_description = self.desc_entry.get()
        if new_name and new_deadline and new_description:
            self.task_manager.update_task(self.index, new_name, new_deadline, new_description)
            self.destroy()
        else:
            messagebox.showwarning('Ошибка', 'Все поля должны быть заполнены')

    def center_on_screen(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()
        x = int((screen_width - window_width) / 2)
        y = int((screen_height - window_height) / 2)
        self.geometry(f'+{x}+{y}')

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('DO Listik')

        self.task_manager = TaskManager()

        self.create_main_menu()
        self.create_widgets()

    def create_main_menu(self):
        menu_bar = Menu(self)
        self.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Сохранить как", command=self.save_tasks)
        file_menu.add_command(label="Загрузить", command=self.load_tasks)
        file_menu.add_separator()
        file_menu.add_command(label="Выйти", command=self.quit)

        task_menu = Menu(menu_bar, tearoff=0)
        task_menu.add_command(label="Добавить задачу", command=self.add_task)
        task_menu.add_command(label="Посмотреть задачи", command=self.view_tasks)

        menu_bar.add_cascade(label="Файл", menu=file_menu)
        menu_bar.add_cascade(label="Задачи", menu=task_menu)

    def save_tasks(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
        )
        if filename:
            response = self.task_manager.save_tasks_to_file(filename)
            messagebox.showinfo("Сохранение задач", response)

    def load_tasks(self):
        filename = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if filename:
            response = self.task_manager.load_tasks_from_file(filename)
            messagebox.showinfo("Загрузка задач", response)

    def create_widgets(self):
        frame = Frame(self)
        frame.pack(pady=20)

        title_label = Label(frame, text="DO Listik", font=("Helvetica", 16))
        title_label.pack(side=tk.TOP, fill=tk.X)

        tk.Label(frame).pack()  # Первая пустая Label
        tk.Label(frame).pack()  # Вторая пустая Label
        
        add_task_button = Button(frame, text="Добавить задачу", command=self.add_task, font=('Helvetica', 12), bg='#007BFF', fg='white')
        add_task_button.pack(side=tk.LEFT, padx=10)

        view_tasks_button = Button(frame, text="Посмотреть задачи", command=self.view_tasks, font=('Helvetica', 12), bg='#007BFF', fg='white')
        view_tasks_button.pack(side=tk.LEFT, padx=10)

    def add_task(self):
        AddTaskDialog(self, self.task_manager)

    def view_tasks(self):
        ViewTasksDialog(self, self.task_manager)

app = MainApp()
app.mainloop()