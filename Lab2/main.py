from googletrans import Translator, LANGUAGES


# Функція для перекладу тексту
def TransLate(text, lang):
    translator = Translator()
    translation = translator.translate(text, dest=lang)
    return translation.text


# Функція для визначення мови тексту та її достовірності
def LangDetect(text):
    translator = Translator()
    detected_lang = translator.detect(text)
    return detected_lang.lang, detected_lang.confidence


# Функція для отримання коду мови за назвою або назви за кодом
def CodeLang(lang):
    lang = lang.lower()
    if lang in LANGUAGES:
        return lang
    else:
        for code, name in LANGUAGES.items():
            if lang == name.lower():
                return code
    return None


# Основна програма
if __name__ == "__main__":
    while True:
        print("Меню:")
        print("1. Перекласти текст")
        print("2. Визначити мову тексту")
        print("3. Вийти")
        choice = input("Оберіть опцію: ")

        if choice == "1":
            text = input("Введіть текст для перекладу: ")
            target_lang = input("Введіть мову, на яку перекласти текст: ")
            translated_text = TransLate(text, target_lang)
            print(f"Переклад: {translated_text}")

        elif choice == "2":
            text = input("Введіть текст для визначення мови: ")
            detected_lang, confidence = LangDetect(text)
            language_name = LANGUAGES.get(detected_lang, "Невідома")
            print(f"Мова тексту: {language_name} (Достовірність: {confidence})")

        elif choice == "3":
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")