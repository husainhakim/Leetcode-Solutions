class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0
        
        isprime = [True] * n
        isprime[0] = isprime[1] = False
        
        count_prime = 0
        for num in range(2, int(n**0.5) + 1):
            if isprime[num]:
                for multiple in range(num*num, n, num):
                    isprime[multiple] = False
        
        return sum(isprime)
