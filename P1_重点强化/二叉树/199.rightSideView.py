"""
题目：199. 二叉树的右视图 (rightSideView)
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
给定一个二叉树的根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例 1：
输入: [1,2,3,null,5,null,4]
输出: [1,3,4]
"""


# ==================== 解题思路 ====================
"""
层序遍历
每一层逐个遍历
把每一层的最右边元素添加到res中，
那么这样就需要逐层判断是否有右子节点，否则直接添加左子节点
"""

# ==================== 代码实现 ====================
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root: return []
        queue = deque([root])
        res = []
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if i == n - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res




# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    n5 = TreeNode(5); n4 = TreeNode(4)
    n2 = TreeNode(2, None, n5); n3 = TreeNode(3, None, n4)
    n1 = TreeNode(1, n2, n3)
    assert sol.rightSideView(n1) == [1, 3, 4]
    assert sol.rightSideView(None) == []
    assert sol.rightSideView(TreeNode(1)) == [1]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
