"""
题目：200. 岛屿数量 (numIslands)
难度：中等
分类：图
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

示例 1：
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
"""


# ==================== 解题思路 ====================
"""
岛屿即四面环水，如果在网格边界，但2-3面环水也记为岛屿
需要动态扩展？
判断上下左右是否为0，是则记为岛屿，否则只要有一个为1，然后继续判断那个1的另外几面是否为0，以此类推，那么就需要使用递归？
双层遍历，将1附近的1标记为0，避免重复访问。
"""

# ==================== 代码实现 ====================
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
        # 提示：边界和字符不匹配用同一个 if 合并判断
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return  # 越界或非陆地 → 直接返回
            grid[i][j] = "0"  # 沉岛：标记已访问
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1  # 发现新岛屿起点
                    dfs(i, j)  # 淹没整片
        return count
# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    grid1 = [["1","1","1","1","0"],
             ["1","1","0","1","0"],
             ["1","1","0","0","0"],
             ["0","0","0","0","0"]]
    assert sol.numIslands(grid1) == 1
    grid2 = [["1","1","0","0","0"],
             ["1","1","0","0","0"],
             ["0","0","1","0","0"],
             ["0","0","0","1","1"]]
    assert sol.numIslands(grid2) == 3
    assert sol.numIslands([["0"]]) == 0
    assert sol.numIslands([["1"]]) == 1
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
