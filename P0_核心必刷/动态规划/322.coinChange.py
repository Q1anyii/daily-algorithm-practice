"""
题目：322. 零钱兑换 (coinChange)
难度：中等
分类：动态规划
"""

from typing import List, Optional, Dict, Tuple

from sklearn.externals.array_api_compat.torch import maximum

# ==================== 题目描述 ====================
"""
给你一个整数数组 coins，表示不同面额的硬币；以及一个整数 amount，表示总金额。
计算并返回可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
你可以认为每种硬币的数量是无限的。

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
"""


# ==================== 解题思路 ====================
"""
先对数组最大值取余数？然后再从余数中继续对剩下的最大值取余数？ 然后由余数拼接(证伪，贪心不成立)

先初始化amount长度的dp， 然后动态计算每个amount可由硬币拼接的数量，
如果这个dp[amount]不更新，那么就说明没有任何一种硬币组合能组成总金额，返回 -1。
"""

# ==================== 代码实现 ====================
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 : return 0
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.coinChange([1, 2, 5], 11) == 3
    assert sol.coinChange([2], 3) == -1
    assert sol.coinChange([1], 0) == 0
    assert sol.coinChange([1], 1) == 1
    assert sol.coinChange([1, 2, 5], 100) == 20
    assert sol.coinChange([186, 419, 83, 408], 6249) == 20
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
