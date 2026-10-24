"""
题目：155. 最小栈 (MinStack)
难度：中等
分类：栈
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
实现 MinStack 类:
- MinStack() 初始化堆栈对象。
- void push(int val) 将元素 val 推入堆栈。
- void pop() 删除堆栈顶部的元素。
- int top() 获取堆栈顶部的元素。
- int getMin() 获取堆栈中的最小元素。

示例 1：
输入：["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
输出：[null,null,null,null,-3,null,0,-2]
"""


# ==================== 解题思路 ====================
"""
"""

# ==================== 代码实现 ====================
class MinStack:

    def __init__(self):
        self.stack = []
        self.astack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.astack or self.astack[-1] >= value:
            self.astack.append(value)

    def pop(self) -> None:
        pop = self.stack.pop()
        if pop == self.astack[-1]:
            self.astack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.astack[-1]


# ==================== 测试用例 ====================
def test_solution():
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.getMin() == -3
    min_stack.pop()
    assert min_stack.top() == 0
    assert min_stack.getMin() == -2
    # 额外测试
    ms2 = MinStack()
    ms2.push(5)
    ms2.push(3)
    ms2.push(4)
    assert ms2.getMin() == 3
    ms2.pop()
    assert ms2.getMin() == 3
    ms2.pop()
    assert ms2.getMin() == 5
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
