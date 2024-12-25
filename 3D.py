import plotly.express as px
import pandas as pd

# Данные
cities = ['Los Angeles', 'Tokyo', 'London', 'Berlin', 'Paris']
energy_consumption = [4200, 3600, 4800, 3100, 4500]
air_pollution = [75, 60, 85, 50, 65]

# Создание DataFrame
df = pd.DataFrame({
    'Город': cities,
    'Потребление электроэнергии (кВт·ч)': energy_consumption,
    'Уровень загрязнения воздуха (мкг/м³)': air_pollution
})

# Построение 3D графика
fig = px.scatter_3d(df, x='Потребление электроэнергии (кВт·ч)', y='Уровень загрязнения воздуха (мкг/м³)',
                    z='Город', color='Потребление электроэнергии (кВт·ч)', size_max=18,
                    color_continuous_scale='Viridis',
                    title='Анализ энергопотребления и загрязнения воздуха',
                    labels={'Потребление электроэнергии (кВт·ч)': 'Потребление электроэнергии (кВт·ч)',
                            'Уровень загрязнения воздуха (мкг/м³)': 'Уровень загрязнения воздуха (мкг/м³)'},
                   )

# Обновление параметров фигуры
fig.update_traces(marker=dict(size=12),
                  selector=dict(mode='markers'))

# Показ графика
fig.show()
