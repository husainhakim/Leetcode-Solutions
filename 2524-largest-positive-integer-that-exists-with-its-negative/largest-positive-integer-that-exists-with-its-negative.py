class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        max_k = -1  

        for num in nums:
            if num > 0 and -num in nums:
                max_k = max(max_k, num)
        
        return max_k  
