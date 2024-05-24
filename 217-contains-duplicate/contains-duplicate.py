class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for x in nums:
            if x in s:
                return True
            else:
                s.add(x)
        return False