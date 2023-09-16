from MyPackageTest.module1 import *

text = "Доброго ранку"

# Визначення мови тексту
detected_lang = LangDetect(text, set="lang")
print(f"Мова тексту: {detected_lang}")

print("------------------------")

dest_lang = "en"
translation = TransLate(text, scr=detected_lang, dest=dest_lang)
print(f"Перекладено з {detected_lang} на {dest_lang}: {translation}")

print("------------------------")

lang_name = "English"
lang_code = CodeLang(lang_name)
print(f"Код мови для {lang_name}: {lang_code}")

print("------------------------")

lang_code = "en"
lang_name = CodeLang(lang_code)
print(f"Мова для {lang_code}: {lang_name}")

print("------------------------")

print("\nLanguageList функція:")
result = LanguageList(out="file", text=text)
print(result)