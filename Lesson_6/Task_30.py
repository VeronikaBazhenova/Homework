# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_el = int(input('Введите первый элемент прогрессии: '))
shift_def = int(input('Введите разность прогрессии (шаг):'))
size = int(input('Введите размер массива: '))
math_progress = [first_el]
for i in range(2, size+1):
    math_progress.append(math_progress[0] + (i-1)*shift_def)
print(math_progress, end=' ')

