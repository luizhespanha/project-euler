'''
Created on Jul 3, 2012

@author: lhespanha
'''

import operator
# A slightly efficient superset of primes.
def PrimesPlus():
    yield 2 
    yield 3
    i = 5
    while True:
        yield i
        if i % 6 == 1:
            i += 2
        i += 2

# Returns a dict d with n = product p ^ d[p]
def GetPrimeDecomp(n):
    d = {}
    primes = PrimesPlus()
    for p in primes:
        while n % p == 0:
            n /= p
            d[p] = d.setdefault(p, 0) + 1
        if n == 1:
            return d
        
def NumberOfDivisors(n):
    d = GetPrimeDecomp(n)
    powers_plus = map(lambda x: x+1, d.values())
    return reduce(operator.mul, powers_plus, 1)


acc = 0;

for p in PrimesPlus():
    if p > 10:
        break
    else:
        print p

for i in range(1):
    achou= False
    divisors = 1;
    
    acc = sum(range(1,i+2))
    if NumberOfDivisors(acc) > 500:
        print acc
        break
        
if __name__ == '__main__':
    pass