f1 = int(input('введите число  '))


def fib(n):
    f1, f2 = 0, 1
    for _ in range(n):
        yield f1
        f1, f2 = f2, f1 + f2

print(list(fib(f1)))