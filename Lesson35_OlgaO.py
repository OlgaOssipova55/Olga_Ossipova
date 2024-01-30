# Совмещенные графики
'''import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка набора данных tips из Seaborn
tips = sns.load_dataset('tips')

# Построение гистограммы для total_bill
sns.histplot(tips['total_bill'], kde=False, color='skyblue', alpha=0.7, label='Total Bill')

# Добавление гистограммы для tip
sns.histplot(tips['tip'], kde=False, color='salmon', alpha=0.7, label='Tip')

# Добавление легенды
plt.legend()

# Настройка внешнего вида графика
plt.title('Total Bill vs Tip')  # заголовок
plt.xlabel('Amount')           # подпись оси x
plt.ylabel('Frequency')         # подпись оси y
plt.grid(True)                 # добавление сетки
plt.show()                     # отображение графика'''


# тепловая карта корреляции
'''import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")
flights = flights.pivot_table(index='month', columns='year', values='passengers')

sns.heatmap(flights, cmap="YlGnBu")
plt.title('Correlation between Months and Passengers Transport')
plt.show()'''

# ящик с усами

import seaborn as sns
import matplotlib.pyplot as plt

diamonds = sns.load_dataset("diamonds")

sns.boxplot(x='cut', y='price', data=diamonds, palette="Set3")
plt.title('Price Distribution by Cut Quality')
plt.show()