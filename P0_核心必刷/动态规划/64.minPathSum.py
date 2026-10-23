"""
题目：64. 最小路径和 (minPathSum)
难度：中等
分类：动态规划
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个包含非负整数的 m x n 网格 grid，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例 1：
输入：grid = [[1,3,1],
             [1,5,1],
             [4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
"""


# ==================== 解题思路 ====================
"""
这题和上一题算路径有点类似，不过问题变成了算每条路径的大小，而非路径的数量
那么需要维护一个min值，动态计算最小值？
然后再用上一题的解法
新问题：需要获取节点的大小然后相加
"""

# ==================== 代码实现 ====================
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0 : continue
                if i == 0: grid[i][j] += grid[i][j - 1]
                elif j == 0: grid[i][j] += grid[i - 1][j]
                else: grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]

        def dfs(i, j):
            if i < 0 or j < 0 : return float("inf")
            if i == 0 and j == 0 : return grid[0][0]
            return grid[i][j] + min(dfs(i - 1, j), dfs(i, j - 1))
        return dfs(len(grid) - 1, len(grid[0]) - 1)

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert sol.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12
    assert sol.minPathSum([[1]]) == 1
    assert sol.minPathSum([[1, 2], [1, 1]]) == 3
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
