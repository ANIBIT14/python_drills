def is_prime(n):
    """
    Check whether a number is prime or not
    """
    if n > 1:
        for i in range(2, n):
            if( n % i == 0):
                return False
        else:
            return True


def n_digit_primes(digit):
    """
    Return a list of `n_digit` primes using the `is_prime` function.

    Set the default value of the `digit` argument to 2
    """
    l = []
    for i in range (10 ** (digit-1), 10 ** (digit)):
        if is_prime(i):
            l.append(i)
        
    return l

