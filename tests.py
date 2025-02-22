
import os
import tempfile

# Создаем временную директорию для тестов
with tempfile.TemporaryDirectory() as temp_dir:
    # Переходим во временную директорию
    original_dir = os.getcwd()
    os.chdir(temp_dir)

    # Создаем тестовую среду: несколько файлов и папок
    test_files = ['test_file1.txt', 'test_file2.py']
    test_dirs = ['test_dir1', 'test_dir2']

    # Создаем файлы и папки
    for file in test_files:
        with open(file, 'w') as f:
            f.write('')  # Создаем пустой файл
    for dir in test_dirs:
        os.mkdir(dir)

    # Запускаем тестируемый код
    with open('listdir.txt', 'w') as f:
        items = os.listdir()
        # Исключаем файл listdir.txt из списка файлов
        files = [item for item in items if os.path.isfile(item) and item != 'listdir.txt']
        dirs = [item for item in items if os.path.isdir(item)]
        f.write('files: ' + ', '.join(files) + '\n')
        f.write('dirs: ' + ', '.join(dirs) + '\n')

    # Проверяем, что файл listdir.txt существует
    if os.path.exists('listdir.txt'):
        print("Файл listdir.txt успешно создан.")
    else:
        print("Ошибка: файл listdir.txt не создан.")

    # Читаем содержимое файла и проверяем его
    with open('listdir.txt', 'r') as f:
        content = f.read()
        print("Содержимое файла listdir.txt:")
        print(content)

    # Проверяем, что файлы и папки записаны правильно
    expected_files = 'files: ' + ', '.join(test_files)
    expected_dirs = 'dirs: ' + ', '.join(test_dirs)

    if expected_files in content and expected_dirs in content:
        print("Тест пройден: файл listdir.txt содержит правильные данные.")
    else:
        print("Тест не пройден: файл listdir.txt содержит некорректные данные.")

    # Возвращаемся в исходную директорию
    os.chdir(original_dir)

print("Тестовая среда очищена автоматически.")