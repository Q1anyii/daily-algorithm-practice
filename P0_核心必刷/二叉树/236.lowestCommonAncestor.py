"""
题目：236. 二叉树的最近公共祖先 (lowestCommonAncestor)
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
给定一个二叉树，找到该树中两个指定节点的最近公共祖先。
最近公共祖先的定义为：对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大。

示例 1：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
"""


# ==================== 解题思路 ====================
"""
公共祖先
即公共祖先能够向下查找到这两个节点，根节点一定是所有节点的公共祖先
动态更新祖先节点？
首先定义祖先节点为根节点，
判断目标节点是否在左子树还是右子树，
如果统一在左子树或右子树，那么就把根节点返回，
如果一左一右，那么就把左或右返回
"""

# ==================== 代码实现 ====================
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode | None':
        if not root: return None
        if root is q or root is p: return root
        left_sig = self.lowestCommonAncestor(root.left, p, q)
        right_sig = self.lowestCommonAncestor(root.right, p, q)
        if left_sig and right_sig: return root
        elif left_sig:
            return left_sig
        elif right_sig:
            return right_sig
        else:
            return None

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    #      3
    #     / \
    #    5   1
    #   / \ / \
    #  6  2 0 8
    #    / \
    #   7   4
    n7 = TreeNode(7); n4 = TreeNode(4)
    n2 = TreeNode(2, n7, n4); n6 = TreeNode(6)
    n5 = TreeNode(5, n6, n2); n0 = TreeNode(0); n8 = TreeNode(8)
    n1 = TreeNode(1, n0, n8); n3 = TreeNode(3, n5, n1)
    assert sol.lowestCommonAncestor(n3, n5, n1) is n3
    assert sol.lowestCommonAncestor(n3, n5, n4) is n5
    assert sol.lowestCommonAncestor(n3, n7, n4) is n2
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
