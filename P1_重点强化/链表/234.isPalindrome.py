"""
题目：234. 回文链表 (isPalindrome)
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
给你一个单链表的头节点 head，请你判断该链表是否为回文链表。如果是，返回 true；否则，返回 false。

示例 1：
输入：head = [1,2,2,1]
输出：true

示例 2：
输入：head = [1,2]
输出：false
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    # 1->2->2->1
    n1 = ListNode(1); n2 = ListNode(2); n3 = ListNode(2); n4 = ListNode(1)
    n1.next = n2; n2.next = n3; n3.next = n4
    assert sol.isPalindrome(n1) is True
    # 1->2
    m1 = ListNode(1); m2 = ListNode(2)
    m1.next = m2
    assert sol.isPalindrome(m1) is False
    # 单节点
    assert sol.isPalindrome(ListNode(1)) is True
    # 1->2->3->2->1
    p1 = ListNode(1); p2 = ListNode(2); p3 = ListNode(3); p4 = ListNode(2); p5 = ListNode(1)
    p1.next = p2; p2.next = p3; p3.next = p4; p4.next = p5
    assert sol.isPalindrome(p1) is True
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
