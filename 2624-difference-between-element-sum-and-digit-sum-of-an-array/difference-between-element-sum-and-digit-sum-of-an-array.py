class Solution:
    def differenceOfSum(self, nums) :
        sumlist=0
        for i in nums:
            sumlist+=i
        totalsum = 0
        for num in nums:
            numstr = str(num)
            for digit in numstr:
                totalsum += int(digit)
        return sumlist-totalsum

        