# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 => 2 2
# 5 6 => 3 2

sum = int(input("Введите сумму чисел:"))
multy = int(input("Введите произведение чисел:"))
n = 1000
flag = True
for i in range (n):
    for j in range (n):
        if (i+j == sum) and (i*j == multy):
            print ("X = ", i, "Y = ", j)
            flag =False
            break
if flag:
    print ("Таких чисел нет")
