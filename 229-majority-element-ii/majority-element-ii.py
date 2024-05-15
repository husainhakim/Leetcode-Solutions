class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={x:nums.count(x) for x in set(nums) if nums.count(x)>len(nums)//3}
        return list(d.keys())