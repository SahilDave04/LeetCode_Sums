from utilities import TreeNode, only_function, createBinaryTree, printLinks

class Solution:
    def maxDepth(self, root: [TreeNode]) -> int:
        def recursiveDFS():
            if not root:
                return 0

            return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        
        def iterativeBFS():
            if not root:
                return 0
            stack = [[root,1]]
            res = 0

            while stack:
                node, depth = stack.pop()

                if node:
                    res = max(res, depth)
                    stack.append([node.left,depth+1])
                    stack.append([node.right,depth+1])
            return res
        
        return recursiveDFS(), iterativeBFS()



root = [1,None,2]
output = only_function("maxDepth", createBinaryTree(root))
print(output)


#Maximum Depth of Binary Tree (Very Important Question)