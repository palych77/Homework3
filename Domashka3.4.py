# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
def binarnie(msg):
    number = int(input('Введите число: '))
    binar = ''
    while number > 0:
        binar = str(number % 2) + binar
        number = number // 2
    print(binar)
    return msg

msg = ('Некорректный ввод!')

try:
    msg = binarnie(msg)
except:
    print(msg)