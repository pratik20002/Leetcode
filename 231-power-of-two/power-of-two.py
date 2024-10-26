class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #With Loops T / S = O(1)
        # x = 1
        # while x < n:
        #     x *= 2
        # return x == n

        #Without loops and recursion

        return n > 0 and (n & (n - 1)) == 0