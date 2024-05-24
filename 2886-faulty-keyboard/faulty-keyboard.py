class Solution:
    def finalString(self, s: str) -> str:
        fin = ''
        for char in s:
            if char != 'i':
                fin += char
            else:
                fin = fin[::-1]
        return fin