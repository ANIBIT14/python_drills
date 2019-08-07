import functools
import time
import math


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.10f} secs")
        return value
    return wrapper_timer

def memoize(func):
    """Keep a cache of previous function calls"""
    @functools.wraps(func)
    def wrapper_memoize(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_memoize.cache:
            wrapper_memoize.cache[cache_key] = func(*args, **kwargs)
        return wrapper_memoize.cache[cache_key]
    wrapper_memoize.cache = dict()
    return wrapper_memoize


@timer 
def sqrt(x):
    return math.sqrt(x)

@timer
def square(x):
    return (x * x)

@timer
def square_different(x):
    return (x ** 2)

@timer
def add(x, y):
    return x + y

@timer
def add3(x, y, z):
    return x + y + z

@timer
def add_any(*args):
    return sum(args)

@timer
def abs_add_any(*args, **kwargs):
    total = sum(args)
    if kwargs.get('abs') is True:
        return abs(total)
    return total

@memoize
def fib(n):
    print("Computing fib({})".format(n))
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)

@functools.lru_cache(maxsize=16)
def factorial(n):
    print("Computing factorial({})".format(n))
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


sqrt(243243)
square(243243)
square_different(243243)
add(5, 7)
add3(9, 14, 56)
add_any(6, 7, 8, 2, 5, 90)
abs_add_any(4, 5, 7, 6, a=1, b=2, c=3)
fib(10)
factorial(30)
print(factorial.cache_info())