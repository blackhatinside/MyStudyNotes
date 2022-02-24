# Important Problems for Practice for Interviews

# Stack: https://atcoder.jp/contests/agc005/tasks/agc005_a
w = input(); stack = [];
for x in w:
	if not stack or not (stack[-1] == "S" and x == "T"):
		stack.append(x)
	else:
		stack.pop()
print(len(stack))

# Stack: https://atcoder.jp/contests/abc064/tasks/abc064_d
n = int(input()); w = input(); stack = []; ans = w;
for x in w:
	if not stack or not (stack[-1] == "(" and x == ")"):
		stack.append(x)
	else:
		stack.pop()
for x in stack:
	if x == ")":
		ans = "(" + ans
	else:
		ans = ans + ")"
print(ans)

# Stack: https://atcoder.jp/contests/arc108/tasks/arc108_b
n = int(input()); w = input(); stack = [];
for x in w:
	stack.append(x)
	if len(stack) >= 2:
		while len(stack) >= 3 and (stack[-1] == "x" and stack[-2] == "o" and stack[-3] == "f"):
			stack.pop(); stack.pop(); stack.pop();
ans = "".join(stack)
print(len(ans) if len(w) != len(ans) else len(w))

# Stack: https://www.hackerrank.com/challenges/simple-text-editor/problem
stack = [[],]
n = int(input())
while n:
    q = input().split()
    if q[0] == "1":
        stack.append(stack[-1] + list(q[1]))
    elif q[0] == "2":
        stack.append(stack[-1][:-int(q[1])])
    elif q[0] == "3":
        print(stack[-1][int(q[1]) - 1])
    elif q[0] == "4":
        stack.pop()
    n -= 1

# Stack: https://leetcode.com/problems/next-greater-element-ii/
class Solution:
    def nextGreaterElements(self, arr: List[int]) -> List[int]:
        n, beg = len(arr), 0
        arr = arr[::-1]
        stack = []; ans = [];
        for i in range(2 * n):
            while stack and arr[i % n] >= stack[-1]:
                stack.pop()
            if not stack:
                ans.insert(beg, -1)
            else:
                ans.insert(beg, stack[-1])
            stack.append(arr[i % n])
        return ans[:n]

# Stack: https://www.hackerrank.com/challenges/largest-rectangle/problem
n = int(input())
arr = list(map(int, input().split()))
def largestRectangleAreaUnderHistogram(heights):
    maxarea = 0
    pstack, hstack = [], []
    currarea, maxarea = 0, 0
    heights.append(0)
    for i in range(len(heights)):
        prevwidth = int(1e9)
        while hstack != [] and hstack[-1] > heights[i]:
            prevwidth = pstack[-1]
            width = i - pstack.pop()
            height = hstack.pop()
            currarea = width * height
            maxarea = max(currarea, maxarea)
        if hstack == [] or hstack[-1] < heights[i]:
            hstack.append(heights[i])
            pstack.append(min(prevwidth, i))
        # while hstack: # not needed if we are appending value 0 to the heights
        #     currarea = (len(heights) - pstack.pop()) * hstack.pop()
        #     maxarea = max(currarea, maxarea)
    return maxarea
ans = largestRectangleAreaUnderHistogram(arr)
print(ans)

# Stack: https://codeforces.com/gym/102760/problem/F
n = int(input())
arr = list(map(int, input().split()))
def largestSquareUnderHistogram(heights): # O(n) solution using Stacks
    pstack, hstack = [], []
    maxside, currarea, maxside = 0, 0, 0
    heights.append(0)   # to finish off the remaining items in the stack
    for i in range(len(heights)):
        prevwidth = int(1e9)
        while hstack != [] and hstack[-1] > heights[i]: # negative slope
            prevwidth = pstack[-1]
            maxside = max(maxside, min(hstack.pop(), i - pstack.pop()))
        if not hstack or hstack[-1] < heights[i]: # positive slope
            hstack.append(heights[i])
            pstack.append(min(prevwidth, i))
    return maxside
ans = largestSquareUnderHistogram(arr)
print(ans)
