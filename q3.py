def fNonPrimes(n):
    return [i for i in range(2, n + 1) if not all(i % j != 0 for j in range(2, i))]