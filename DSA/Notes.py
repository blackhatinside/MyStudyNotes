
'''
Data Structures
    - Non Primitive
        * Linear
            # Static - Arrays
            # Dynamic - Linked Lists, Stacks, Queues
        * Non Linear - Trees, Graphs
    - Primitive - Int, Char, String, Boolean

Recursion: Performing the same operation multiple times with smaller inputs to reach the solution
    - Recursion consumes more space (due to stack)
    - Recursion takes more time (due to push and pop)
    - Use Recursion to traverse a Tree
    - Reduce time complexity using memoization
    
Notations:
    - Big O - complexity <= Worst case
    - Big Omega - complexity >= Best case
    - Big Theta - Worst case <= complexity <= Best case

Algorithm run-time complexities
O(1) - access element in array
O(n) - single loop
O(logn) - find in sorted array (for loop where controlling parameter reduces search space by 2 in every iteration)
O(nlogn) - sort an array
O(n2) - two nested loops
O(2n) - double recursion in Fibonacci

In Time and Space Complexity
    - Drop constant terms
    - Drop smaller terms (take only degree of the polynomial)

Time complexity of Recursion that makes multiple calls
- O(pow(branches, depth))

Array
    - position of each element can be calculated using its index using a formula
    - all the elements of n-dimensional array are stored in memory as a 1D array
    - insertions and deletions at the beginning of the array are costly - O(n)

Lists
    - append() have Amortized Average Case for n elements

Tuples
    - are immutable, comparable and hashable
    - faster access than lists

'''

# recursion
 def fact(n):
    assert int(n) == n and n >= 0, "The number must be a positive integer only"
    if n <= 0:
        return 1;
    else:
        return n * fact(n - 1)

# recursion
def fibo(n):
    assert int(n) == n and n >= 0, "Input takes numbers only!"
    if n in [0, 1]:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)
    
# recursion
def loop(n):
    assert int(n) == n and n >= 0
    if n == 0:
        return
    else:
        loop(n - 1)
        print(n)
        
# recursion
def sumofdigits(n):
    if 0 <= n < 10:
        return n
    else:
        ans = n % 10 + sumofdigits(n // 10)
        return ans
  
# recursion
def raisepower(base, power):
    if power == 0:
        return 1
    else:
        ans = base * raisepower(base, power - 1)
        return ans
    
# recursion
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
# recursion
def decimaltobinary(n):
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * binary(n // 2)
