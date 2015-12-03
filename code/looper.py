from timeit import timeit


class Countdown(object):

    def __init__(self, start):
        self.count = start

    def __iter__(self):
        return self

    def __next__(self):
        i = self.count
        if i <= 0:
            raise StopIteration
        self.count -= 1
        return i


def countdown(start):
    while start > 0:
        yield start
        start -= 1


def cycle_iter(n, trace=False):

    for i in Countdown(n):
        for j in Countdown(n):
            for k in Countdown(n):
                if trace:
                    print ("iter:", i, j, k)


def cycle_gener(n, trace=False):
    for i in countdown(n):
        for j in countdown(n):
            for k in countdown(n):
                if trace:
                    print ("gener:", i, j, k)


def check(n, trace=False, runs=3):
    print('#\t', n, "\t iter =>\t", timeit("cycle_iter(n={n},trace={trace})".format(n=n, trace=trace), setup="from __main__ import cycle_iter", number=runs))
    print('#\t', n, "\tgener =>\t", timeit("cycle_gener(n={n},trace={trace})".format(n=n, trace=trace), setup="from __main__ import cycle_gener", number=runs))


def main():
    check(5, trace=True)
    check(10)
    check(100)
    check(200)
    check(300)


if __name__ == '__main__':
    main()
