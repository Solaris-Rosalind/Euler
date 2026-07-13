'''
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
'''

def summation_of_primes(limit):
    # Create a boolean array initialized to True
    sieve = [True] * limit
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    
    # Iterate up to the square root of the limit
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            # Mark multiples of i as composite (False)
            for j in range(i * i, limit, i):
                sieve[j] = False
                
    # Sum the indices that remain True
    return sum(i for i, is_prime in enumerate(sieve) if is_prime)

# Find the sum of all primes below two million
limit = 2000000
print(f"The sum of primes below {limit} is: {summation_of_primes(limit)}")