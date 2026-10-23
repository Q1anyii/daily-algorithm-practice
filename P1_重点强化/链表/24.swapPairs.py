"""
题目：24. 两两交换链表中的节点 (swapPairs)
难度：中等
分类：链表
"""

from typing import List, Optional, Dict, Tuple

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ==================== 题目描述 ====================
"""
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题。

示例 1：
输入：head = [1,2,3,4]
输出：[2,1,4,3]

示例 2：
输入：head = []
输出：[]
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    n1 = ListNode(1); n2 = ListNode(2); n3 = ListNode(3); n4 = ListNode(4)
    n1.next = n2; n2.next = n3; n3.next = n4
    result = sol.swapPairs(n1)
    vals = []
    while result:
        vals.append(result.val)
        result = result.next
    assert vals == [2, 1, 4, 3]
    assert sol.swapPairs(None) is None
    s1 = ListNode(1)
    r = sol.swapPairs(s1)
    assert r.val == 1 and r.next is None
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
