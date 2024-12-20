import pandas as pd
import plotly.express as px

# Чтение данных из Excel
file_path = 'экономические_показатели.xlsx'
data = pd.read_excel(file_path, index_col='Страна')

# Преобразуем типы данных
data['ВВП ($ млрд)'] = pd.to_numeric(data['ВВП ($ млрд)'], errors='coerce')
data['Уровень безработицы (%)'] = pd.to_numeric(data['Уровень безработицы (%)'], errors='coerce')

# Нормализуем уровень безработицы для использования в цвете
min_unemp = data['Уровень безработицы (%)'].min()
max_unemp = data['Уровень безработицы (%)'].max()
normalized_unemp = (data['Уровень безработицы (%)'] - min_unemp) / (max_unemp - min_unemp) * 100
data['Normalized Unemployment Rate'] = normalized_unemp

# Создание карты
fig = px.scatter_geo(data,
                     locations=data.index,
                     locationmode='country names',
                     size="ВВП ($ млрд)",
                     color="Normalized Unemployment Rate",
                     hover_name=data.index,
                     hover_data={'ВВП ($ млрд)': True, 'Уровень безработицы (%)': True},
                     color_continuous_scale=px.colors.sequential.Plasma,
                     size_max=60,
                     projection="natural earth")

# Настройка легенды и заголовков осей
fig.update_layout(
    title_text='ВВП и уровень безработицы стран',
    geo=dict(showframe=False),
    legend_title_text='Уровень безработицы'
)

# Отображение карты
fig.show()
