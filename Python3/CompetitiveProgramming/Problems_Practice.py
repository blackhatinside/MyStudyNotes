# Important Problems for Practice for Interviews

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
