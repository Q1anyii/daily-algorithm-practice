"""
题目：64. 最小路径和 (minPathSum)
"""

from typing import List


# ==================== 题目描述 ====================
"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，
使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例 1：
输入：grid = [[1,3,1],
             [1,5,1],
             [4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。

示例 2：
输入：grid = [[1,2,3],
             [4,5,6]]
输出：12

示例 3：
输入：grid = [[1]]
输出：1

提示：
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
"""


# ==================== 代码实现 ====================
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 动态规划，每到一个点计算当前点左侧或上侧的最小
        # m, n = len(grid), len(grid[0])
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0: continue
        #         elif i == 0: grid[i][j] += grid[i][j - 1]
        #         elif j == 0: grid[i][j] += grid[i - 1][j]
        #         else: grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        # return grid[m - 1][n - 1]

        m, n = len(grid), len(grid[0])
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = grid[i][j]
                elif i == 0:
                    dp[j] = dp[j - 1] + grid[i][j]
                elif j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[-1]


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()

    # 示例
    assert sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert sol.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12
    assert sol.minPathSum([[1]]) == 1

    # 边界：单行 / 单列，只有一条路径可走
    assert sol.minPathSum([[1, 2, 3, 4]]) == 10
    assert sol.minPathSum([[1], [2], [3]]) == 6

    # 两行两列，走下再右比先右再下更省
    assert sol.minPathSum([[1, 2], [1, 1]]) == 3

    # 全零网格
    assert sol.minPathSum([[0, 0], [0, 0]]) == 0

    # 需要绕开大数
    assert sol.minPathSum([[1, 9, 1], [9, 9, 1], [1, 1, 1]]) == 13

    # 大值累加，验证没有溢出或提前截断
    assert sol.minPathSum([[200, 200], [200, 200]]) == 600

    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
