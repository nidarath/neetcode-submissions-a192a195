class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else: 
            ans, add = 1, 1
            for i in range(n - 1):
                temp = ans 
                ans = ans + add
                add = temp
            return ans
                

