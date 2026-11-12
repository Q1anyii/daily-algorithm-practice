"""
题目：102. 二叉树的层序遍历 (levelOrder)
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
给你二叉树的根节点 root，返回其节点值的层序遍历。（即逐层地，从左到右访问所有节点）。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
"""


# ==================== 解题思路 ====================
"""
队列存储，可以根据从左到右，从上到下的顺序，依次popleft取。
这样就可以按顺序逐个存入和取出
"""

# ==================== 代码实现 ====================
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        from collections import deque
        queue = deque([root])
        #每一次queue判断就是对一层的遍历
        while queue:
            #获取cur_size,这取决于当前层级有多少个节点，从而逐个获取
            cur_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                cur_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(cur_level)
        return res

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    n15 = TreeNode(15); n7 = TreeNode(7)
    n20 = TreeNode(20, n15, n7); n9 = TreeNode(9)
    n3 = TreeNode(3, n9, n20)
    assert sol.levelOrder(n3) == [[3], [9, 20], [15, 7]]
    assert sol.levelOrder(None) == []
    assert sol.levelOrder(TreeNode(1)) == [[1]]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
