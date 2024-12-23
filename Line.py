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



# Линейный график ВВП с Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['ВВП ($ млрд)'], marker='o', color='teal', linewidth=2)
plt.title('ВВП стран (Matplotlib)', fontsize=14)
plt.xlabel('Страны', fontsize=12)
plt.ylabel('ВВП ($ млрд)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Линейный график уровня безработицы с Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Уровень безработицы (%)'], marker='s', linestyle='--', color='darkred', linewidth=2)
plt.title('Уровень безработицы стран (Matplotlib)', fontsize=14)
plt.xlabel('Страны', fontsize=12)
plt.ylabel('Уровень безработицы (%)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Линейный график ВВП с Seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(x=data.index, y=data['ВВП ($ млрд)'], marker='o', color='teal', linewidth=2)
plt.title('ВВП стран (Seaborn)', fontsize=14)
plt.xlabel('Страны', fontsize=12)
plt.ylabel('ВВП ($ млрд)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Линейный график уровня безработицы с Seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(x=data.index, y=data['Уровень безработицы (%)'], marker='s', color='darkred', linewidth=2, linestyle='--')
plt.title('Уровень безработицы стран (Seaborn)', fontsize=14)
plt.xlabel('Страны', fontsize=12)
plt.ylabel('Уровень безработицы (%)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Линейный график ВВП с Plotly
fig = px.line(data, x=data.index, y='ВВП ($ млрд)', title='ВВП стран (Plotly)', markers=True,
              color_discrete_sequence=['teal'], template='plotly_white')
fig.update_layout(xaxis_title="Страны", yaxis_title="ВВП ($ млрд)", xaxis_tickangle=45)
fig.show()

# Линейный график уровня безработицы с Plotly
fig = px.line(data, x=data.index, y='Уровень безработицы (%)', title='Уровень безработицы стран (Plotly)', markers=True,
              color_discrete_sequence=['darkred'], template='plotly_white')
fig.update_layout(xaxis_title="Страны", yaxis_title="Уровень безработицы (%)", xaxis_tickangle=45)
fig.show()
