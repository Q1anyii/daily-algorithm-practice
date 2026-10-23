class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 前序遍历（根左右）：递归模板
    def preorder(self, root):
        if not root:
            return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)

    # 中序（左根右）/ 后序（左右根）同理改顺序

    # 最大深度
    def max_depth(self, root):
        if not root:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))