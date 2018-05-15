class Fib():
    def __init__(self):
        self.prev = 1
        self.cur = 1

    def __iter__(self):
        return self

    def __next__(self):
        v = self.prev
        self.prev = self.cur
        self.cur = self.prev + self.cur
        return v


if __name__ == '__main__':
    f = Fib()
    for i in range(10):
        fi = iter(f)
        print(next(fi))

    from itertools import islice
    f2 = Fib()
    for i in islice(iter(f2),0,10):
        print(i)