
Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число). Протестируем функцию на файле article.txt со следующим содержимым

def read_last(lines, file):
    try:
        lines = int(lines)
        if lines <= 0:
            print("Количество строк должно быть положительным числом.")
            return
    except ValueError:
        print("Количество строк должно быть задано положительным целым числом.")
        return
    try:
        with open(file, 'r') as f:
            all_lines = f.readlines()
            last_lines = all_lines[-lines:]

            for line in last_lines:
                print(line.strip())
    except FileNotFoundError:
        print("Файл не найден.")

'''


'''
Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
'''


'''
import os

def print_docs(directory):
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for file in files:
            print('{}{}'.format(subindent, file))
'''

'''
окумент article.txt содержит следующий текст:

>Вечерело  
 Жужжали мухи  
 Светил фонарик  
 Кипела вода в чайнике  
 Венера зажглась на небе  
 Деревья шумели  
 Тучи разошлись  
 Листва зеленела

Требуется реализовать функцию `longest_words(file)`, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).  
'''

'''
def longest_words(file):
    try:
        with open(file, 'r') as f:
            content = f.read()
            words = content.split()
            max_length = len(max(words, key=len))
            longest = [word for word in words if len(word) == max_length]
            if len(longest) > 1:
                print("Самые длинные слова в файле '{}' (длина {}):".format(file, max_length))
                for word in longest:
                    print(word)
            else:
                print("Самое длинное слово в файле '{}' (длина {}):".format(file, max_length))
                print(longest[0])
    except FileNotFoundError:
        print("Файл не найден.")
'''

'''
Составьте программу - простейший редактор текстовых файлов. 
Алгоритм работы программы: 
  1. Программа предлагает ввести имя будущего файла. Записывает его, присваивая расширение .txt. 
  2. Программа предлагает записать строку в файл. При каждом нажатии кнопки ENTER происходит запись строки и переход на новую строчку. 
  3. Если строка пустая или спец. символ - программа сохраняет файл.
'''

'''
def text_editor():
    file_name = input("Введите имя файла (без расширения): ")
    file_name += ".txt"
    try:
        with open(file_name, 'w') as file:
            while True:
                line = input("Введите строку (или оставьте пустую строку для сохранения): ")
                if line == "":
                    print("Файл успешно сохранен.")
                    break
                file.write(line + "\n")
    except FileNotFoundError:
        print("Ошибка при открытии файла.")
text_editor()
'''

'''
Требуется создать csv-файл rows_300.csv со следующими столбцами:
– № - номер по порядку (от 1 до 300);
– Секунда – текущая секунда на вашем ПК;
– Микросекунда – текущая миллисекунда на часах.
На каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.
'''


'''
import csv
import time

def create_csv():
    with open('rows_300.csv', 'w', newline='') as csvfile:
        fieldnames = ['№', 'Секунда', 'Микросекунда']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(1, 301):
            current_time = time.time()
            seconds = int(current_time)
            microseconds = int((current_time - seconds) * 1000000)
            writer.writerow({'№': i, 'Секунда': seconds, 'Микросекунда': microseconds})
            time.sleep(0.01)
create_csv()

'''


'''
При помощи библиотеки Pillow в директории circles (создайте ее во время выполнения функции) нарисуйте и сохраните 100 кругов радиусом 300 пикселей случайных цветов в формате jpg на белом фоне (каждый круг - отдельный файл). Для этого напишите функцию circles_generator(num_of_circles=100).
'''


'''
from PIL import Image, ImageDraw
import random
import os

def circles_generator(num_of_circles=100):
    if not os.path.exists("circles"):
        os.makedirs("circles")
    width, height = 600, 600
    for i in range(num_of_circles):
        image = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(image)
        center_x = random.randint(0, width)
        center_y = random.randint(0, height) 
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.ellipse((center_x - 300, center_y - 300, center_x + 300, center_y + 300), fill=color)
        image.save(f"circles/circle_{i+1}.jpg")
circles_generator(100)
'''
