import os
import re
import sys

BASE_NAME_PROJECT = "baseProject"
DIRS = ["baseProject", ".gitignore"]


def rename_base_project(new_name=None):
    """Перебираем все файлы и меняем базовое имя проекта на новое"""
    # Выход в родительскую dir project
    os.chdir("..")

    is_dir = os.getcwd()

    # Рекурсивный обход всех файлов в директории
    for root, dirs, files in os.walk(is_dir):
        dirs = [dir for dir in dirs if dir not in IGNOR]
        files = [file for file in files if file not in IGNOR]

        print(files)
        #
        # for file in files:  # Переименование файлов
        #     file_path = os.path.join(root, file)
        #     try:
        #         # Чтение содержимого файла
        #         with open(file_path, 'r', encoding='utf-8') as f:
        #             content = f.read()
        #
        #         # Замена старого имени на новое
        #         new_content = re.sub(BASE_NAME_PROJECT, new_name, content)
        #
        #         # Запись измененного содержимого обратно в файл
        #         with open(file_path, 'w', encoding='utf-8') as f:
        #             f.write(new_content)
        #
        #         print(f"Файл {file_path} обработан.")
        #     except Exception as e:
        #         print(f"Произошла ошибка: {e}")
        #
        # for file in files:
        #     file_path = os.path.join(root, file)
        #     try:
        #         # Чтение содержимого файла
        #         with open(file_path, 'r', encoding='utf-8') as f:
        #             content = f.read()
        #
        #         # Замена старого имени на новое
        #         new_content = re.sub(BASE_NAME_PROJECT, new_name, content)
        #
        #         # Запись измененного содержимого обратно в файл
        #         with open(file_path, 'w', encoding='utf-8') as f:
        #             f.write(new_content)
        #
        #         print(f"Файл {file_path} обработан.")
        #     except Exception as e:
        #         print(f"Произошла ошибка: {e}")





if __name__ == "__main__":
    rename_base_project()
