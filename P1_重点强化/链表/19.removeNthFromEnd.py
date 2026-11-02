"""
题目：19. 删除链表的倒数第 N 个结点 (removeNthFromEnd)
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
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]
"""


# ==================== 解题思路 ====================
"""
解法一：逐个遍历获取数组，然后再删除，用数组再构建新节点，缺点空间复杂度O（L）

解法二：构建dummy节点，快慢指针，让快指针先走n步， 
      然后快慢指针一起走直到快指针到终点，slow.next = slow.next.next
"""

# ==================== 代码实现 ====================
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    # 1->2->3->4->5, 删除倒数第2个
    n1 = ListNode(1); n2 = ListNode(2); n3 = ListNode(3); n4 = ListNode(4); n5 = ListNode(5)
    n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n5
    result = sol.removeNthFromEnd(n1, 2)
    vals = []
    while result:
        vals.append(result.val)
        result = result.next
    assert vals == [1, 2, 3, 5]
    # 单节点删除
    s1 = ListNode(1)
    assert sol.removeNthFromEnd(s1, 1) is None
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
