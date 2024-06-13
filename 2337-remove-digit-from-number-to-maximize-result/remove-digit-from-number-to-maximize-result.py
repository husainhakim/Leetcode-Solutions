class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = 0
        for i, dig in enumerate(list(number)):
            if dig == digit:
                ans = max(ans, int(number[:i]+number[i+1:]))
        
        return str(ans)