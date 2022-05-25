// # use let to reassign variables
let x = 10

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
