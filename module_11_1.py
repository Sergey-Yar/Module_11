'''Цель: познакомиться с использованием сторонних библиотек в Python
 и применить их в различных задачах.'''


from PIL import Image   #Работа с библиотекой pillow. Позволяет работать с изображениями.


def image_job(image_path):
    image = Image.open(image_path)          #открываем изображение
    image = image.resize((800, 600))        #меняем размер изображения
    image = image.convert('L')              #преобразуем изображение из цветного в черно-белое
    image.save('img_2.png')                 #сохраняем изображение в другой формат


image_job('img_1.jpg')




import requests    #Инструментом для работы с HTTP-запросами

resp = requests.get('https://example.com')  #отправляем простой GET-запрос на URL https://example.com
print(resp.status_code)                     #информация о статусе запроса
print(resp.encoding)                         #узнаем, какую кодировку использует requests


#работа с заголовками
headers = {                                     #добавляем 2 заголовка
    'User-Agent': 'MyApp/1.0',                  #Идентифицируем наше приложение
    'Content-Type': 'application/json'          #Указываем формат передаваемых данных
}
resp2 = requests.get('https://example.com', headers=headers)
for key, value in resp2.headers.items():
    print(f'{key}: {value}')                    #выводим заголовки, полученные от сервера





#Модуль для работы с многомерными массивами и матрицами
# также реализует широкий спектр математических функций, необходимых для обработки данных,
# линейной алгебры, статистики и многого другого.

import numpy

print('------------------------------')
array_1d = numpy.array([11, 5, 8, 65, 9])                     #Создаем одномерный массив
print("Одномерный массив:", array_1d)


array_2d = numpy.array([[21, 22, 23], [34, 35, 36], [47, 48, 49]])       #Создаем двумерный массив
print("\nДвумерный массив:\n", array_2d)


sum_array = numpy.sum(array_1d)                                  #Суммируем элементы массива
print("\nСумма элементов одномерного массива:", sum_array)

#Решение системы линейных уравнений
x = numpy.array([[4, 8], [9, 15]])
y = numpy.array([2, 3])

# Подмодуль solve решает систему линейных уравнений, linalg - выполняет операции линейной алгебры
result = numpy.linalg.solve(x, y)
print("\nРешение системы линейных уравнений:", result)