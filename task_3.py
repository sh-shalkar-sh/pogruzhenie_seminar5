# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

name = ['Arman', 'Nurlan', "Medina"]
my_int = [300000, 400000, 500000]
proc = ['10.25%', '9.25%', '8%']
print(f'Входные данные:\n{name}\n{my_int}\n{proc}')
print()
print({name: my_int * float(proc[:-1]) / 100 for name, my_int, proc in zip(name, my_int, proc)})
