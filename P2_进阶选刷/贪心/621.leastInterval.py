"""
题目：621. 任务调度器 (leastInterval)
难度：中等
分类：贪心
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表，用字母 A 到 Z 表示，以及一个冷却时间 n。每个周期或时间间隔允许完成一项任务。任务可以按任何顺序完成，但有一个限制：两个相同种类的任务之间必须有长度为 n 的冷却时间。
返回完成所有任务所需要的最短时间间隔。

示例 1：
输入：tasks = ["A","A","A","B","B","B"], n = 2
输出：8
解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert sol.leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6
    assert sol.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2) == 16
    assert sol.leastInterval(["A", "B"], 2) == 2
    assert sol.leastInterval(["A"], 2) == 1
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
