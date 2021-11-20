class Solution:
    def __init__(self):
        self.dp = []
        self.dp.append(1)
        self.dp.append(1)
        for i in range(2, 45+1):
            self.dp.append(self.dp[i-1] + self.dp[i-2])
        
        
    def climbStairs(self, n: int) -> int:
        return self.dp[n]
