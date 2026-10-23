"""
题目：2. 两数相加 (addTwoNumbers)
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
给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。

示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    # 342 + 465 = 807
    a1 = ListNode(2); a2 = ListNode(4); a3 = ListNode(3)
    a1.next = a2; a2.next = a3
    b1 = ListNode(5); b2 = ListNode(6); b3 = ListNode(4)
    b1.next = b2; b2.next = b3
    result = sol.addTwoNumbers(a1, b1)
    vals = []
    while result:
        vals.append(result.val)
        result = result.next
    assert vals == [7, 0, 8]
    # 0 + 0 = 0
    z1 = ListNode(0); z2 = ListNode(0)
    r = sol.addTwoNumbers(z1, z2)
    assert r.val == 0 and r.next is None
    # 999 + 1 = 1000
    c1 = ListNode(9); c2 = ListNode(9); c3 = ListNode(9)
    c1.next = c2; c2.next = c3
    d1 = ListNode(1)
    r2 = sol.addTwoNumbers(c1, d1)
    v2 = []
    while r2:
        v2.append(r2.val)
        r2 = r2.next
    assert v2 == [0, 0, 0, 1]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
