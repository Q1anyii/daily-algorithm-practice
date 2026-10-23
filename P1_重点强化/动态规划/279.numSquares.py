"""
题目：279. 完全平方数 (numSquares)
难度：中等
分类：动态规划
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个整数 n，返回和为 n 的完全平方数的最少数量。
完全平方数是一个整数，其值等于另一个整数的平方。

示例 1：
输入：n = 12
输出：3
解释：12 = 4 + 4 + 4

示例 2：
输入：n = 13
输出：2
解释：13 = 4 + 9
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def numSquares(self, n: int) -> int:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.numSquares(12) == 3
    assert sol.numSquares(13) == 2
    assert sol.numSquares(1) == 1
    assert sol.numSquares(2) == 2
    assert sol.numSquares(4) == 1
    assert sol.numSquares(9) == 1
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
