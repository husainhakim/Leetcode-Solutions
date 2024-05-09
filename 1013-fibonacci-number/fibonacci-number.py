class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
            
        first,second=0,1
        sumn=1
        for i in range(1,n):
            sumn+=first
            nextn=first+second
            first=second
            second=nextn
        return sumn


       


