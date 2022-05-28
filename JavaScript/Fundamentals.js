// # read line by line input from a file
let fs = require("fs");
let data = fs.readFileSync(0, "utf-8");
let idx = 0;
data = data.split("\n");
function input() {
  return data[idx++];
}

// # use let to reassign variables
let x = 10

// # get an integer input
let tcs = parseInt(input())

// # use const to make variable constant
const pi = 3.14

// # for loop
for (let i = 0; i < n; i++) {

}

// # declare an array of size n with all values as 0
let arr = Array(n).fill(0)

// # length of the array
let sz = arr.length

// # clear an array [all elements of the array are automatically deleted]
arr.length = 0

// # get an array input with space seperated (delimiter) integers
let arr = input().split(" ").map(Number)

// # technique: tree traversal
const ans = []
var inorderTraversalUtil = function(root) {
    if (root) {
        inorderTraversalUtil(root.left)
        ans.push(root.val)
        inorderTraversalUtil(root.right)
    }
}
var inorderTraversal = function(root) {
    ans.length = 0
    inorderTraversalUtil(root)
    return ans
}

// # spread operator for array
...arr

// # concatenation of 2 arrays
c = [...a,...b]

// # technique: binary search
var search = function(nums, target) {
    let beg = 0, end = nums.length - 1
    while (beg <= end) {
        mid = beg + ~~((end - beg) / 2)
        if (nums[mid] == target)
            return mid;
        else if (nums[mid] < target) {
            beg = mid + 1
        }
        else {
            end = mid - 1
        }
    }
    return -1;
};
