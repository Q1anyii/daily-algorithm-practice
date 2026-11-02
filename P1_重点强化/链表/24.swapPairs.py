"""
题目：24. 两两交换链表中的节点 (swapPairs)
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
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题。

示例 1：
输入：head = [1,2,3,4]
输出：[2,1,4,3]

示例 2：
输入：head = []
输出：[]
"""


# ==================== 解题思路 ====================
"""
递归写法，当head或head.next不存在，直接返回head
然后temp = head.next 存储head.next,防止交换顺序错乱
head.next = self.swapPairs(temp.next)，这一步是为了后续交换
temp.next = head 最后把head.next.next切换成head
return temp

迭代写法：把curr.next(a) curr.next.next(b)存起来
然后当前节点的下一个节点指向当前节点的下一个节点的下一个节点(b):  
再把当前节点的下一个节点(a)的下一个节点指向a的下一个节点的下一个节点(b.next), 
最后再把b的下一个节点(b.next)指向a，完成交换 
另外还需要再把a赋值给curr，进行后续节点交换

"""

# ==================== 代码实现 ====================
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 递归终止条件：没有节点 / 只剩1个节点，不用交换
        # if not head or not head.next:
        #     return head
        # temp = head.next  # temp 是 head 的下一个节点（要换到前面的那个）
        # head.next = self.swapPairs(temp.next)  # 后面剩下的链表先递归交换好，再接在head后面
        # temp.next = head  # 把head接到temp的后面，完成这一组交换
        # return temp  # temp变成这一组的新头，返回给上层

        dummy = ListNode(0, head)
        curr = dummy
        while curr.next and curr.next.next:
            n1 = curr.next
            n2 = curr.next.next
            curr.next = n2
            n1.next = n2.next
            n2.next = n1
            curr = n1
        return dummy.next

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    n1 = ListNode(1); n2 = ListNode(2); n3 = ListNode(3); n4 = ListNode(4)
    n1.next = n2; n2.next = n3; n3.next = n4
    result = sol.swapPairs(n1)
    vals = []
    while result:
        vals.append(result.val)
        result = result.next
    assert vals == [2, 1, 4, 3]
    assert sol.swapPairs(None) is None
    s1 = ListNode(1)
    r = sol.swapPairs(s1)
    assert r.val == 1 and r.next is None
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
