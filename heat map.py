import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import seaborn as sns
from data_frame2 import data_2

# 1 Matplotlib
# Двухмерный массив данных
heat_data = np.array([data_2['Потребление электроэнергии (кВт·ч)'], data_2['Уровень загрязнения воздуха (мкг/м³)']])

# Тепловая карта
plt.figure(figsize=(8, 5))
plt.imshow(heat_data, cmap='coolwarm', aspect='auto')
plt.colorbar(label='Значение')
plt.xticks(range(len(data_2.index)), data_2.index, rotation=45)
plt.yticks([0, 1], ['Потребление электроэнергии', 'Уровень загрязнения'])
plt.title('Тепловая карта (Matplotlib)')
plt.show()

# 2. Seaborn:


# Подготовка данных для тепловой карты
heat_data = data_2.transpose()

# Тепловая карта
plt.figure(figsize=(8, 5))
sns.heatmap(heat_data, annot=True, cmap='coolwarm', fmt='g', cbar_kws={'label': 'Значение'},
            xticklabels=data_2.index, yticklabels=['Потребление электроэнергии', 'Уровень загрязнения'])
plt.title('Тепловая карта (Seaborn)')
plt.show()

# 3. Plotly:


# Подготовка данных для тепловой карты в Plotly
heat_data = data_2.T

# Тепловая карта
fig = px.imshow(heat_data, labels=dict(x='Город', y='Показатель', color='Значение'),
                x=data_2.index, y=['Потребление электроэнергии', 'Уровень загрязнения'],
                color_continuous_scale='Viridis')
fig.update_layout(title='Тепловая карта (Plotly)', xaxis_nticks=len(data_2.index))
fig.show()
