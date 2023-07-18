# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random
n = int(input("Введите кол-во моонеток:"))
count_o = 0
count_t = 0
for i in range (n):
    side = random.randint(0,1)
    print(side, end=" ")
    if side > 0:
        count_o += 1
    else:
        count_t += 1
print()
if count_t > count_o:
    print(count_o, )
else: print(count_t)