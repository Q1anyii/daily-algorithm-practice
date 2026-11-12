"""
题目：94. 二叉树的中序遍历 (inorderTraversal)
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
给定一个二叉树的根节点 root，返回它的中序遍历。

示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]

示例 2：
输入：root = []
输出：[]
"""


# ==================== 解题思路 ====================
"""
中序遍历：左-根-右
那么就需要判断是否有左右子节点，
设置stack栈机制
if node not none: stack.append(node) as the last one
node = node.left until node.left is none
node = stack.pop 
res.append(node.val) cause the deeply left has no sub-left or sub-right
so can append it directly
and get right node 
if right-node is none: return last-second node 
stack can solve this helpful
"""

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root: return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

        stack = []
        res = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right

        return res


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    # 1->right 2->left 3
    n3 = TreeNode(3)
    n2 = TreeNode(2, n3, None)
    n1 = TreeNode(1, None, n2)
    assert sol.inorderTraversal(n1) == [1, 3, 2]
    assert sol.inorderTraversal(None) == []
    single = TreeNode(1)
    assert sol.inorderTraversal(single) == [1]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
