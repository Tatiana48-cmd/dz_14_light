import os
import shutil
import platform
import time

project_path = os.path.dirname(os.path.abspath(__file__)) # Корень проекта

# def new_folder(folder_name):
#     if not os.path.exists(folder_name):
#         os.makedirs(folder_name)
#         print(f"Папка `{folder_name}` создана")
#     else:
#         print(f"Папка `{folder_name}` уже существует, всё в порядке!")

''' 
Следуюший тернарный оператор, хоть и работает, но некорректно:
после создания папки нужно обязательно выйти из основной программы. 
Кроме того, не удаётся вывести принт о том, что папка создана. 
Это происходит оттого, что что тернарный оператор в Python возвращает значение,
но не выполняет действия, если они не связаны с возвратом значения.
Поэтому лучше использовать исходный простой код.
'''
def new_folder(folder_name):
    _ = os.makedirs(folder_name) if not os.path.exists(folder_name) else print(f"Папка `{folder_name}` уже существует, всё в порядке!")

def delete_path(name):
    """Удаляет файл или папку в текущей директории."""
    # Определяем путь к текущей директории (где находится этот скрипт)
    full_path = os.path.join(project_path, name)

    if os.path.exists(full_path):
        if os.path.isfile(full_path):  # Если это файл
            os.remove(full_path)
            print(f"Файл '{name}' удалён.")
        elif os.path.isdir(full_path):  # Если это папка
            shutil.rmtree(full_path)
            print(f"Папка '{name}' удалена.")
    else:
        print(f"Объект '{name}' не найден.")

def copy_path(src_name, new_name):
    """Копирует файл или папку в ту же директорию с новым именем."""
    #project_path = os.path.dirname(os.path.abspath(__file__))  # Определяем текущую директорию
    src_path = os.path.join(project_path, src_name)  # Путь к исходному объекту
    dst_path = os.path.join(project_path, new_name)  # Новый путь с новым именем

    if os.path.exists(src_path):
        if os.path.isfile(src_path):  # Если файл
            shutil.copy2(src_path, dst_path)
            print(f"Файл '{src_name}' скопирован как '{new_name}'.")
        elif os.path.isdir(src_path):  # Если папка
            shutil.copytree(src_path, dst_path)
            print(f"Папка '{src_name}' скопирована как '{new_name}'.")
    else:
        print(f"Объект '{src_name}' не найден.")

def directory_view(project_path):

    # Получаем список файлов
    files = os.listdir(project_path)

    # Выводим список файлов
    print(f'Список объектов в директории: ', files)

# Используется генератор списка
def get_subdirectories(project_path):
    return [name for name in os.listdir(project_path) if os.path.isdir(os.path.join(project_path, name))]

# Используется генератор списка
def get_files(project_path):
    return [name for name in os.listdir(project_path) if os.path.isfile(os.path.join(project_path, name))]

# Декоратор для измерения времени выполнения
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Засекаем время начала выполнения
        result = func(*args, **kwargs)  # Вызываем оригинальную функцию
        end_time = time.time()  # Засекаем время окончания выполнения
        print(f"Функция {func.__name__} выполнилась за {end_time - start_time:.4f} секунд")
        return result
    return wrapper

# Применяем декоратор к функции
@timer_decorator
def get_system_info():
    info = {
        "ОС": platform.system(),
        "Версия ОС": platform.version(),
        "Имя устройства": platform.node(),
        "Архитектура": platform.architecture()[0],
        "Процессор": platform.processor(),
        "Количество ядер": os.cpu_count(),
    }
    return info

# def get_system_info():
#     info = {
#         "ОС": platform.system(),
#         "Версия ОС": platform.version(),
#         "Имя устройства": platform.node(),
#         "Архитектура": platform.architecture()[0],
#         "Процессор": platform.processor(),
#         "Количество ядер": os.cpu_count(),
#     }
#     return info

