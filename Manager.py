from SpeechClassify import get_language
from SpeechRecognition import transcribe
from Converter import convert
from Helper import get_path

def run():
    file_path = get_path()
    converted_path = convert(file_path)

    print("Определяем язык...")
    detected_lang = get_language(converted_path)
    print(f"Обнаружен язык: {detected_lang}")

    print("Начинаем распознавание...")
    text = transcribe(converted_path, detected_lang)

    path_to_save = "result//subtitles.srt"
    with open(path_to_save, "w", encoding="utf-8") as f:
        f.write(text)
        print(f"Файл сохранён по пути: {path_to_save}")