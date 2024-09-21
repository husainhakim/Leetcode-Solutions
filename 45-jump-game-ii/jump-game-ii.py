class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
             return 0
        jumps = 0        
        farthest = 0      
        currentend = 0    
     
        for i in range(n - 1):
      
            farthest = max(farthest, i + nums[i])
        

            if i == currentend:
                jumps += 1
                currentend = farthest
            
          
            if currentend >= n - 1:
                return jumps
    
