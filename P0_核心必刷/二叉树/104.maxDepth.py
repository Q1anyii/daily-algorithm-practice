"""
题目：104. 二叉树的最大深度 (maxDepth)
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
给定一个二叉树 root，返回其最大深度。
二叉树的最大深度是指从根节点到最远叶子节点的最长路径上的节点数。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：3
"""


# ==================== 解题思路 ====================
"""
解法一：
动态更新深度，若节点存在子节点，即更新深度
使用队列的思想？但空间复杂度高

解法二：
一路递归往下拆，直到碰到空节点（基线条件），然后开始回溯并加上自身这一层。
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root: return 0
        # max_depth = 0
        # from collections import deque
        # q = deque([root])
        # while q:
        #     cur_size = len(q)
        #     cur_level = []
        #     for _ in range(cur_size):
        #         node = q.popleft()
        #         cur_level.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     max_depth += 1
        # return max_depth
        if not root: return 0
        """
        若两个节点都无子节点，那么就把这一层的深度返回
        """
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1



# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    #    3
    #   / \
    #  9  20
    #     / \
    #    15  7
    n15 = TreeNode(15); n7 = TreeNode(7)
    n20 = TreeNode(20, n15, n7); n9 = TreeNode(9)
    n3 = TreeNode(3, n9, n20)
    assert sol.maxDepth(n3) == 3
    assert sol.maxDepth(None) == 0
    assert sol.maxDepth(TreeNode(1)) == 1
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
