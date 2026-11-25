"""
题目：94. 二叉树的中序遍历 (inorderTraversal)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ==================== 题目描述 ====================
"""
给定一个二叉树的根节点 root，返回它的中序遍历。

示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]
"""


# ==================== 代码实现 ====================
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if not root: return []
        # return (self.inorderTraversal(root.left) +
        #         [root.val] +
        #         self.inorderTraversal(root.right))

        res = []; stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


# ==================== 测试用例 ====================
def build_tree(values):
    """按层序数组构造二叉树，None 表示空节点"""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def test_solution():
    sol = Solution()
    assert sol.inorderTraversal(build_tree([1, None, 2, 3])) == [1, 3, 2]
    assert sol.inorderTraversal(build_tree([])) == []
    assert sol.inorderTraversal(build_tree([1])) == [1]
    assert sol.inorderTraversal(build_tree([1, 2, 3, 4, 5])) == [4, 2, 5, 1, 3]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
