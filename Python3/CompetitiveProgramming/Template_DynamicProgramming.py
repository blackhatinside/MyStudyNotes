# MAXIMUM SUBARRAY SUM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalmax = localmax = nums[0]
        for i in range(1, len(nums)):
            localmax = max(nums[i], localmax + nums[i])
            globalmax = max(globalmax, localmax)
        return globalmax
