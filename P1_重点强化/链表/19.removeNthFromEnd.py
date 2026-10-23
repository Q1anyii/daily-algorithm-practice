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
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # TODO: 实现该方法
        pass


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
