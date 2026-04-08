class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        dyanmic programming: sum the 1s
        if power of 2: just one
        else other: 1 + dp[n-mostsigbit]
        """
        msb = 1
        ans = []

        for i in range(n + 1):
            if i == 0:
                ans.append(0)
                continue
            if i == msb * 2:
                msb = msb * 2
                ans.append(1)
                continue
            else:
                ans.append(1+ans[i - msb])

        return ans