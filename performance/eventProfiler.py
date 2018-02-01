# import cProfile
# import pstats

class Memorized():
    def __init__(self, fn):
        self.fn = fn
        self.result = dict()

    def __call__(self, *args, **kwargs):
        key = ''.join(map(str,args))
        print("key:",key)

        try:
            return self.result[key]
        except KeyError:
            print("not find key",key)
            self.result[key] = self.fn(*args)
            return self.result[key]

# @Memorized
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibSeq(n):
    seq = list()
    if n > 0:
        seq.extend(fibSeq(n - 1))
    seq.append(fib(n))
    return seq
    





print(fibSeq(30))
