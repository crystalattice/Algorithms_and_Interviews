def sieve(n):
    prime = [True for i in range(n + 1)]  # Create list of True values
    p = 2
    primes = []
    while (p * p <= n):  # Start at p^2 for next in series
        if prime[p]:  # If value at [p] is True, it's prime
            for i in range(p * p, n + 1, p):  # Update all multiples of p
                prime[i] = False  # Change multiples to False
        p += 1

    for p in range(2, n):  # Get primes
        if prime[p]:
            primes.append(p)

    return primes

if __name__ == '__main__':
    n = 30
    print(sieve(n))
