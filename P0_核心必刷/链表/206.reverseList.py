"""
题目：206. 反转链表 (reverseList)
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
给你单链表的头节点 head，请你反转链表，并返回反转后的链表。

示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    # 1->2->3->4->5
    n1 = ListNode(1); n2 = ListNode(2); n3 = ListNode(3); n4 = ListNode(4); n5 = ListNode(5)
    n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n5
    result = sol.reverseList(n1)
    vals = []
    while result:
        vals.append(result.val)
        result = result.next
    assert vals == [5, 4, 3, 2, 1]
    assert sol.reverseList(None) is None
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
