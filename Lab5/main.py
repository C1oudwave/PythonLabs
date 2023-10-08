import re
import locale

# Встановлюємо українську локаль для сортування
locale.setlocale(locale.LC_COLLATE, 'uk_UA.UTF-8')

# Функція для зчитування та обробки текстового файлу
def read_and_process_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()

            # Знаходимо перше речення
            sentences = re.split(r'(?<=[.!?])\s+', text)
            first_sentence = sentences[0] if sentences else ""

            # Виводимо перше речення
            print("Перше речення:")
            print(first_sentence)

            # Знаходимо всі слова та видаляємо знаки пунктуації
            words = re.findall(r'\b\w+\b', text, re.UNICODE)
            words = [word.lower() for word in words]

            # Розділяємо слова на українські та англійські
            ukrainian_words = sorted([word for word in words if re.match("^[а-яїєіґ']+$", word)], key=locale.strxfrm)
            english_words = sorted([word for word in words if re.match("^[a-zA-Z]+$", word)])

            # Виводимо відсортовані слова та їх кількість
            print("\nУкраїнські слова:")
            for word in ukrainian_words:
                print(word)
            print("\nАнглійські слова:")
            for word in english_words:
                print(word)

            print("\nКількість слів у тексті:", len(words))

    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print("Помилка при обробці файлу:", str(e))

# Викликаємо функцію з файлом, який ви хочете обробити
read_and_process_file("example.txt")
