class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxx, minn = -1, nums[0]
        for i in range(len(nums)):
            maxx = max(maxx, nums[i] - minn)
            minn = min(minn, nums[i])
        return maxx if maxx != 0 else -1

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalmax = localmax = nums[0]
        for i in range(1, len(nums)):
            localmax = max(nums[i], localmax + nums[i])
            globalmax = max(globalmax, localmax)
        return globalmax
