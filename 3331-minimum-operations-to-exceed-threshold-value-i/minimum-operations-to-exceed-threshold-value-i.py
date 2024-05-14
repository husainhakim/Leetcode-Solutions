class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        number=0
        for i in range(len(nums)):
            if nums[i]<k:
                number=number+1
        return number



        