from builtins import print

a = 0
b = 0


def q(c, d=a):
    """

    :type c: int
    :type d: int
    """

    def f(x):
        global b
        return x + c + d + b
    return f


def call_110() -> None:
    """

    :rtype: None
    """
    global a, b

    h = q(10)
    v = h(100)
    print("a={}; b={}; q({})({}) => {}".format(a, 10, 100, v))


def main():
    global a, b
    call_110()
    a = 1
    b = 1000
    call_110()


if __name__ == '__main__':
    main()
