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

# Подготовка цветовой палитры
colors = sns.color_palette('pastel')

# ВВП
plt.figure(figsize=(8, 8))
plt.pie(data['ВВП ($ млрд)'], labels=data.index, autopct='%1.1f%%', startangle=140,
        shadow=True, colors=colors)
plt.title('Доля ВВП стран (Matplotlib)', fontsize=16)
plt.axis('equal')
plt.show()

# Уровень безработицы
plt.figure(figsize=(8, 8))
plt.pie(data['Уровень безработицы (%)'], labels=data.index, autopct='%1.1f%%', startangle=90,
        shadow=True, colors=colors)
plt.title('Уровень безработицы стран (Matplotlib)', fontsize=16)
plt.axis('equal')
plt.show()

# ВВП
fig = px.pie(data, values='ВВП ($ млрд)', names=data.index, title='Доля ВВП стран (Plotly)',
             hole=0.1, hover_data=['Уровень безработицы (%)'], template='presentation')
fig.update_traces(textinfo='percent+label', textfont_size=14)
fig.show()

# Уровень безработицы
fig = px.pie(data, values='Уровень безработицы (%)', names=data.index, title='Уровень безработицы стран (Plotly)',
             hole=0.1, hover_data=['ВВП ($ млрд)'], template='presentation')
fig.update_traces(textinfo='percent+label', textfont_size=14)
fig.show()
