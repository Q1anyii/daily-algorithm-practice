"""
题目：142. 环形链表 II (detectCycle)
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
给定一个链表的头节点 head，返回链表开始入环的第一个节点。如果链表无环，则返回 null。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    # 3->2->0->-4->(回到2), 入口为2
    n1 = ListNode(3); n2 = ListNode(2); n3 = ListNode(0); n4 = ListNode(-4)
    n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n2
    assert sol.detectCycle(n1) is n2
    # 无环
    m1 = ListNode(1); m2 = ListNode(2)
    m1.next = m2
    assert sol.detectCycle(m1) is None
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
