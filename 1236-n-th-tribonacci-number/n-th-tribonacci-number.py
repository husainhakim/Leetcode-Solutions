class Solution(object):
    def tribonacci(self, n):
        if n < 3:
            return 0 if n == 0 else 1

        a, b, c = 0, 1, 1

        for i in range(2, n):
            a, b, c = b, c, a + b + c

        return c

        