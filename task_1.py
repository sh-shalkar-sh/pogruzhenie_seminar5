#Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
#Для проверки числа на простоту используйте
#правило: «число является простым, если делится
#нацело только на единицу и на себя».

from typing import Generator

def primes(n: int) -> Generator:
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            yield i


for num, i in enumerate(primes(50), start=1):
    print(f'{num} = {i}')

