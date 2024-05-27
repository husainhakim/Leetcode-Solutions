class Solution:
  def equalFrequency(self, word: str) -> bool:
    freq = Counter(word).values()
    mi, ma, le, wle = min(freq), max(freq), len(freq), len(word)
    return (
      le == 1 or 
      ma == 1 or  
      mi == ma - 1 and wle == mi * le + 1 or  
      mi == 1 and wle == ma * (le - 1) + 1 
    )