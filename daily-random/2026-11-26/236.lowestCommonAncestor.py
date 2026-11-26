"""
题目：236. 二叉树的最近公共祖先 (lowestCommonAncestor)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ==================== 题目描述 ====================
"""
给定一个二叉树，找到该树中两个指定节点的最近公共祖先。

最近公共祖先的定义为：对于有根树 T 的两个节点 p、q，
最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大
（一个节点也可以是它自己的祖先）。

示例 1：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3。

示例 2：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5，因为根据定义最近公共祖先节点可以为节点本身。

示例 3：
输入：root = [1,2], p = 1, q = 2
输出：1

提示：
树中节点数目在范围 [2, 10^5] 内
所有 Node.val 互不相同
p != q
p 和 q 均存在于给定的二叉树中
"""


# ==================== 代码实现 ====================
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> Optional['TreeNode']:
        if not root or root is p or root is q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root


# ==================== 测试用例 ====================
def build_tree(values):
    """按层序数组构造二叉树，None 表示空节点；同时返回按 val 索引的节点表"""
    if not values:
        return None, {}
    root = TreeNode(values[0])
    nodes = {root.val: root}
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            nodes[values[i]] = node.left
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            nodes[values[i]] = node.right
            queue.append(node.right)
        i += 1
    return root, nodes


TREE = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]


def test_solution():
    sol = Solution()

    # 示例 1：p、q 分居左右子树 → 根
    root, nodes = build_tree(TREE)
    assert sol.lowestCommonAncestor(root, nodes[5], nodes[1]) is nodes[3]

    # 示例 2：q 在 p 的子树里 → p 自己就是答案
    root, nodes = build_tree(TREE)
    assert sol.lowestCommonAncestor(root, nodes[5], nodes[4]) is nodes[5]

    # 兄弟节点，都在 node2 之下
    root, nodes = build_tree(TREE)
    assert sol.lowestCommonAncestor(root, nodes[7], nodes[4]) is nodes[2]

    # 深层节点与浅层节点
    root, nodes = build_tree(TREE)
    assert sol.lowestCommonAncestor(root, nodes[6], nodes[8]) is nodes[3]

    # 示例 3：只有两个节点，答案是根
    root, nodes = build_tree([1, 2])
    assert sol.lowestCommonAncestor(root, nodes[1], nodes[2]) is nodes[1]

    # 左斜树，最深的节点与最浅的节点
    root, nodes = build_tree([1, 2, None, 3])
    assert sol.lowestCommonAncestor(root, nodes[1], nodes[3]) is nodes[1]

    # 右斜树
    root, nodes = build_tree([1, None, 2, None, 3])
    assert sol.lowestCommonAncestor(root, nodes[2], nodes[3]) is nodes[2]

    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
