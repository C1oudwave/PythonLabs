from googletrans import Translator, LANGUAGES
from tabulate import tabulate
import pandas as pd

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translator = Translator()
        translated_text = translator.translate(text, src=scr, dest=dest)
        return translated_text.text
    except Exception as e:
        return str(e)

def LangDetect(text: str, set: str = "all"):
    try:
        translator = Translator()
        result = translator.detect(text)

        detected_lang = result.lang
        confidence = result.confidence

        if set == "lang":
            return detected_lang
        elif set == "confidence":
            return confidence
        else:
            return detected_lang, confidence
    except Exception as e:
        return str(e)

def CodeLang(lang: str) -> str:
    translator = Translator()
    lang = lang.lower()

    if lang in LANGUAGES:
        language_name = LANGUAGES[lang]
        return language_name.capitalize()
    else:
        try:
            translation = translator.translate(lang, src='en', dest='en')
            for code, name in LANGUAGES.items():
                if name.lower() == translation.text.lower():
                    return code
            return "Не знайдено мову"
        except Exception as e:
            return str(e)

def LanguageList(out="screen", text=None):
    try:
        languages = list(LANGUAGES.values())
        codes = list(LANGUAGES.keys())
        data = {"N": range(1, len(languages) + 1), "Language": languages, "ISO-639 code": codes}
        if text:
            translations = [TransLate(text, "auto", lang) for lang in codes]
            data["Text"] = translations

        df = pd.DataFrame(data)

        if out == "screen":
            print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))
            return "Ok"
        elif out == "file":
            filename = "LanguageList_gtrans.txt"
            with open(filename, "w", encoding='utf-8') as file:
                file.write(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))
            return f"Таблиця збережена у файлі: {filename} \n Ok"
        else:
            return "Недійсний параметр 'out'"
    except Exception as e:
        return f"Помилка: {e}"