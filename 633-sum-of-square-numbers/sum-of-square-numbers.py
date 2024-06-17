class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        currentsum=0
        left,right=0,int(c**0.5)
        while left<=right:
            currentsum=left**2+right**2
            if currentsum==c:
                return True
            elif currentsum>c:
                right=right-1
            else:left=left+1
        return False

