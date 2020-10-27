import functools


def benchmark(func):
    import time

    def wrapper(a):
        start = time.time()
        res = func(a)
        end = time.time()
        print('[*] Completion time: {} seconds.'.format(end - start))
        return res

    return wrapper


@benchmark
def get_fact(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i
    return fact


number_1 = 5
print(f'Factorial of {number_1} is {get_fact(number_1)}')


@benchmark
def factorial(n):
    if n == 0:
        return 1
    else:
        return functools.reduce(lambda x, y: x*y, range(1, n+1))


number_2 = 5
print(f'Factorial of {number_2} is {factorial(number_2)}')

