"""
题目：226. 翻转二叉树 (invertTree)
难度：简单
分类：二叉树
"""

from typing import List, Optional, Dict, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ==================== 题目描述 ====================
"""
给你一棵二叉树的根节点 root，翻转这棵二叉树，并返回其根节点。

示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
"""


# ==================== 解题思路 ====================
"""
翻转树，左左=右右，左右=右左，和判断是否是对称二叉树有点像
        root.left, root.right = root.right, root.left
        root.left.left, root.right.right = root.right.right, root.left.left
        root.left.right, root.right.left = root.right.left, root.left.right
        这样循环往复直到root为空
"""

class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root: return None
        left, right = root.left, root.right
        root.left = self.invertTree(right)
        root.right = self.invertTree(left)
        return root


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    #     4
    #    / \
    #   2   7
    #  / \ / \
    # 1  3 6  9
    n1 = TreeNode(1); n3 = TreeNode(3); n6 = TreeNode(6); n9 = TreeNode(9)
    n2 = TreeNode(2, n1, n3); n7 = TreeNode(7, n6, n9)
    n4 = TreeNode(4, n2, n7)
    result = sol.invertTree(n4)
    # 翻转后: 4->left 7, 4->right 2
    assert result.left.val == 7
    assert result.right.val == 2
    assert result.left.left.val == 9
    assert result.left.right.val == 6
    assert sol.invertTree(None) is None
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
