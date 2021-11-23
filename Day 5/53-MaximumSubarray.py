class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        val = 0
        con = 0
        mx = -100000000000
        for x in nums:
            con = con + x
            con = max(con, 0)
            val = max(con, val)
            mx = max(mx, x)
        if mx < 0:
            val = mx
        return val
