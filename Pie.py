import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Чтение данных из Excel
file_path = 'экономические_показатели.xlsx'
data = pd.read_excel(file_path, index_col='Страна')
# Вывод данных для проверки
print("DataFrame:")
print(data)

# Круговая диаграмма ВВП с помощью Matplotlib
plt.figure(figsize=(8, 8))
plt.pie(data['ВВП ($ млрд)'], labels=data.index, autopct='%1.1f%%', startangle=140)
plt.title('Доля ВВП стран (Matplotlib)')
plt.axis('equal')
plt.show()

# Круговая диаграмма уровня безработицы с помощью Matplotlib
plt.figure(figsize=(8, 8))
plt.pie(data['Уровень безработицы (%)'], labels=data.index, autopct='%1.1f%%', startangle=90)
plt.title('Уровень безработицы стран (Matplotlib)')
plt.axis('equal')
plt.show()


# Круговая диаграмма ВВП с помощью Plotly
fig = px.pie(data, values='ВВП ($ млрд)', names=data.index, title='Доля ВВП стран (Plotly)')
fig.show()

# Круговая диаграмма уровня безработицы с помощью Plotly
fig = px.pie(data, values='Уровень безработицы (%)', names=data.index, title='Уровень безработицы стран (Plotly)')
fig.show()

