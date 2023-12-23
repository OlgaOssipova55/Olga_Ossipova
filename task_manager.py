import json

class Task:
    def __init__(self, name, deadline, description):
        self.name = name
        self.deadline = deadline
        self.description = description

    def __str__(self):
        return f"Задача: {self.name}   Срок: {self.deadline}\n   Описание: {self.description}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, deadline, description):
        new_task = Task(name, deadline, description)
        self.tasks.append(new_task)

    def show_tasks(self):
        return '\n'.join(str(task) for task in self.tasks)

    def delete_task(self, task_name):
        self.tasks = [task for task in self.tasks if task.name != task_name]

    def update_task(self, index, name, deadline, description):
        if 0 <= index < len(self.tasks):
            if name:
                self.tasks[index].name = name
            if deadline:
                self.tasks[index].deadline = deadline
            if description:
                self.tasks[index].description = description
            return True
        return False

    def save_tasks_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                json.dump([task.__dict__ for task in self.tasks], file)
            return "Задачи сохранены."
        except IOError as e:
            return f"Ошибка сохранения: {e}"

    def load_tasks_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task(**data) for data in tasks_data]
            return "Задачи загружены."
        except IOError as e:
            return f"Ошибка загрузки: {e}"
        
    def get_task(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        return None  # или поднимать исключение, или обрабатывать этот случай как-то иначе
    

    def update_task(self, index, name, deadline, description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].name = name
            self.tasks[index].deadline = deadline
            self.tasks[index].description = description
            return True
        else:
            return False


