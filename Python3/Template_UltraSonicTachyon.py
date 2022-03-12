# CALL YOUR MODULES HERE	-------------------->
# import bisect, heapq
# import fractions, math, numpy
import atexit, io, os, sys, time
#		<----------------------------------------

# DEFINE YOUR FASTIO HERE	-------------------->
# 0 in os.read() indicated file descriptor for standard input (STDIN)
# os.fstat(0).st_size will tell Python how many bytes are currently waiting in the STDIN buffer
# Then os.read() will read those bytes in bulk from STDIN, producing a bytestring
inputt = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# A lambda function to get integer input and return it
input = lambda: inputt()   # integers
# A lambda function to get string input and return it
# input = lambda: inputt().decode().strip()   # strings
# ss = sys.stdout
ss = io.BytesIO()
_write = ss.write
ss.write = lambda s: _write(s.encode())
atexit.register(lambda: os.write(1, ss.getvalue()))
#		<----------------------------------------

# DEFINE YOUR FUNCTIONS HERE	-------------------->
# def readnumbers(zero=0):
#     _ord, nums, num, neg = lambda x: x, [], zero, False
#     i, s = 0, io.BytesIO(os.read(0,os.fstat(0).st_size)).read()
#     try:
#         while True:
#             if s[i] >= b"0"[0]:num = 10 * num + _ord(s[i]) - 48
#             elif s[i] == b"-"[0]:neg = True
#             elif s[i] != b"\r"[0]:
#                 nums.append(-num if neg else num)
#                 num, neg = zero, False
#             i += 1
#     except IndexError:
#         pass
#     if s and s[-1] >= b"0"[0]: nums.append(-num if neg else num)
#     return nums
# def FastInt(zero=0):
#     _ord, nums, num, neg = lambda x: x, [], zero, False
#     i, s = 0, io.BytesIO(os.read(0,os.fstat(0).st_size)).read()
#     try:
#         while True:
#             if s[i] >= b"0"[0]:num = 10 * num + _ord(s[i]) - 48
#             elif s[i] == b"-"[0]:neg = True
#             elif s[i] != b"\r"[0]:
#                 nums.append(-num if neg else num)
#                 num, neg = zero, False
#             i += 1
#     except IndexError:
#         pass
#     if s and s[-1] >= b"0"[0]: nums.append(-num if neg else num)
#     return nums
#		<----------------------------------------

# ENTER YOUR CODE HERE	-------------------->
     
def main():
	print("Hello World")
	# word = input()
	# num = int(input())
	# arr = list(map(int, input().split()))
	return

if __name__ == '__main__':
	main()

#		<----------------------------------------
# ENTER YOUR NOTES HERE	-------------------->
'''		# NOTES	- uncomment line to run this block

Python Competitive Programming Template for FAST I/O 

# '''
#		<----------------------------------------
