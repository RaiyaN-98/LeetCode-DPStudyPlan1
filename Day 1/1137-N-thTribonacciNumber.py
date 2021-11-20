class Solution:
    def __init__(self):
        self.dp = []
        for i in range(40):
            if i == 0:
                self.dp.append(0)
            elif i == 1 or i == 2:
                self.dp.append(1)
            else:
                self.dp.append(self.dp[i-1] + self.dp[i-2] + self.dp[i-3])
    
    def tribonacci(self, n: int) -> int:
        return self.dp[n]
        
