from utilities import TreeNode, only_function, createBinaryTree, printLinks

class Solution:
    def inorderTraversal(self, root: [TreeNode]) -> list[int]:
        def iterativeSol():
            res = []
            stack = []
            cur = root

            while cur or stack:
                while cur:
                    stack.append(cur)
                    cur = cur.left
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right

            return res

        def recursiveSol():
            res = []

            def inorder(root):
                if not root:
                    return
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)

            inorder(root)
            return res
        
        return recursiveSol(), iterativeSol()

root = [1,None,2,3]
output = only_function("inorderTraversal", createBinaryTree(root))
print(output)


#Binary Tree Inorder Traversal (Important Question)