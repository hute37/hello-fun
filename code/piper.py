from builtins import print

a = 0
b = 0


def orange(start, stop, step):
    print(" <= orange({},{},{})".format(start, stop, step))
    return range(start, stop, step)


def q(c, d=a):
    """

    :type c: int
    :type d: int
    """

    def f(n):
        global b
        for i in orange(0, n, b+1):
            print("i={}, n={}, b={}, c={}, d={}".format(i, n, b, c, d))
            l = i + c + d
            yield l
    return f


def call_110() -> None:
    """

    :rtype: None
    """
    global a, b

    h = q(100)
    g = h(10)
    v = list(g)

    print("a={}; b={}; q({})({}) => {}".format(a, b, 100, 10, v))


def main():
    global a, b
    call_110()
    a = 1
    b = 2
    call_110()


if __name__ == '__main__':
    main()
