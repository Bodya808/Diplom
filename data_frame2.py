import pandas as pd

# Данные
cities = ['Los Angeles', 'Tokyo', 'London', 'Berlin', 'Paris']
energy_consumption = [4200, 3600, 4800, 3100, 4500]  # Потребление электроэнергии в кВт·ч
air_pollution = [75, 60, 85, 50, 65]  # Уровень загрязнения воздуха в мкг/м³

# Создание DataFrame
data_2 = pd.DataFrame({
    'Потребление электроэнергии (кВт·ч)': energy_consumption,
    'Уровень загрязнения воздуха (мкг/м³)': air_pollution
}, index=cities)

print("DataFrame:")
print(data_2)

# Шаг 2: Сохранение DataFrame в Excel
data_2.to_excel('energy_pollution_data.xlsx', index=False)
print("\nДанные сохранены в файл 'экономические_показатели.xlsx'.")