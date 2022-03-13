"""
# Definition for a Node.
class Node:
    def __init__(self, val = None, children = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        nodes = []
        def TraversalUtil(root):
            if not root:
                return
            
            nodes.append(root.val)
            
            for child in root.children:
                TraversalUtil(child)
            
#             if root.left:
#                 TraversalUtil(root.left)
                
#             if root.right:
#                 TraversalUtil(root.right)
                
        TraversalUtil(root)
        return nodes

'''	Leetcode List : https://leetcode.com/list/9n8rhk1m	'''
# inorderTraversal : Given a binary tree root, return an inorder traversal of root as a list
# preorderTraversal : Given a binary tree root, return a preorder traversal of root as a list
# postorderTraversal : Given a binary tree root, return a postorder traversal of root as a list
# maxDepth : Given the root of a binary tree, return its maximum depth i.e. its height
# levelOrder : Given a binary tree root, return the level order traversal of root as a list
# zigzagLevelOrder : Given a binary tree root, return the zigzag level order traversal of its nodes' values
# lowestCommonAncestor :
# invertTree : 
# sortedArrayToBST :
# isValidBST :
# searchBST :
# verticalTraversal :
# rangeSumBST :
# levelOrderNary :
# mergeTrees :
# maxDepth :
# preorder :
# postorder :
# pathSum :



# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BinaryTree:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # INORDER TRAVERSAL ==> LEFT CHILD >> ROOT >> RIGHT CHILD
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else list()
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # PREORDER - ROOT >> LEFT CHILD >> RIGHT CHILD 
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else list()
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
	# POSTORDER TRAVERSAL ==> LEFT CHILD >> RIGHT CHILD >> ROOT
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else list()
    def maxDepth(self, root: Optional[TreeNode]) -> int:	#height()
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q, result, beg, x = [root,], [], 0, 0
        while q:
            print(x)
            level=[]
            for i in range(len(q)):
                node=q.pop()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.insert(beg, node.left)
                    if node.right:
                        q.insert(beg, node.right)
            if level:
                    result.append(level)
            x = x + 1
        return result
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res, q, direction = [], [root], 1
        if root:
            while q:
                temp = list()
                for i in range(len(q)):
                    node = q.pop(0)
                    temp.append(node.val)
                    q += [e for e in (node.left, node.right) if e]
                res += [temp[::direction]]
                direction *= -1
        return res
    def lowestCommonAncestor(self, root: 'TreeNode', n1: 'TreeNode', n2: 'TreeNode') -> 'TreeNode':
        if root in (None, n1, n2):
            return root
        left = self.lowestCommonAncestor(root.left, n1, n2)
        right = self.lowestCommonAncestor(root.right, n1, n2)
        if left and right:
            return root 
        else:
            return left or right
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[ :mid])
        root.right = self.sortedArrayToBST(nums[mid + 1: ])
        return root
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkBST(root, l, r):
            if root:
                if root.val > l and root.val < r:
                    if checkBST(root.left, l, root.val) and checkBST(root.right, root.val, r):
                        return True
                return False
            return True
        return checkBST(root, float("-inf"), float("inf"))
    def searchBST(self, root: Optional[TreeNode], k: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if k < root.val:
            return self.searchBST(root.left, k)
        if k > root.val:
            return self.searchBST(root.right, k)
        return root
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hp = collections.defaultdict(list)
        q = [(root, 0, 0)]
        ans = []
        while q:
            for ele in range(len(q)):
                node, col, row = q.pop(0)	# row and col are used to track hor. & ver. dist. of node
                hp[col].append((row, node.val))
                if node.left:
                    q.append((node.left, col - 1, row + 1))
                if node.right:
                    q.append((node.right, col + 1, row + 1))
        for i in sorted(hp.keys()):
            level = [x[1] for x in sorted(hp[i], key = lambda x: (x[0], x[1]))]   
            ans.append(level)
        return ans
    def rangeSumBST(self, root: Optional[TreeNode], l: int, h: int) -> int:
        if root:
            if (l <= root.val and root.val <= h):
                return self.rangeSumBST(root.left, l, h) + root.val + self.rangeSumBST(root.right, l, h)
            else:
                return self.rangeSumBST(root.left, l, h) + self.rangeSumBST(root.right, l, h)
        return 0
    def levelOrderNary(self, root: 'Node') -> List[List[int]]:
        q, res, beg = [root,], [], 0
        while q:
            level = []
            for i in range(len(q)):
                node = q.pop()
                if node:
                    level.append(node.val)
                    q = [e for e in (node.children) if e] + q
            if level:
                res.append(level[::-1])
        return res
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return TreeNode(root1.val + root2.val, self.mergeTrees(root1.left,  root2.left),  self.mergeTrees(root1.right, root2.right)) if (root1 and root2) else root1 or root2
    def maxDepth(self, root: 'Node') -> int:
        return max([self.maxDepth(child) for child in root.children], default = 0) + 1 if root else 0
    def preorder(self, root: 'Node') -> List[int]:	# N-ary Tree Preorder Traversal
        return [root.val] + [ele for child in root.children for ele in self.preorder(child)] if root else []
    def postorder(self, root: 'Node') -> List[int]:	# N-ary Tree Postorder Traversal
        return [val for child in root.children for val in self.postorder(child)] + [root.val] if root else [] 
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, k, [], res, 0)
        return res
    def pathSum_util(self, root, k, ls, res, tot):
        if root != None:
            ls = ls + [root.val]      # root definitely has a value
            tot += root.val
            if root.left == None and root.right == None:
                if k == tot:
                    res.append(ls)
            self.pathSum_util(root.left, k, ls, res, tot)
            self.pathSum_util(root.right, k, ls, res, tot)
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def LevelOrderSum(root):
            q = []
            q.append(root)
            levels = []
            while q:
                ans = 0 # will update the level sum at each level till last level
                currentSize = len(q) # size of the queue = no. of elements in current level
                for _ in range(currentSize): # iterating over the current level nodes
                    ele = q.pop(0)
                    ans += ele.val
                    if ele.left:    # check if left child exists
                        q.append(ele.left)
                    if ele.right:   # check if right child exists
                        q.append(ele.right)
                levels.append(ans)
            return levels
        lvls = LevelOrderSum(root)
        ind, maxx = -1, -sys.maxsize
        for i in range(len(lvls)):
            if lvls[i] > maxx:
                maxx = lvls[i]
                ind = i + 1
        return ind
