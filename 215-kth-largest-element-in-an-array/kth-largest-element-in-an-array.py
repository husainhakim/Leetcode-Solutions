class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       hello=sorted(nums)
       return hello[-k]

        