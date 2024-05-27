class Solution:
    def specialArray(self, nums: List[int]) -> int:
        mem = [0 for i in range(len(nums)+1)]
        for num in nums:
            if num >= len(nums):
                mem[-1] += 1
            else:
                mem[num] += 1
        cur = 0 
        for i in range(len(mem)-1, -1, -1):
            cur += mem[i] 
            if cur == i:
                return i 
        return -1