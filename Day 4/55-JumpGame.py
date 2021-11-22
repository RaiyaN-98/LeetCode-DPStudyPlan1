class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canGo = 0
        n = len(nums)
        ans = True
        for i in range(n):
            canGo = max(canGo, i+1+nums[i])
            if canGo == i+1 and i+1 != n:
                ans = False
                break
        return ans
                
