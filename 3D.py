import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Данные
cities = ['Los Angeles', 'Tokyo', 'London', 'Berlin', 'Paris']
energy_consumption = [4200, 3600, 4800, 3100, 4500]
air_pollution = [75, 60, 85, 50, 65]

# Создание DataFrame
data_2 = pd.DataFrame({
    'Потребление электроэнергии (кВт·ч)': energy_consumption,
    'Уровень загрязнения воздуха (мкг/м³)': air_pollution
}, index=cities)

# Построение 3D графика
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Извлечение данных
x = data_2['Потребление электроэнергии (кВт·ч)']
y = data_2['Уровень загрязнения воздуха (мкг/м³)']
z = np.arange(len(data_2))

# Построение графика
sc_energy = ax.scatter(x, y, z, c=energy_consumption, cmap='coolwarm', marker='o', s=150, edgecolor='k', label='Энергия')
sc_pollution = ax.scatter(x, y, z, c=air_pollution, cmap='viridis', marker='^', s=100, edgecolor='k', alpha=0.7, label='Загрязнение')

# Добавление легенды
ax.legend(loc='upper right', fontsize=10, markerscale=1.5)

# Добавление аннотаций
for i, city in enumerate(cities):
    ax.text(x.iloc[i], y.iloc[i], z[i], city, fontsize=10, ha='center', va='bottom', color='dimgray', backgroundcolor='w', alpha=0.7)

# Настройка осей
ax.set_xlabel('Потребление электроэнергии (кВт·ч)', fontsize=12, labelpad=15)
ax.set_ylabel('Уровень загрязнения воздуха (мкг/м³)', fontsize=12, labelpad=15)
ax.set_zlabel('Города', fontsize=12, labelpad=15)
ax.set_zticks(z)
ax.set_zticklabels(data_2.index, fontsize=10)

# Добавление цветовой шкалы
cbar_energy = plt.colorbar(sc_energy, ax=ax, shrink=0.5, aspect=5, pad=0.1, fraction=0.05)
cbar_energy.set_label('Потребление электроэнергии (кВт·ч)', fontsize=10)

cbar_pollution = plt.colorbar(sc_pollution, ax=ax, location='right', shrink=0.5, aspect=5, pad=0.1, fraction=0.05)
cbar_pollution.set_label('Уровень загрязнения (мкг/м³)', fontsize=10)

# Настройка угла обзора
ax.view_init(elev=30, azim=135)

# Заголовок
plt.title('Анализ Энергопотребления и Загрязнения Воздуха', fontsize=16, pad=30)

# Ручная настройка макета
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

plt.show()
