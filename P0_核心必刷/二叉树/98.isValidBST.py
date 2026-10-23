"""
题目：98. 验证二叉搜索树 (isValidBST)
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
给你一个二叉树的根节点 root，判断其是否是一个有效的二叉搜索树。
有效二叉搜索树定义如下：
- 节点的左子树只包含小于当前节点的数。
- 节点的右子树只包含大于当前节点的数。
- 所有左子树和右子树自身必须也是二叉搜索树。

示例 1：
输入：root = [2,1,3]
输出：true
"""


# ==================== 解题思路 ====================
"""
左子树只包含比当前小的节点数， if cur.left > cur : return false
right-sub-tree only include node value that more than curr: if cur.right < cur : return false
all trees must have left or right
"""

# ==================== 代码实现 ====================
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def validate(node, low=float("-inf"), high=float("inf")):
            if not node: return True
            if not (low < node.val < high): return False
            left_true = validate(node.left, low, node.val)
            right_true = validate(node.right, node.val, high)
            return left_true and right_true
        return validate(root)


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    n1 = TreeNode(1); n3 = TreeNode(3)
    n2 = TreeNode(2, n1, n3)
    assert sol.isValidBST(n2) is True
    # 无效: 5->left 4, 5->right 6->left 3 (3 < 5 但在右子树中)
    m3 = TreeNode(3); m7 = TreeNode(7)
    m6 = TreeNode(6, m3, m7); m4 = TreeNode(4)
    m5 = TreeNode(5, m4, m6)
    assert sol.isValidBST(m5) is False
    assert sol.isValidBST(None) is True
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
