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
    
class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        max_value=arr[0]
        min_value=arr[0]
        ans=arr[0]
        for i in range(1,len(arr)):                 #using DP approach
            choice1=arr[i]*max_value                # + for subarraysum, * for subarrayproduct
            choice2=arr[i]*min_value                # + for subarraysum, * for subarrayproduct
            # if -ve ele then min +/* ele, else max +/* ele, also compare ele alone by itself
            max_value=max(arr[i],choice1,choice2)   # local maximum
            min_value=min(arr[i],choice1,choice2)   # local minimum
            ans=max(ans,max_value)                  # global maximum
        return(ans)
