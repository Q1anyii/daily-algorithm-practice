"""
题目：543. 二叉树的直径 (diameterOfBinaryTree)
难度：简单
分类：二叉树
"""
import time
from typing import List, Optional, Dict, Tuple

from networkx.algorithms.approximation.distance_measures import diameter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ==================== 题目描述 ====================
"""
给你一棵二叉树的根节点，返回该树的直径。
二叉树的直径是指树中任意两个节点之间最长路径的长度。这条路径可能经过也可能不经过根节点 root。
两节点之间路径的长度由它们之间边数表示。

示例 1：
输入：root = [1,2,3,4,5]
输出：3
"""


# ==================== 解题思路 ====================
"""
动态更新最长，路径即两个点之间的边的数量，向下查询深度？
最长路径，那么就需要找到最深节点？然后计算根节点与最深节点的边数量？
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.diameter = 0
        def depth(node):
            if not node: return 0
            left = depth(node.left)
            right = depth(node.right)
            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1
        depth(root)
        return self.diameter

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    #   1
    #  / \
    # 2   3
    #/ \
    #4 5
    n4 = TreeNode(4); n5 = TreeNode(5)
    n2 = TreeNode(2, n4, n5); n3 = TreeNode(3)
    n1 = TreeNode(1, n2, n3)
    assert sol.diameterOfBinaryTree(n1) == 3
    assert sol.diameterOfBinaryTree(None) == 0
    assert sol.diameterOfBinaryTree(TreeNode(1)) == 0
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
