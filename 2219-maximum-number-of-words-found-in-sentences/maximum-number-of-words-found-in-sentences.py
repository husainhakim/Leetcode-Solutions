class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(i.count(" ") for i in sentences) +1