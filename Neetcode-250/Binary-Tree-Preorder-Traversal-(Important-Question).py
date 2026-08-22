from utilities import TreeNode, only_function, createBinaryTree, printLinks

class Solution:
    def preorderTraversal(self, root: [TreeNode]) -> list[int]:
        res = []
        stack = []
        cur = root

        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()
        
        return res

root = [1,2,3,4,5,None,8,None,None,6,7,9]
output = only_function("preorderTraversal", createBinaryTree(root))
print(output)


#Binary Tree Preorder Traversal (Important Question)