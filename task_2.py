import os

my_path = "C:/test/seminar_5_task_2.py"

def fun(two_path: str) -> tuple:
    path, file_name = os.path.split(two_path)
    name, extension = file_name.split('.')
    return path, name, extension

print(f'Путь: {my_path} \nКортеж: {fun(my_path)}')
