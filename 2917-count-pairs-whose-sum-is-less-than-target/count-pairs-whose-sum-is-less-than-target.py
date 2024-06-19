class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count=0
        for i in range(len(nums)-1):
            for j in range(len(nums)):
                if i<j and nums[i]+nums[j]<target:
                    count+=1
        return count
