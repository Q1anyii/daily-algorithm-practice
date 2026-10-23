"""
题目：230. 二叉搜索树中第 K 小的元素 (kthSmallest)
难度：中等
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
给定一个二叉搜索树的根节点 root，和一个整数 k，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

示例 1：
输入：root = [3,1,4,null,2], k = 1
输出：1
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    #   3
    #  / \
    # 1   4
    #  \
    #   2
    n2 = TreeNode(2); n1 = TreeNode(1, None, n2)
    n4 = TreeNode(4); n3 = TreeNode(3, n1, n4)
    assert sol.kthSmallest(n3, 1) == 1
    assert sol.kthSmallest(n3, 2) == 2
    assert sol.kthSmallest(n3, 3) == 3
    assert sol.kthSmallest(n3, 4) == 4
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
