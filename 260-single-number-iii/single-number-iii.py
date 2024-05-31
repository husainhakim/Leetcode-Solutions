class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        List=[]
        for num in nums:
             if nums.count(num)==1:
                List.append(num)  
                
                
        return List
       