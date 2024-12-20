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

# Линейный график ВВП с помощью Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['ВВП ($ млрд)'], marker='o', label='ВВП', color='blue', linewidth=2)
plt.title('ВВП стран (Matplotlib)')
plt.xlabel('Страны')
plt.ylabel('ВВП ($ млрд)')
plt.grid(True)
plt.legend()
plt.show()

# Линейный график уровня безработицы с помощью Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Уровень безработицы (%)'], marker='s', label='Уровень безработицы', color='red',
         linestyle='--', linewidth=2)
plt.title('Уровень безработицы стран (Matplotlib)')
plt.xlabel('Страны')
plt.ylabel('Уровень безработицы (%)')
plt.grid(True)
plt.legend()
plt.show()

# Линейный график ВВП с помощью Seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(x=data.index, y=data['ВВП ($ млрд)'], marker='o', color='blue', label='ВВП')
plt.title('ВВП стран (Seaborn)')
plt.xlabel('Страны')
plt.ylabel('ВВП ($ млрд)')
plt.grid(True)
plt.legend()
plt.show()

# Линейный график уровня безработицы с помощью Seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(x=data.index, y=data['Уровень безработицы (%)'], marker='s', color='red', label='Уровень безработицы')
plt.title('Уровень безработицы стран (Seaborn)')
plt.xlabel('Страны')
plt.ylabel('Уровень безработицы (%)')
plt.grid(True)
plt.legend()
plt.show()

# Линейный график ВВП с помощью Plotly
fig = px.line(data, x=data.index, y='ВВП ($ млрд)', title='ВВП стран (Plotly)', markers=True)
fig.update_layout(xaxis_title="Страны", yaxis_title="ВВП ($ млрд)")
fig.show()

# Линейный график уровня безработицы с помощью Plotly
fig = px.line(data, x=data.index, y='Уровень безработицы (%)', title='Уровень безработицы стран (Plotly)', markers=True)
fig.update_layout(xaxis_title="Страны", yaxis_title="Уровень безработицы (%)")
fig.show()
