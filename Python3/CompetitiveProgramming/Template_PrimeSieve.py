def get_primes(n):
    is_prime = [1] * (n + 1)    # [0.....N]
    is_prime[0], is_prime[1] = 0, 0    # make 0 and 1 NOT PRIME
    for i in range(4, n + 1, 2):    # make even nos. NOT PRIME
        is_prime[i] = 0
    for i in range(3, int(n ** 0.5 + 2), 2):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = 0
    return is_prime
