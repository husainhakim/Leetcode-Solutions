class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        flag = 0
        for word in words:
            flag = 0
            for i in word:
                if i not in allowed:
                    flag = 1
                    break
            if flag:
                continue
            
            count += 1
        return count
