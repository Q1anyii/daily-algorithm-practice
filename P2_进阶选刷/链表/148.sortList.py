"""
题目：148. 排序链表 (sortList)
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
给你链表的头结点 head，请将其按升序排列并返回排序后的链表。

示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]

示例 2：
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    n1 = ListNode(4); n2 = ListNode(2); n3 = ListNode(1); n4 = ListNode(3)
    n1.next = n2; n2.next = n3; n3.next = n4
    result = sol.sortList(n1)
    vals = []
    while result:
        vals.append(result.val)
        result = result.next
    assert vals == [1, 2, 3, 4]
    # 负数
    m1 = ListNode(-1); m2 = ListNode(5); m3 = ListNode(3); m4 = ListNode(4); m5 = ListNode(0)
    m1.next = m2; m2.next = m3; m3.next = m4; m4.next = m5
    r = sol.sortList(m1)
    v = []
    while r:
        v.append(r.val)
        r = r.next
    assert v == [-1, 0, 3, 4, 5]
    assert sol.sortList(None) is None
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
