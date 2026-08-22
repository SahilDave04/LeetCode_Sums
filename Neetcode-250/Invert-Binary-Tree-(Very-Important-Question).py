from utilities import TreeNode, only_function, createBinaryTree, printLinks

class Solution:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:
        if not root:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


root = [4,2,7,1,3,6,9]
output = only_function("invertTree", createBinaryTree(root))
print(output)


#Invert Binary Tree (Very Important Question)