"""
题目：494. 目标和 (findTargetSumWays)
难度：中等
分类：动态规划
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个非负整数数组 nums 和一个整数 target。
向数组中的每个整数前添加 '+' 或 '-'，然后串联起所有整数，可以构造一个表达式：
例如，nums = [2, 1]，可以在 2 之前添加 '+'，在 1 之前添加 '-'，然后串联起来得到表达式 "+2-1"。
返回可以通过上述方法构造的、运算结果等于 target 的不同表达式的数目。

示例 1：
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3。
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
    assert sol.findTargetSumWays([1], 1) == 1
    assert sol.findTargetSumWays([1], 2) == 0
    assert sol.findTargetSumWays([0, 0, 0, 0, 0, 0, 0, 0, 1], 1) == 256
    assert sol.findTargetSumWays([1000], -1000) == 1
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
