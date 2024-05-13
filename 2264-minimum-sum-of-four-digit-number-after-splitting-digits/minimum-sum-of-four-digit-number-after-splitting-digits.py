class Solution:
    def minimumSum(self, num: int) -> int:

        num=str(num)
        num=list(num)
        num.sort()
        a=num[0]+num[2]
        b=num[1]+num[3]
        
        return int(a) + int(b)
        