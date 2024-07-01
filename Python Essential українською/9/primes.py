# primes.py

def is_prime(n): # Перевіряє, чи є число n простим.

    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(limit): # Повертає список простих чисел до певного значення limit.

    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes
