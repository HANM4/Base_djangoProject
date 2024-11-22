import os
import re
import sys

PATH_DIRS_RENAME = (
    "baseProjectRename\\baseProjectRename\\static\\baseProjectRename",
    "baseProjectRename\\baseProjectRename",
    "baseProjectRename"
)
BASE_RENAME_PROJECT = "baseProjectRename"
PATH_FILES_RENAME = (
    ".gitignore",
    "baseProjectRename\\docker-compose.yml",
    "baseProjectRename\\gunicorn_config.py",
    "baseProjectRename\\manage.py",
    "baseProjectRename\\baseProjectRename\\asgi.py",
    "baseProjectRename\\baseProjectRename\\settings.py",
    "baseProjectRename\\baseProjectRename\\urls.py",
    "baseProjectRename\\baseProjectRename\\wsgi.py",
    "gulpfile.js",
    "tailwind.config,js",
    "baseProjectRename\\templates\\index.html"
)


def construct_path(path_dirs: tuple[str] = PATH_DIRS_RENAME,
                   path_files: tuple[str] = PATH_FILES_RENAME) -> list[list[str]]:
    full_paths_dirs = []
    full_paths_files = []
    this_dir = os.path.dirname(os.getcwd())
    for path_dir in path_dirs:
        path = os.path.join(this_dir, path_dir)
        full_paths_dirs.append(path)
    for path_file in path_files:
        path = os.path.join(this_dir, path_file)
        full_paths_files.append(path)
    return [full_paths_dirs, full_paths_files]


def rename_base_project(list_path_dirs_and_files: list[list[str]],
                        new_name: str,
                        old_name: str = BASE_RENAME_PROJECT
                        ) -> None:
    """Перебираем все файлы и меняем базовое имя проекта на новое"""

    list_path_dirs: list[str]
    list_path_files: list[str]
    list_path_dirs, list_path_files = list_path_dirs_and_files

    for path_file in list_path_files:  # Переименование файлов
        try:
            # Чтение содержимого файла
            if os.path.exists(path_file):
                with open(path_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Замена старого имени на новое
                new_content = re.sub(old_name, new_name, content)

                # Запись измененного содержимого обратно в файл
                with open(path_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                print(f"Файл {path_file} обработан.")
            else:
                print(f"Файл {path_file} не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    for path_dir in list_path_dirs:
        try:
            if os.path.exists(path_dir):
                os.rename(path_dir, path_dir[:path_dir.rfind('\\')]+new_name)
                print(f"Дериктория {path_dir} обработан.")
            else:
                print(f"Дериктория {path_dir} не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    rename_base_project(construct_path(), "new_project")
