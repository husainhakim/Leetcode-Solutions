class Solution:
    def minimumPushes(self, word: str) -> int:
        m = len(word)
        ans = 0
        for i in range((m // 8) + 1):
            ans += 8 * i
        ans += (m // 8 + 1) * (m % 8)
        return ans