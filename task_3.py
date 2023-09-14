name = ['Arman', 'Nurlan', "Medina"]
my_int = [300000, 400000, 500000]
proc = ['10.25%', '9.25%', '8%']
print(f'Входные данные:\n{name}\n{my_int}\n{proc}')
print()
print({name: my_int * float(proc[:-1]) / 100 for name, my_int, proc in zip(name, my_int, proc)})
