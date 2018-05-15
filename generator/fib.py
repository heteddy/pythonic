def fib():
    prev, cur = 1, 1
    while True:
        yield prev
        prev = cur
        cur = prev + cur


if __name__ == '__main__':
    from itertools import islice

    f = fib()
    f10 = islice(f, 0, 10)
    for v in f10:
        print(v)
