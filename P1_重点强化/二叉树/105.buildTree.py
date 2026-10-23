"""
题目：105. 从前序与中序遍历序列构造二叉树 (buildTree)
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
给定两个整数数组 preorder 和 inorder，其中 preorder 是二叉树的先序遍历，inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

示例 1：
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
"""


# ==================== 解题思路 ====================
"""
根据二叉树的前序与中序遍历结果构造二叉树
前序遍历： 根-左-右     中序遍历： 左-根-右     后序遍历： 左-右-根
 
 原图：
        3
       / \
      9   20
         /  \
        15   7
        
    中序如何找到根的位置？前序遍历第一个一定是根，所以可以通过遍历查找到根
    中序遍历一定是左节点-根节点-右节点顺序，那么找到根节点后，左右节点就可以

"""

# ==================== 代码实现 ====================
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            if not left : return None
            root_node = left[0]
            root_idx = 0
            for i in range(len(right)):
                if right[i] == root_node:
                    root_idx = i
            left_tree = build(left[1: root_idx + 1], right[:root_idx])
            right_tree = build(left[root_idx + 1:], right[root_idx + 1:])
            root = TreeNode(root_node, left_tree, right_tree)
            return root
        return build(preorder, inorder)

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    result = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert result.val == 3
    assert result.left.val == 9
    assert result.right.val == 20
    assert result.right.left.val == 15
    assert result.right.right.val == 7
    r2 = sol.buildTree([-1], [-1])
    assert r2.val == -1
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
