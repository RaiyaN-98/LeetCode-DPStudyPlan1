class Solution:
    def __init__(self):
        self.arr = []
        self.dp = []
        for i in range(10007):
            self.arr.append(0)
            self.dp.append(0)
    
    def deleteAndEarn(self, nums: List[int]) -> int:
        for x in nums:
            self.arr[x] += 1
        ans = 0
        self.dp[1] = self.arr[1]
        self.dp[2] = self.arr[2]*2
        for i in range(3, 10007):
            self.dp[i] = max(self.dp[i-2], self.dp[i-3]) 
            self.dp[i] += (i*self.arr[i])
            ans = max(ans, self.dp[i])
        return ans
