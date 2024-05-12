class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        totalsum=0
        for i in range (len(nums)):
            totalsum+=nums[i]
            nums[i]=totalsum
        return nums

        