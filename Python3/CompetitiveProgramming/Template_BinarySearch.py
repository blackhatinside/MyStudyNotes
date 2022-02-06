def binSearch_iter(arr, key):
	beg, end = 0, len(arr) - 1
	while beg <= end:
		mid = beg + (end - beg) // 2  # to avoid mid overflow
		if key == arr[mid]:
			return True
		elif key < arr[mid]:
			end = mid - 1
		else:
			beg = mid + 1
	return False
# arr = [84, 21, 47, 96, 15,]
# print(binSearch_iter(arr, 96))

def binSearch_recur(arr, key, beg, end):
	if beg > end:
		return False
	else:
		mid = (beg + end) // 2
		if key == arr[mid]:
			return True
		elif key < arr[mid]:
			return binSearch_recur(arr, key, beg, mid - 1)
		else:
			return binSearch_recur(arr, key, mid + 1, end)
# arr = [84, 21, 47, 96, 15]
# print(binSearch_recur(arr, 96, 0, arr(len) - 1))

'''https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/promotion-1/'''
def isPossible(box, man, n, m, min_dist):
    tmp, tot = 0, 0
    while tot < m:
        j = 0
        while j < min_dist and tmp < n and man[tot] >= box[tmp]:
            tmp += 1
            j += 2
        tot += 1
    if tmp == n:
        return True
    return False

def dist(box, man, nb, nm):
    box.sort(); man.sort();
    beg, end = 0, 2 * nb
    min_dist = 0
    while beg <= end:   # binary search
        mid = beg + (end - beg) // 2
        if isPossible(box, man, nb, nm, mid):
            min_dist = mid
            end = mid - 1
        else :
            beg = mid + 1
    return min_dist

n_b, n_m = map(int, input().split())
box_arr = list(map(int, input().split()))
man_arr = list(map(int, input().split()))
print(dist(box_arr, man_arr, n_b, n_m))
