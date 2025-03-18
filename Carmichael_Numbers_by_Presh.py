# Chukwuezi, Tochukwu Precious

# Carmichael Number Search

# March 18, 2025

# Dependencies

# The Sieve of Erastosthenes
def primes_less_than_eq(n: int) -> list[int]:
    """
    Author: Chukwuezi, T. Precious
    
    This function is an alias for the Sieve of Erastosthenes It uses the
    Sieve of Erastosthenes powered by effiecient prime factorization search for an 
    arbitraty inter > 1 up to its square root.It derives its power and speed from the
    cancelation of multiples of all prime factors below the square root of the number given.

    Args:
        n (int): The number, or range of for prime number search.

    Returns: 
        list[int]: The list of prime numbers <= n.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for p in range(2, int(n**0.5)+1): # While p*p <= n
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
    
    return [p for p in range(2, n+1) if primes[p]]

# Prime Factorization
def prime_factors(n):
    """
    Author: Chukwuezi, T. Precious"

    This function finds all prime factors and their powers of a given number n.

    Args:
        n (int): The number to find prime factors.
    
    Returns:
        tuple: A tuple of prime factors and their powers in ascending order.
    """
    i = 2
    factors = []
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i += 1
    primes = tuple(sorted(set(factors)))
    powers = [(x, factors.count(x)) for x in primes]

    return primes, powers


# Basic Function Tests
# Here, I check the functions to see if they are work properly.

print(prime_factors(20))
l1 = primes_less_than_eq(100)
print(l1, "\n\nThere are",len(l1),"primes in this range\n")


l2 = primes_less_than_eq(10001)
print("\n", l2)
print("\nThere are",len(l1),"primes in this range\n")


# Carmichael Numbers Demonstration using the Dependencies
# Here, I implemented the main functionality to test the if numbers in a given range are Carmichael numbers.
def Carmichael_Search(a, b):
    """
    Author: Chukwuezi, T. Precious
    
    This function finds all Carmichael numbers between two range or integers a, b.
    It uses the prime factorization and Euler's totient function to find Carmichael numbers.
    Other than  using Fermmat's theorem, this function uses mostly Korselt's Criterion, that 
    for all prime factors p of N, (p-1) divides (N-1). They find applications in testing secure
    Cryptographic systems.

    Returns:
        list: Of Carmichael numbers between a and b (inclusive, if they pass the test).
    """
    P = primes_less_than_eq(b)
    carmichael_numbers = []

    iter_not_prime = [x for x in range(a, b+1) if (x not in P)] # Since Carmichael are not primes, filter out primes.
    
    for n in iter_not_prime:
        f, power_prime = prime_factors(n)

        if not all(e[1] == 1 for e in power_prime): # there are no square factorizations and so forth for Carmichael Numbers
            continue
        if all([(n - 1) % (p-1) == 0 for p in f]): # Korselt's Criterion:
            carmichael_numbers.append(n)
    return carmichael_numbers



l3 = Carmichael_Search(560, 10000)
print(l3, "\n\nThere are", len(l3),"Carmichael numbers in this range\n")

l3 = Carmichael_Search(10001, 100000)
print(l3, "\n\nThere are", len(l3),"Carmichael numbers in this range\n")