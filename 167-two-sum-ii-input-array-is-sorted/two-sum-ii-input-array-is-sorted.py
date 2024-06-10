class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head=0
        tail=len(numbers)-1
        while head<=tail:
            pairsum=numbers[head]+numbers[tail]
            if pairsum < target:
                head=head+1
            elif pairsum >target:
                tail=tail-1
            else:
                return [head+1,tail+1]
        return [-1,-1]
