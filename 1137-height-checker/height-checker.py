class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected=sorted(heights)
        mismatch=0
        for i in range (len(heights)):
            if expected[i]!=heights[i]:
                mismatch+=1
        return mismatch