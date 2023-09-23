import csv
import openpyxl
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from datetime import datetime

try:
    data = pd.read_csv('employees.csv', delimiter=',', encoding='cp1251')

    workbook = Workbook()

    sheets = ["all", "younger than 18", "18-45", "45-70", "older than 70"]
    for sheet_name in sheets:
        workbook.create_sheet(sheet_name)

    default_sheet = workbook['Sheet']
    workbook.remove(default_sheet)

    ws_all = workbook['all']
    for row in dataframe_to_rows(data, index=False, header=False):
        birthdate = row[4]

        try:
            birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
            age = datetime.now().year - birthdate.year
        except (TypeError, ValueError):
            age = None

        ws_all.append(row + [age])

    today = datetime.now()
    for sheet_name in sheets[1:]:
        ws = workbook[sheet_name]

        if "younger" in sheet_name:
            max_age = 18
            min_age = None
        elif "older" in sheet_name:
            min_age = 71
            max_age = None
        else:
            min_age, max_age = map(int, sheet_name.split('-'))

        for row in dataframe_to_rows(data, index=False, header=False):
            birthdate = row[4]

            try:
                birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
                age = datetime.now().year - birthdate.year
            except (TypeError, ValueError):
                age = None

            if "younger" in sheet_name and age is not None and age < max_age:
                ws.append(row + [age])
            elif "older" in sheet_name and age is not None and age >= min_age:
                ws.append(row + [age])
            elif min_age is not None and max_age is not None and min_age <= age <= max_age:
                ws.append(row + [age])

    workbook.save('employees.xlsx')
    print("Готово! Файл employees.xlsx створено!")
except FileNotFoundError:
    print("Помилка: Файл CSV не знайден.")
except Exception as e:
    print(f"Помилка: {str(e)}")
else:
    print("Програма успішно завершила свою роботу!")
