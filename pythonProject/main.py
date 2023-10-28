import pandas as pd

# Чтение данных из Excel файла
df = pd.read_excel('test.xlsx')

# Создание списка для дублирования
duplicated_data = []
for index, row in df.iterrows():
    duplicated_data.extend([row] * 2)

# Создание нового датафрейма с дубликатами
df_duplicated = pd.DataFrame(duplicated_data)

# Запись обновленных данных в новый файл
df_duplicated.to_excel('ваш_файл_с_дубликатами_по_порядку.xlsx', index=False)