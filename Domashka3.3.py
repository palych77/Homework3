# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
sp = [1.1, 1.2, 3.1, 5, 10.01]
for i in range(len(sp)):
    sp[i] = sp[i] % 1
if 0 in sp:
    sp.remove(0)
print(sp)
smallest = min(sp)
highest = max(sp)
print(round(highest-smallest,2))
