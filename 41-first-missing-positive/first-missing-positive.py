class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        num=1
        for j in nums:
            if j==num:
                num+=1
        return num
