n = 10
sz = 3

tetris = [[] for _ in range(n)]

def isValid(arr):
	flag = 0
	if arr == [1, 1, 1]:
		flag = 1
	elif arr == [3]:
		flag = 2
	elif arr == [1, 2, 1]:
		flag = 1
	# elif arr = [1, -2, 1]:
	# 	flag = True
	# elif arr = [1, 3, 1]:
	# 	flag = True
	else:
		flag = 0
	return flag

turns = int(input("How many turns do you want: "))
score = 0
ceiling = int(input("Enter the height of the room (NOTE: width = 10): "))
height = 0

while turns:
	arr = list(map(int, input("Enter the shape: ").split()))
	print(arr)
	check = isValid(arr)
	if not check:
		print("Game Over")
		break
	index = int(input("Enter the index: "))
	if len(arr) == sz and index in [1, n]:
		print("Game Over")
		break
	index -= 1
	if check == 2:
		for i in range(3): tetris[index].append("*")
		height = max(height, len(tetris[index]))
	elif check == 1:
		for i in range(arr[0]): tetris[index - 1].append("*")
		for i in range(arr[1]): tetris[index].append("*")
		for i in range(arr[2]): tetris[index + 1].append("*")
		left = len(tetris[index - 1])
		mid = len(tetris[index])
		right = len(tetris[index + 1])
		height = max(left, mid, right, height)
	if height > ceiling:
		print("You lost!")
		break
	elif height == ceiling:
		print("You won!")
		break
	else:
		# print("DEBUG: ", height, ceiling, check)
		pass
	turns -= 1
	for i in range(n):
		if len(tetris[i]) and len(tetris[i]) % 4 == 0:
			for j in range(4):
				tetris[i].pop()
	print(tetris)
	if turns == 0:
		print("You lost!")
