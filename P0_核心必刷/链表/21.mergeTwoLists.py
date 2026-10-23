"""
题目：21. 合并两个有序链表 (mergeTwoLists)
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
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    # l1: 1->2->4, l2: 1->3->4
    a1 = ListNode(1); a2 = ListNode(2); a3 = ListNode(4)
    a1.next = a2; a2.next = a3
    b1 = ListNode(1); b2 = ListNode(3); b3 = ListNode(4)
    b1.next = b2; b2.next = b3
    result = sol.mergeTwoLists(a1, b1)
    vals = []
    while result:
        vals.append(result.val)
        result = result.next
    assert vals == [1, 1, 2, 3, 4, 4]
    assert sol.mergeTwoLists(None, None) is None
    c1 = ListNode(0)
    r = sol.mergeTwoLists(None, c1)
    assert r.val == 0
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
