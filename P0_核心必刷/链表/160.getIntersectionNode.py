"""
题目：160. 相交链表 (getIntersectionNode)
难度：简单
分类：链表
"""

from typing import List, Optional, Dict, Tuple

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ==================== 题目描述 ====================
"""
给你两个单链表的头节点 headA 和 headB，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null。

示例 1：
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]
输出：Intersected at '8'
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    # 构造相交链表
    # A: 4->1->8->4->5
    # B: 5->6->1->8->4->5 (相交于8)
    a1 = ListNode(4); a2 = ListNode(1)
    c1 = ListNode(8); c2 = ListNode(4); c3 = ListNode(5)
    a1.next = a2; a2.next = c1; c1.next = c2; c2.next = c3
    b1 = ListNode(5); b2 = ListNode(6); b3 = ListNode(1)
    b1.next = b2; b2.next = b3; b3.next = c1
    sol = Solution()
    assert sol.getIntersectionNode(a1, b1) is c1
    # 不相交
    d1 = ListNode(1); d2 = ListNode(2)
    assert sol.getIntersectionNode(d1, d2) is None
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
