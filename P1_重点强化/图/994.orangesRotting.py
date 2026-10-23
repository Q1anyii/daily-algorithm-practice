"""
题目：994. 腐烂的橘子 (orangesRotting)
难度：中等
分类：图
"""
from collections import deque
from typing import List, Optional, Dict, Tuple

from networkx.algorithms.traversal import dfs_successors

# ==================== 题目描述 ====================
"""
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
值 0 代表空单元格；值 1 代表新鲜橘子；值 2 代表腐烂的橘子。
每分钟，腐烂的橘子周围 4 个方向上相邻的新鲜橘子都会腐烂。
返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

示例 1：
输入：grid = [[2, 1, 1],
             [1, 1, 0],
             [0, 1, 1]]
输出：4
"""


# ==================== 解题思路 ====================
"""
只能一次一次扩散，
"""

# ==================== 代码实现 ====================
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        minutes = 0
        while queue and fresh > 0:  # 还有新鲜橘子才继续扩散
            size = len(queue)  # ① 本分钟要处理的橘子数（分层关键）
            for _ in range(size):
                i, j = queue.popleft()  # ② FIFO
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):  # ③ 方向数组
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        queue.append((ni, nj))  # ④ 元组入队
                        fresh -= 1  # ⑤ 感染了才减
            minutes += 1  # ⑥ 一层 = 一分钟

        return minutes if fresh == 0 else -1

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.orangesRotting([[2, 1, 1],
                               [1, 1, 0],
                               [0, 1, 1]]) == 4
    assert sol.orangesRotting([[2, 1, 1],
                               [0, 1, 1],
                               [1, 0, 1]]) == -1
    assert sol.orangesRotting([[0, 2]]) == 0
    assert sol.orangesRotting([[1]]) == -1
    assert sol.orangesRotting([[2]]) == 0
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
