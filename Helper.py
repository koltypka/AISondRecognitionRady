import argparse

def format_timestamp(seconds):
    ms = int((seconds % 1) * 1000)
    s = int(seconds % 60)
    m = int((seconds // 60) % 60)
    h = int(seconds // 3600)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

def get_path():
    "Получение аргументов из командой строки"
    parser = argparse.ArgumentParser(description="Скрипт для обработки файла.")
    parser.add_argument("-p", "--path", help="Путь к файлу для обработки", required=True)
    args = parser.parse_args()

    return args.path