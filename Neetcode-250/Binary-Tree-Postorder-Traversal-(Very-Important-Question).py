from utilities import TreeNode, only_function, createBinaryTree, printLinks

class Solution:
    def preorderTraversal(self, root: [TreeNode]) -> list[int]:
        res, stack, freqs = [], [root], [False]
          
        while stack:
            cur, v = stack.pop(), freqs.pop()

            if cur:
                if v:
                    res.append(cur.val)
                else:
                    stack.append(cur)
                    freqs.append(True)
                    stack.append(cur.right)
                    freqs.append(False)
                    stack.append(cur.left)
                    freqs.append(False)
        return res

root = [1,2,3,4,5,None,8,None,None,6,7,9]
output = only_function("preorderTraversal", createBinaryTree(root))
print(output)


#Binary Tree Postorder Traversal (Very Important Question)