"""
题目：141. 环形链表 (hasCycle)
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
给你一个链表的头节点 head，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：true
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    # 有环: 3->2->0->-4->(回到2)
    n1 = ListNode(3); n2 = ListNode(2); n3 = ListNode(0); n4 = ListNode(-4)
    n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n2
    assert sol.hasCycle(n1) is True
    # 无环
    m1 = ListNode(1); m2 = ListNode(2)
    m1.next = m2
    assert sol.hasCycle(m1) is False
    assert sol.hasCycle(None) is False
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
