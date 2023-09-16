from MyPackageTest.module2 import *

text = "Доброго ранку"

detected_lang = LangDetect(text, set="lang")
print(f"Текст: {text}")
print(f"Мова тексту: {detected_lang}")
print("------------------------")

dest_lang = "en"
lang_name = CodeLang(dest_lang)
print(f"Перекладено з {detected_lang} на {lang_name}: {TransLate(text, scr=detected_lang, dest=dest_lang)}")
print("------------------------")

lang_name = "English"
lang_code = CodeLang(lang_name)
print(f"Код мови для {lang_name}: {lang_code}")
print("------------------------")

print("\nLanguageList функція:")
result = LanguageList(out="file", text=text)
print(result)
