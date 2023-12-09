'''# класс Календарь
from datetime import datetime, timedelta

class Calendar:
    def __init__(self) :
        self.events = []

    def add(self,year,mouth,day, event="") :
        event_date = datetime(year, mouth, day)
        self.events.append((event_date, event))

    def show_day(self, data):
        for event_date, event in self.events:
            if data.date() == event_date.date():  # Сравниваем только даты, без времени
                formatted_date = event_date.strftime("%Y-%m-%d")
                print(f"{formatted_date} \nбудет такое мероприятие: {event}")
                return
        
            

    def delete(self, date):
        index = 0
        while index < len(self.events):
            event_date, _ = self.events[index]
            if event_date.date() == date.date():
                print("Удалили дату ",event_date.date()  )
                del self.events[index]
                return
            else:
                index += 1
        print("Таккого событяе нету")
    
    def show_events(self,days):
        current_time = datetime.now()
        for index in range(days):
            new_time = current_time + timedelta(days=index)
            self.show_day(new_time)


        

#START

cal = Calendar()
# Добавление событий для примера
cal.add(2023, 12, 15, "Событие 1")
cal.add(2023, 12, 16, "Событие 2")
cal.add(2023, 12, 17, "Событие 3")

# Отображение событий на протяжении 10 дней
cal.show_events(17)'''

'''class Item:
    def __init__(self,name,count,price) :
        self.name=name
        self.count=count
        self.price=price
    
    def __str__(self):
        return f"Название:{self.name} \nКоличество: {self.count}\nЦена:{self.price}\n-----------------"


class InvetoryItem():
    def __init__(self):
        self.items=[]

    def addItem(self, name,count,price):
        item=Item(name,count,price)
        self.items.append(item)

    def show(self):
        for i in self.items: print(i)
    
    def plusCount(self,name,count):
        for item in self.items: 
            if (item.name==name):
                item.count+=count
                return


    def minusCount(self,name,count):
        for item in self.items: 
            if (item.name==name):
                item.count-=count
                return
            
    def priceItem(self):
        chet=0
        for item in self.items: 
            chet+=item.count*item.price

        print( "Общая стоимость инветоря: ",chet )
        


item=InvetoryItem()

item.addItem("Баунти",10,120)
item.addItem("Сарыгашка", 20,210)
item.show()
item.minusCount("Баунти",20)
item.show()
item.priceItem()'''

'''class Students:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def print_info(self):
        print(f"Студент: {self.name}, успеваемость: {self.grades}")

    def average(self):
        aver = sum(self.grades) / len(self.grades)
        print(f"Успеваемость: {aver}, студент: {self.name}")

# Пример использования
student1 = Students("Иван", [4, 3.3, 4, 5, 3, 2, 1])
student1.print_info()
student1.average()'''


class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def make_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        else:
            print("Некорректный ход. Попробуйте еще раз.")
            return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Проверка строк и столбцов
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ' or \
               self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True

        # Проверка диагоналей
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ' or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True

        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def play_game(self):
        while True:
            self.print_board()
            row = int(input("Введите номер строки (0, 1, 2): "))
            col = int(input("Введите номер столбца (0, 1, 2): "))

            if self.make_move(row, col):
                if self.check_winner():
                    self.print_board()
                    print(f"Игрок {self.current_player} победил!")
                    break
                elif self.check_draw():
                    self.print_board()
                    print("Ничья!")
                    break
                else:
                    self.switch_player()

# Пример использования класса:
game = TicTacToe()
game.play_game()