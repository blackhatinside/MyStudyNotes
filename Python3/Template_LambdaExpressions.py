'''     // -- Template by A_*_A -- //       '''
inum = lambda: int(input())
imap = lambda: map(int, input().split())
itup = lambda: tuple(map(int, input().split()))
isor = lambda: sorted(map(int, input().split()))
isor2 = lambda nums: sorted(nums, key = lambda num1: (num1[0], num1[1]))
ilis = lambda: [int(zz) for zz in input().split()]
dd = lambda: collections.defaultdict(lambda:0)
adjlist = lambda: collections.defaultdict(lambda:[])
lcm = lambda num1, num2: num1 * num2 // math.gcd(num1, num2)
npr = lambda num1, num2: math.factorial(num1) // math.factorial(num1 - num2)
lowerpower = lambda num1, num2: pow(num2, math.floor(math.log(num1, num2)))
upperpower = lambda num1, num2: pow(num2, math.ceil(math.log(num1, num2)))
isperfectsquare = lambda num1: math.ceil(math.log(num1, 2)) == math.floor(math.log(num1, 2))
ncr = lambda num1, num2: math.factorial(num1) // (math.factorial(num2) * math.factorial(num1 - num2))
filtereven = lambda nums: list(filter(lambda num1: num1 % 2 == 0, nums))
filteroddd = lambda nums: list(filter(lambda num1: num1 % 2 != 0, nums))
fact = lambda num1: functools.reduce(lambda num2, num3: num2 * num3, range(1, num1 + 1))
freqarray = lambda nums: collections.Counter(nums)
bitsetarray = lambda nums: [int(num1) for num1 in bin(nums)[2:]]
lengthbitset = lambda num1: math.ceil(math.log(num1 + 0.1, 2))
bit_check = lambda num1, num2: num1 & (1 << num2)
bit_set = lambda num1, num2: num1 | (1 << num2)
bit_unset = lambda num1, num2: num1 & (~(1 << num2))
bit_toggle = lambda num1, num2: num1 ^ (1 << num2)
minheap = lambda nums: 1 if heapq.heapify(nums) == None else 0
maxheap = lambda nums: 1 if heapq._heapify_max(nums) == None else 0   # maybe deprecated!!!
lowerbound = lambda nums, key, start, stop: bisect.bisect_left(nums, key, lo=start, hi=stop)
upperbound = lambda nums, key, start, stop: bisect.bisect_right(nums, key, lo=start, hi=stop)
inorder = lambda root: inorder(root.left) + [root.val] + inorder(root.right) if root else []
pows2 = lambda num1: [1<<i for i in range(num1)]
prefixsumarray = lambda nums: list(itertools.accumulate(nums, lambda num1, num2: num1 + num2))
suffixsumarray = lambda nums: prefixsum(reversed(nums))
grid = lambda rows, cols: [[0 for j in range(cols)] for idx in range(rows)]
palindromeindices = lambda num1: [(num1 // 2 - i -(0 if num1 & 1 else 1), num1 // 2 + i) for i in range(num1 // 2 + (1 if num1 & 1 else 0))]
onum = lambda num1: '%d'%num1
omap = lambda num1, num2: '%d %d'%(num1,num2)
olis = lambda nums: ' '.join((str(nums[idx]) for idx in range(len(nums))))
odict = lambda nums: "\n".join((str("%idx: %s"%(num1[0], " ".join((str(num2) for num2 in num1[1])))) for num1 in zip(nums.keys(), nums.values())))
ogrid = lambda grid: '\n'.join((' '.join((str(num1) for num1 in nums)) for nums in grid))
input = lambda: sys.stdin.readline()
print = lambda nums: sys.stdout.write(nums + "\n")
'''     // -- Template by A_*_A -- //       '''
