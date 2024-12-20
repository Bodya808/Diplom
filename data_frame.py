import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Шаг 1: Создание DataFrame с данными
countries = ['США', 'Германия', 'Великобритания', 'Франция', 'Япония']
gdp = [21300, 3800, 2800, 2700, 5000]  # ВВП в миллиардах долларов
unemployment_rate = [6.0, 4.0, 4.5, 7.1, 2.8]  # Уровень безработицы в %

data = pd.DataFrame({
    'Страна': countries,
    'ВВП ($ млрд)': gdp,
    'Уровень безработицы (%)': unemployment_rate
})

data.set_index('Страна', inplace=True)
print("DataFrame:")
print(data)

# Шаг 2: Сохранение DataFrame в Excel
data.to_excel('экономические_показатели.xlsx', index=True)
print("\nДанные сохранены в файл 'экономические_показатели.xlsx'.")