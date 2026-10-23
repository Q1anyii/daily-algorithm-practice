"""
题目：114. 二叉树展开为链表 (flatten)
难度：中等
分类：二叉树
"""

from typing import List, Optional, Dict, Tuple

from fontTools.varLib.mutator import prev


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ==================== 题目描述 ====================
"""
给你二叉树的根结点 root，请你将它展开为一个单链表：
- 展开后的单链表应该同样使用 TreeNode，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null。
- 展开后的单链表应该与二叉树先序遍历顺序相同。

示例 1：
输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]
"""


# ==================== 解题思路 ====================
"""
按先序的 "反向顺序" 处理节点—— 先序是 根 - 左 - 右，那反过来就是 右 - 左 - 根
6-5-4-3-2-1
如果按这个顺序逐个处理，每处理到一个节点时，
它的 "先序后继"（下一个该接在它后面的节点）已经被处理过了
—— 这时只需要做一件事：把当前节点的 `right` 指向 "已经处理好的一条链"。
"""

# ==================== 代码实现 ====================
class Solution:
    # def __init__(self):
    #     self.prev = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        # if not root: return None
        # self.flatten(root.right)
        # self.flatten(root.left)
        # root.right = self.prev
        # root.left = None
        # self.prev = root
        prev = None
        def dfs(node):
            nonlocal prev
            if not node: return None
            dfs(node.right)
            dfs(node.left)
            node.right = prev
            node.left = None
            prev = node
            return None
        dfs(root)

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    #    1
    #   / \
    #  2   5
    # / \   \
    #3  4    6
    n3 = TreeNode(3); n4 = TreeNode(4)
    n2 = TreeNode(2, n3, n4); n6 = TreeNode(6)
    n5 = TreeNode(5, None, n6); n1 = TreeNode(1, n2, n5)
    sol.flatten(n1)
    vals = []
    curr = n1
    while curr:
        vals.append(curr.val)
        assert curr.left is None
        curr = curr.right
    assert vals == [1, 2, 3, 4, 5, 6]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
