import pandas as pd
import plotly.express as px

# Чтение данных из Excel
file_path = 'экономические_показатели.xlsx'
data = pd.read_excel(file_path, index_col='Страна')

# Преобразуем типы данных
data['Normalized Unemployment Rate'] = (data['Уровень безработицы (%)'] - data['Уровень безработицы (%)'].min()) / (data['Уровень безработицы (%)'].max() - data['Уровень безработицы (%)'].min()) * 100

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
    title_text='GDP and Unemployment Rate by Country',
    geo=dict(showframe=False),
    legend_title_text='Unemployment Rate'
)

# Отображение карты
fig.show()