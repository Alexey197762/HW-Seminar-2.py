# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

a = input('Введите число : ')

def sum_a(a):                           
    if float(a) < 0:                           
        a = float(a) * (-1)
        print(a)
    num = 0

    for i in str(a):
        if i != '.':
            num += int(i)
    return int(num)

   
print(f'Сумма {a} равна = ', sum_a(a))

