"""
题目：437. 路径总和 III (pathSum)
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
给定一个二叉树的根节点 root，和一个整数 targetSum，求该二叉树里节点值之和等于 targetSum 的路径的数目。
路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

示例 1：
输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # TODO: 实现该方法
        pass
        def dfs(node, current_sum):
            # TODO: 实现该方法
            pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    #       10
    #      /  \
    #     5   -3
    #    / \    \
    #   3   2   11
    #  / \   \
    # 3  -2   1
    n3a = TreeNode(3); n_2 = TreeNode(-2)
    n3b = TreeNode(3, n3a, n_2); n1 = TreeNode(1)
    n2 = TreeNode(2, None, n1); n11 = TreeNode(11)
    n5 = TreeNode(5, n3b, n2); n_3 = TreeNode(-3, None, n11)
    n10 = TreeNode(10, n5, n_3)
    assert sol.pathSum(n10, 8) == 3
    assert sol.pathSum(None, 8) == 0
    assert sol.pathSum(TreeNode(1), 1) == 1
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
