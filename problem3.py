# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math

def getPrimeNumbers(lower, upper):
    prime = []
    for num in range(lower,upper+1):
        if num>1:
            for i in range(2, num):
                if num%i==0:
                    break
                else:
                    prime.append(num)
                    break

    return prime

def primeFactors():
    prime_numbers = getPrimeNumbers(1,100)
    prime_factors = []
    n = 600851475143
    while 13195%2==0:
        prime_factors.append(2)
        n = n/2

    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            prime_factors.append(i)
            n = n/i
    
    return prime_factors

if __name__ == '__main__':
    print(primeFactors())