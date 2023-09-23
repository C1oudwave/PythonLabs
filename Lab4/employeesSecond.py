import csv
import openpyxl
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from datetime import datetime

try:
    data = pd.read_csv('employees.csv', delimiter=',', encoding='cp1251')

    workbook = Workbook()

    # Створюємо лист "all" та встановлюємо його як активний
    ws_all = workbook.active
    ws_all.title = "all"

    # Встановлюємо заголовок для листа "all"
    header_all = ["Прізвище", "Ім'я", "По-батькові", "Стать", "Дата народження", "Посада", "Місто проживання",
                  "Адреса проживання", "Телефон", "Email", "Вік"]
    ws_all.append(header_all)

    for row in dataframe_to_rows(data, index=False, header=False):
        birthdate = row[4]

        try:
            birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
            age = datetime.now().year - birthdate.year
        except (TypeError, ValueError):
            age = None

        ws_all.append(row + [age])

    sheets = ["younger than 18", "18-45", "45-70", "older than 70"]

    for sheet_name in sheets:
        # Створюємо інші листи та встановлюємо їх як активні
        ws = workbook.create_sheet(sheet_name)
        workbook.active = ws

        # Встановлюємо заголовок для інших листів
        header_filtered = ["N", "Прізвище", "Ім'я", "По-батькові", "Дата народження", "Вік"]
        ws.append(header_filtered)

        if "younger" in sheet_name:
            max_age = 18
            min_age = None
        elif "older" in sheet_name:
            min_age = 71
            max_age = None
        else:
            min_age, max_age = map(int, sheet_name.split('-'))

        for index, row in enumerate(data.iterrows(), start=1):
            _, data_row = row
            birthdate = data_row['Дата Народження']

            try:
                birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
                age = datetime.now().year - birthdate.year
            except (TypeError, ValueError):
                age = None

            if "younger" in sheet_name and age is not None and age < max_age:
                ws.append([index] + data_row[['Прізвище', 'Ім\'я', 'По-батькові', 'Дата Народження']].tolist() + [age])
            elif "older" in sheet_name and age is not None and age >= min_age:
                ws.append([index] + data_row[['Прізвище', 'Ім\'я', 'По-батькові', 'Дата Народження']].tolist() + [age])
            elif min_age is not None and max_age is not None and min_age <= age <= max_age:
                ws.append([index] + data_row[['Прізвище', 'Ім\'я', 'По-батькові', 'Дата Народження']].tolist() + [age])

    workbook.save('employees.xlsx')
    print("Готово! Файл employees.xlsx створено!")
except FileNotFoundError:
    print("Помилка: Файл CSV не знайден.")
except Exception as e:
    print(f"Помилка: {str(e)}")
else:
    print("Програма успішно завершила свою роботу!")
