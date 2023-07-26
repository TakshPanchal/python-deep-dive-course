import time


def my_timer(func, *args, rep=1, log=False, **kwargs):
    start = time.perf_counter()

    for i in range(rep):
        func(*args, **kwargs)

        if log:
            print(f"----{i}----")

    end = time.perf_counter()
    return (end - start) / rep


def calc_pows_1(n, *, start=1, end):
    # Using for loops
    result = []
    for i in range(start, end):
        result.append(n**i)

    return result


def calc_pows_2(n, *, start=1, end):
    # Using for list comprehension
    return [n**i for i in range(start, end)]


def calc_pows_3(n, *, start=1, end):
    # Using generators expression
    return (n**i for i in range(start, end))


print(my_timer(calc_pows_1, 2, end=20000, rep=5))
print(my_timer(calc_pows_2, 2, end=20000, rep=5))
print(my_timer(calc_pows_3, 2, end=20000, rep=5))