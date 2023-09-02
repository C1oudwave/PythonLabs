from googletrans import Translator, LANGUAGES

# Функція для перекладу тексту
def TransLate(text, lang):

# Функція для визначення мови тексту та її достовірності
def LangDetect(text):

# Функція для отримання коду мови за назвою або назви за кодом
def CodeLang(lang):

# Основна програма
if __name__ == "__main__":
    while True:
        print("Меню:")
        print("1. Перекласти текст")
        print("2. Визначити мову тексту")
        print("3. Вийти")
        choice = input("Оберіть опцію: ")

        if choice == "1":

        elif choice == "2":

        elif choice == "3":
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")