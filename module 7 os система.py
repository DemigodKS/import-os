import os
import os.path
import time
from fileinput import filename

for root, dirs, files in os.walk('.'):

    for file in files:

        path2 = "fake_math.py"
        path3 = "file.txt"

        filepath = os.path.join(file)

        filetime = os.path.getmtime(file)

        formatted_time = time.ctime(filetime)

        filesize = os.path.getsize(file)

        parent_dir = os.path.dirname(file)


        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, '
            f'Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

    break