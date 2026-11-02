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
回文链表，使用栈？(空间复杂度O（n）)

联合两种算法（找中间节点 & 反转链表）， 将中间节点后的链表进行反转然后逐个对比值
"""

# ==================== 代码实现 ====================
class Solution:
    def middleNode(self, head: Optional[ListNode]):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverseList(self, head: Optional[ListNode]):
        cur, prev = head, None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.middleNode(head)
        h2 = self.reverseList(mid)
        while h2:
            if head.val != h2.val:
                return False
            head = head.next
            h2 = h2.next
        return True

        # stack = []
        # cur = head
        # while cur:
        #     stack.append(cur.val)
        #     cur = cur.next
        # cur = head
        # while cur:
        #     if cur.val != stack.pop():
        #         return False
        #     cur = cur.next
        # return True


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
