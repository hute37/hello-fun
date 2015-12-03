from concurrent.futures import ProcessPoolExecutor
import multiprocessing as mp


def prime_sieve(limit):
    numbers = dict()
    limit = int(limit)
    for n in range(2, limit + 1):
        numbers[n] = ()
    primes = numbers.copy()
    for n in numbers:
        m = n
        while m <= limit:
            m = m + n
            primes.pop(m, 0)
    return primes


def factorize_naive(n):
    """Return a list of the prime factors for a natural number."""
    if n < 2:
        return []
    prime_factors = []
    for p in prime_sieve(int(n**0.5) + 1):
        if p*p > n: break
        while n % p == 0:
            prime_factors.append(p)
            n //= p
    if n > 1:
        prime_factors.append(n)
    return prime_factors


def factorize_naive_b(n):
    """ A naive factorization method. Take integer 'n', return list of
        factors.
    """
    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return factors

        r = n % p
        if r == 0:
            factors.append(p)
            n = n // p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            # Advance in steps of 2 over odd numbers
            p += 2
        else:
            # If p == 2, get to 3
            p += 1
    assert False, "unreachable"


def mp_factorizer_map(nums, nprocs):
    with mp.Pool(nprocs) as pool:
        return {num:factors for num, factors in
                                zip(nums,
                                    pool.map(factorize_naive, nums))}


def pool_factorizer_map(nums, nprocs):
    # Let the executor divide the work among processes by using 'map'.
    with ProcessPoolExecutor(max_workers=nprocs) as executor:
        return {num:factors for num, factors in
                                zip(nums,
                                    executor.map(factorize_naive, nums))}


NPROC = 8


def main():
    global NPROC
    nums = [(x * 3 + 1) * 11 * 13 for x in range(0, 75000, 7000)]

    print("mp:\t\t", mp_factorizer_map(nums,NPROC))
    print("pool:\t", pool_factorizer_map(nums,NPROC))


if __name__ == '__main__':
    main()
