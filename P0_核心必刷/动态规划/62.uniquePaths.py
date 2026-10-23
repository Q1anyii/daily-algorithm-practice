"""
题目：62. 不同路径 (uniquePaths)
难度：中等
分类：动态规划
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
一个机器人位于一个 m x n 网格的左上角。机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角。
问总共有多少条不同的路径？

示例 1：
输入：m = 3, n = 7
输出：28

示例 2：
输入：m = 3, n = 2
输出：3
"""


# ==================== 解题思路 ====================
"""
动态规划，
计算最小的路径，然后每次网格变大都直接加上前面的路径再算最新路径？
1*1： 1
1*2： 1
2*2： 2
2*3： 3
其实每个网格最初都固定两个根路径，即向右、向下
但每次只能向右或向下？那其实可以动态更新，每到达下一步，计算下一步的下一步可选数量，然后累加？
就例如：2*3：
1，1 只有向下或向右，
向右：向右可以再向右或向下
向下：只能再向右
这样加起来就是3
但是向右-向下-向右，累加方案不可行
path(i, j) = path(i-1, j) + path(i, j-1)
"""

# ==================== 代码实现 ====================
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}  # 只创建一次
        def dfs(m, n):
            if m == 1 or n == 1: return 1
            if (m, n) in cache: return cache[(m, n)]
            cache[(m, n)] = dfs(m - 1, n) + dfs(m, n - 1)  # 算一次
            return cache[(m, n)]
        return dfs(m, n)

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.uniquePaths(3, 7) == 28
    assert sol.uniquePaths(3, 2) == 3
    assert sol.uniquePaths(1, 1) == 1
    assert sol.uniquePaths(2, 2) == 2
    assert sol.uniquePaths(3, 3) == 6
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
