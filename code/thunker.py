# @see: http://jtauber.com/blog/2008/03/30/thunks,_trampolines_and_continuation_passing/

thunk = lambda name, *args: lambda: name(*args)


def _trampoline(bouncer):
    while callable(bouncer):
        bouncer = bouncer()
    return bouncer


trampoline = lambda f: lambda *args: _trampoline(f(*args))


identity = lambda x: x


_factorial = lambda n, c=identity: c(1) if n == 0 else thunk(_factorial, n - 1, lambda result: thunk(c, n * result))


factorial = trampoline(_factorial)

print(factorial(100000))


# alternative
thunk_b = lambda name: lambda *args: lambda: name(*args)

_factorial_b = lambda n, c=identity: c(1) if n == 0 else thunk_b(_factorial_b)(n - 1, lambda result: thunk_b(c)(n * result))

