class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        listed=[]
        for i in range (len(words)):
           if x in words[i]:
              listed.append(i)
        return listed
                
