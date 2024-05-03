class Solution:
    def subtractProductAndSum(self, n) -> int:
        multiple=1
        sumofnum=0
        for i in str(n):
            multiple*=int(i)
            sumofnum+=int(i)
        return multiple-sumofnum

