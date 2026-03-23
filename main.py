from SpeechClassify import get_language
from SpeechRecognition import transcribe
from Converter import convert

file_path = "data/Деревяшки Тук тук тук DMX MESHUP AI.mp3"
converted_path = convert(file_path)

print("Определяем язык...")
detected_lang = get_language(converted_path)
print(f"Обнаружен язык: {detected_lang}")

print("Начинаем распознавание...")
text = transcribe(converted_path, detected_lang)

with open("result//subtitles.srt", "w", encoding="utf-8") as f:
    f.write(text)
