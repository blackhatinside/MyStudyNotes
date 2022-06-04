class Solution:
    def monotonicstack(self, arr, n):
        ''' Returns the index of NGE '''
        stack = []  # monotonic stack
        nge = [0] * n
        for i in range(n - 1, -1, -1):
            while stack != [] and arr[i % n] >= arr[stack[-1]]:
                stack.pop()
            if stack == []:
                nge[i % n] = -1
            else:
                nge[i % n] = stack[-1]
            stack.append(i % n)
        return nge
# greater = self.monotonicstack(arr, n)

'''---------- https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1/ ----------'''

class Solution:
    def monotonicstack(self, arr, n):
        stack = []  # monotonic stack
        nge = [0] * n
        for i in range(n - 1, -1, -1):
            while stack != [] and arr[i] >= arr[stack[-1]]:
                stack.pop()
            if stack == []:
                nge[i] = -1
            else:
                nge[i] = stack[-1]
            stack.append(i)
        return nge
    def nextLargerElement(self,arr,n):
        #code here
        ans = []
        greater = self.monotonicstack(arr, n)
        for i in range(n):
            if greater[i] != -1:
                ans.append(arr[greater[i]])
            else:
                ans.append(-1)
        return ans

'''---------- https://leetcode.com/problems/next-greater-element-ii/ ----------'''

class Solution:
    def monotonicstack(self, arr, n):
        stack = []  # monotonic stack
        nge = [0] * n
        for i in range(2 * n - 1, -1, -1):
            while stack != [] and arr[i % n] >= arr[stack[-1]]:
                stack.pop()
            if stack == []:
                nge[i % n] = -1
            else:
                nge[i % n] = stack[-1]
            stack.append(i % n)
        return nge
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        greater = self.monotonicstack(nums, len(nums))
        ans = [nums[greater[i]] if greater[i] != -1 else -1 for i in range(len(nums))]
        return ans

'''---------- https://leetcode.com/problems/sliding-window-maximum/ ----------'''
    
class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        stack = []
        ans = []
        for i in range(len(arr)):
            while stack != [] and arr[stack[-1]] < arr[i]:    # monotonic stack
                stack.pop()
            stack.append(i)
            while stack[0] <= i - k:    # if windows overflow, keep popping from beginning
                stack.pop(0)
            if i >= k - 1:  # when window is full, keep finding the max element
                ans.append(arr[stack[0]])
        return ans
