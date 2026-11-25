"""
题目：141. 环形链表 (hasCycle)
"""

from typing import Optional


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

示例 2：
输入：head = [1,2], pos = 0
输出：true

示例 3：
输入：head = [1], pos = -1
输出：false
"""


# ==================== 代码实现 ====================
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        fast = slow = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False

# ==================== 测试用例 ====================
def build_list_with_cycle(values, pos):
    """建链，pos=-1 表示无环，否则尾节点指向下标 pos"""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]
    return nodes[0]


def test_solution():
    sol = Solution()
    assert sol.hasCycle(build_list_with_cycle([3, 2, 0, -4], 1)) is True
    assert sol.hasCycle(build_list_with_cycle([1, 2], 0)) is True
    assert sol.hasCycle(build_list_with_cycle([1], -1)) is False
    assert sol.hasCycle(build_list_with_cycle([1], 0)) is True
    assert sol.hasCycle(None) is False
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
