class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    temp=nums[j]
                    nums[j]=nums[i]
                    nums[i]=temp
        return nums
                