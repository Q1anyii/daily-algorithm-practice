"""
题目：62. 不同路径 (uniquePaths)
"""


# ==================== 题目描述 ====================
"""
一个机器人位于一个 m x n 网格的左上角。机器人每次只能向下或者向右移动一步。
问总共有多少条不同的路径到达网格的右下角。

示例 1：
输入：m = 3, n = 7
输出：28

示例 2：
输入：m = 3, n = 2
输出：3

示例 3：
输入：m = 1, n = 1
输出：1
"""


# ==================== 代码实现 ====================
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.uniquePaths(3, 7) == 28
    assert sol.uniquePaths(3, 2) == 3
    assert sol.uniquePaths(1, 1) == 1
    assert sol.uniquePaths(2, 2) == 2
    assert sol.uniquePaths(3, 3) == 6
    assert sol.uniquePaths(1, 10) == 1
    assert sol.uniquePaths(10, 1) == 1
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
