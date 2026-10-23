"""
题目：221. 最大正方形 (maximalSquare)
难度：中等
分类：动态规划
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

示例 1：
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    assert sol.maximalSquare(matrix) == 4
    assert sol.maximalSquare([["0"]]) == 0
    assert sol.maximalSquare([["1"]]) == 1
    assert sol.maximalSquare([["1","1"],["1","1"]]) == 4
    assert sol.maximalSquare([["1","0"],["0","1"]]) == 1
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
