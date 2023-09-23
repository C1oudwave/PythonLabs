import csv
from faker import Faker
import random
from datetime import date, timedelta

fake = Faker()

def random_birthdate():
    start_date = date(1938, 1, 1)
    end_date = date(2008, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

with open('employees.csv', 'w', newline='') as csvfile:
    fieldnames = ['Прізвище', 'Ім\'я', 'По-батькові', 'Стать', 'Дата Народження', 'Посада', 'Місто проживання',
                  'Адреса проживання', 'Телефон', 'Email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for _ in range(2000):
        gender = random.choice(['Чоловік', 'Жінка'])
        last_name = fake.last_name()  # Генеруємо прізвище
        full_name = fake.name_male() if gender == 'Чоловік' else fake.name_female()
        full_name = full_name.split()
        first_name = full_name[0]
        middle_name = full_name[1] if len(full_name) > 1 else ""
        if not middle_name:
            middle_name = None
        birthdate = random_birthdate()
        position = fake.job()
        city = fake.city()
        address = fake.address()
        phone_number = fake.phone_number()
        email = fake.email()

        writer.writerow({
            'Прізвище': last_name,
            'Ім\'я': first_name,
            'По-батькові': middle_name,
            'Стать': gender,
            'Дата Народження': birthdate,
            'Посада': position,
            'Місто проживання': city,
            'Адреса проживання': address,
            'Телефон': phone_number,
            'Email': email
        })

print("Готово! Файл employees.csv створено.")
