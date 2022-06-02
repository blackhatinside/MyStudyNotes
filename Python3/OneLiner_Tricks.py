# val = 5
# flag = True
# letters = ['p', 'r', 'o', 'j', 'e', 'c', 't', 's',]
# arr = [1, 3, 5, 7, 8, 6, 4, 2,]
# grid = [['apple', 30], ['guava', 25], ['grapes', 25], ['banana', 20], ['orange', 40],]

# to get an array from STDIN
arr = list(map(int, input().split()))

# to print the array without [,]
print(*arr) # 1 3 5 ..... 6 4 2

# to find the average of the array
print(sum(arr) / len(arr))  # 4.5

# to add seperator between different elements in the output array
print(*arr, sep = "--->") # 1--->3--->5 ..... 6--->4--->2

# single line if-else statement
res = "YES" if flag == 1 else "NO"  # res = "YES"

# single line for loop
arr = [(i + 1) * 10 for i in range(10)] # [10 20 30 ..... 80 90 100]

# n-sized array declaration
arr = [0] * 10  # [0 0 0 ..... 0 0 0]

# filter in array (single line for and if-else statement)
oddarr = [i for i in range(10) if i % 2 == 1] # [1 3 5 7 9]

# difference array 
diffarr = [abs(val - arr[i - 1]) for i, val in enumerate(arr, 0) if i > 0] # 2 2 2 1 2 2 2

# sort a 2D array by its 2nd value first and then by its 1st value
grid.sort(key = lambda x:(x[1], x[0]))  # [['banana', 20], ['grapes', 25], ['guava', 25], ['apple', 30], ['orange', 40],]

# inorder traversal of the binary search tree with a root node
return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right) if root else []

# if flag is true then print "YES" else print "NO"
print("YNEOS"[not flag::2]  # YES

# floor value without math.floor
print(val//2) # 2

# ceil value without math.ceil
print(-(-val//2)) # 3

# make hashmap out of keys array and values array
hp = dict(zip(letters, arr))
