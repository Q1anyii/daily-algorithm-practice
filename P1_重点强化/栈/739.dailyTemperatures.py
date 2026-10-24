"""
题目：739. 每日温度 (dailyTemperatures)
难度：中等
分类：栈
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个整数数组 temperatures，表示每天的温度，返回一个数组 answer，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

示例 1：
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
"""


# ==================== 解题思路 ====================
"""
1. **栈里存下标，不存温度值**—— 因为你需要算 "距离几天"。
2. 栈里的温度是**单调递减**的：如果后面某天比前面高，前面那天就被弹走了。
3. 遍历每一天 `i`：
   - 问自己：今天的温度 `temperatures[i]` 比栈顶那天高吗？
   - 高 → 栈顶那天找到了答案，弹出，答案就是 `i - 栈顶下标`。然后继续看新的栈顶，直到栈空或栈顶温度 >= 今天。
   - 不高 → 把今天压入栈，继续等后面的天。
"""

# ==================== 代码实现 ====================
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                p = stack.pop()
                ans[p] = i - p
            stack.append(i)
        return ans


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert sol.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert sol.dailyTemperatures([60, 50, 40, 30]) == [0, 0, 0, 0]
    assert sol.dailyTemperatures([30]) == [0]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
