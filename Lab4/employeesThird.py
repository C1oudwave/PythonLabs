import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Определение функции для вычисления возраста
def calculate_age(birthdate):
    today = datetime.now()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def read_csv_file(file_path):
    try:
        data = pd.read_csv(file_path, encoding='cp1251')
        return data
    except FileNotFoundError:
        print("Помилка: Файл CSV не знайден.")
        return None
    except Exception as e:
        print(f"Помилка при читанні файлу: {str(e)}")
        return None

def analyze_gender(data):
    if data is not None:
        gender_counts = data['Стать'].value_counts()
        print("Кількість співробітників по статі:")
        print(gender_counts)

        gender_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title('Розподіл співоробітників по статі')
        plt.ylabel('')  # Убираем название оси y
        plt.show()

def analyze_age_categories(data):
    if data is not None:
        # Вычисление возраста и добавление его в DataFrame
        data['Вік'] = data['Дата Народження'].apply(calculate_age)

        age_bins = [0, 18, 45, 70, data['Вік'].max()]
        age_labels = ["Молодші 18", "18-45", "45-70", "Старші 70"]

        data['Вікова категорія'] = pd.cut(data['Вік'], bins=age_bins, labels=age_labels)

        age_category_counts = data['Вікова категорія'].value_counts()
        print("Кількість співробітників по різній категорії:")
        print(age_category_counts)

        age_category_counts.plot(kind='bar')
        plt.xlabel('Вікова категорія')
        plt.ylabel('Кількість співробітників')
        plt.title('Кількість співробітників по різній категорії')
        plt.show()

def analyze_gender_and_age_categories(data):
    if data is not None:
        gender_age_counts = data.groupby(['Стать', 'Вікова категорія']).size().unstack(fill_value=0)
        print("Кількість співробітників по статі и віковим категоріям:")
        print(gender_age_counts)

        gender_age_counts.plot(kind='bar', stacked=True)
        plt.xlabel('Вікова категорія')
        plt.ylabel('Кількість співробітників')
        plt.title('Кількість співробітників по різній категорії')
        plt.legend(title='Стать')
        plt.show()


file_path = 'employees.csv'
employee_data = read_csv_file(file_path)
if employee_data is not None:
    analyze_gender(employee_data)
    analyze_age_categories(employee_data)
    analyze_gender_and_age_categories(employee_data)
