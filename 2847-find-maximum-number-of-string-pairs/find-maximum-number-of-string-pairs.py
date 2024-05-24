class Solution:
    def maximumNumberOfStringPairs(self, w: List[str]) -> int:
        return sum(v[::-1] in w[i+1:] for i,v in enumerate(w))