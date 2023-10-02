"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
# Checks if the number given is a prime number
def check_prime(num):
    flag = True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            flag = False
    
    return flag


def primes(number_of_primes):
    list = []
    # Solution starts here
    if number_of_primes < 1:
        pass
    else:
        counter = 0
        num = 2
        while counter < number_of_primes:
            if check_prime(num):
                list.append(num)
                counter += 1
            num+=1


    return list
