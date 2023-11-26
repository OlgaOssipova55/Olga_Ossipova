import json

class List:
    def __init__(self, name, deadline, desc):
        self.name = name
        self.deadline = deadline
        self.desc = desc

    def __str__(self):
        return f"Название: {self.name}\nСроки: {self.deadline}\nОписание: {self.desc}\n-----------------"

class DoList:
    def __init__(self):
        self.lists = []

    def addList(self):
        name = input("Пожалуйста, укажите задачу: \n")
        deadline = input("Пожалуйста, укажите сроки выполнения: \n")
        desc = input("Пожалуйста, укажите описание: \n")
        new_list = List(name, deadline, desc)
        self.lists.append(new_list)

    def show_lists(self):
        for index, task in enumerate(self.lists):
            print(f"Индекс {index} \n", task)

    def delete_list(self):
        name_list = input("Введите название задачи для удаления: ")
        for index, task in enumerate(self.lists):
            if name_list == task.name:
                del self.lists[index]
                print(f"Задача '{name_list}' удалена.")
                return
        print(f"Задача '{name_list}' не найдена.")

    def edit(self):
        indexx = int(input("Введите индекс задачи для редактирования: "))
        for index, note in enumerate(self.lists):
            if indexx == index:
                print(f"Вы выбрали {note}")
                if input("Правильно?(Y,N): ") == "Y":
                    new_name = input("Напишите новое имя (Пропустить - Enter): ")
                    new_desc = input("Напишите новое описание (Пропустить - Enter): ")
                    new_deadli = input("Напишите новую дату (Пропустить - Enter): ")

                    if new_name:
                        note.name = new_name
                    if new_desc:
                        note.desc = new_desc
                    if new_deadli:
                        note.deadline = new_deadli
                    print("Задача обновлена.")
                    return

        print("Не найдена задача по указанному индексу.")

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            json.dump([task.__dict__ for task in self.lists], file)
        return "Задачи сохранены."

    def load_tasks(self, filename):
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            self.lists = [List(**data) for data in tasks_data]
        return "Задачи загружены."

# Запуск программы

main = DoList()

while True:
    command = input("Выберите команду: (Сохранить, Показать, Добавить, Редактировать, Удалить, Выход)\n")

    if command.upper() == "СОХРАНИТЬ":
        print(main.save_tasks("tasks.json"))
    elif command.upper() == "ПОКАЗАТЬ":
        main.show_lists()
    elif command.upper() == "ДОБАВИТЬ":
        main.addList()
    elif command.upper() == "РЕДАКТИРОВАТЬ":
        main.edit()
    elif command.upper() == "УДАЛИТЬ":
        main.delete_list()
    elif command.upper() == "ВЫХОД":
        break

print("Спасибо за использование")