# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
size_lst = random.randint(5,20)

first_bord = int(input('Введите меньшую границу: '))
second_bord = int(input('Введите большую границу: '))
kit_numbers = [random.randint(first_bord-random.randint(1,5),second_bord+random.randint(1,5)) for _ in range(size_lst)]
index_kit = []

for i in range(size_lst):
    if first_bord <= kit_numbers[i] and kit_numbers[i] <= second_bord:
        index_kit.append(i)
print(kit_numbers, end=' ')
print()
print(index_kit, end=' ')