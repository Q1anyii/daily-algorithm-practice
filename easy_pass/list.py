class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #反转链表，本质是将当前节点的下一个节点指向前一个节点
    def reverse_list(self, head: Node):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            curr, prev = nxt, curr
        return prev

    # 找中间节点（快慢指针：fast 走 2 步，slow 走 1 步）
    def middle_node(self, head: Node):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

if __name__ == "__main__":
    n1 = Node(2)

