import os
import subprocess
import time
import platform
from my_functions import (
    new_folder,
    delete_path,
    copy_path,
    directory_view,
    get_subdirectories,
    get_files,
    get_system_info,
  )

project_path = os.path.dirname(os.path.abspath(__file__))  # Корень проекта

def main():
    while True:
        try:
            print('\n1. Создать папку')
            print('2. Удалить (файл/папку)')
            print('3. Копировать (файл/папку)')
            print('4. Просмотр содержимого рабочей директории')
            print('5. Посмотреть только папки')
            print('6. Посмотреть только файлы')
            print('7. Просмотр информации об операционной системе')
            print('8. Создатель программы')
            print('9. Играть в викторину')
            print('10. Мой банковский счет')
            print('11. Смена рабочей директории (*необязательный пункт)')
            print('12. Выход')

            choice = input('Выберите пункт меню: ')

            # Проверяем, является ли ввод числом
            if not choice.isdigit():
                # Принудительный выход на except, если в качестве пункта меню задана не цифра
                raise TypeError("Неправильный пункт меню: введите число от 1 до 12")

            choice = int(choice)

            if choice == 1:
                folder_name = input('Введите название папки: ')
                new_folder(folder_name)

            elif choice == 2:
                name = input('Введите название файла/папки: ')
                delete_path(name)

            elif choice == 3:
                src_name = input('Введите название файла/папки, который/ую нужно скопировать: ')
                new_name = input('Введите название файла/папки, под которым его/её нужно записать: ')
                copy_path(src_name, new_name)

            elif choice == 4:
                directory_view(project_path)

                # Создаем или пересоздаем файл listdir.txt
                listdir_path = os.path.join(project_path, 'listdir.txt')
                with open(listdir_path, 'w') as f:
                    # Получаем список всех элементов в текущей директории
                    items = os.listdir(project_path)

                    # Разделяем элементы на файлы и папки
                    files = [item for item in items if os.path.isfile(os.path.join(project_path, item))]
                    dirs = [item for item in items if os.path.isdir(os.path.join(project_path, item))]

                    # Записываем файлы
                    f.write('files: ' + ', '.join(files) + '\n')
                    # Записываем папки
                    f.write('dirs: ' + ', '.join(dirs) + '\n')

                print("Файл listdir.txt успешно создан/пересоздан.")

                # Выводим содержимое файла listdir.txt на печать
                with open(listdir_path, 'r') as f:
                    content = f.read()
                    print("\nСодержимое файла listdir.txt:")
                    print(content)

            elif choice == 5:
                folders = get_subdirectories(project_path)
                print(f'Список папок в директории <console file manager>: {", ".join(folders)}')

            elif choice == 6:
                files = get_files(project_path)
                print(f'Список файлов в директории <console file manager>: {", ".join(files)}')

            elif choice == 7:
                system_info = get_system_info()
                for key, value in system_info.items():
                    print(f"{key}: {value}")

            elif choice == 8:
                prog_creator = 'Tatiana Rostkova'
                print(f'Автор программы - {prog_creator}')

            elif choice == 9:
                subprocess.run(["python", "victory.py"], check=True)

            elif choice == 10:
                subprocess.run(["python", "my_bill.py"], check=True)

            elif choice == 11:
                new_dir = input('Введите путь к новой рабочей директории: ')
                try:
                    os.chdir(new_dir)
                    print(f'Рабочая директория изменена на: {os.getcwd()}')
                except FileNotFoundError:
                    print('Указанная директория не найдена.')

            elif choice == 12:
                print('Выход из программы.')
                break

            else:
                print('Неправильный пункт меню: введите число от 1 до 12.')

        except Exception as e:
            print(f'Произошла ошибка: {e}')

if __name__ == "__main__":
    main()