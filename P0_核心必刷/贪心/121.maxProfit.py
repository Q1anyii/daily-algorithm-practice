"""
题目：121. 买卖股票的最佳时机 (maxProfit)
难度：简单
分类：贪心
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个数组 prices，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0。

示例 1：
输入：[7,1,5,3,6,4]
输出：5
"""


# ==================== 解题思路 ====================
"""

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if not prices: return profit
        lowest = prices[0]
        for p in prices:
            if p == lowest: continue
            profit = max(profit, p - lowest)
            if p < lowest:
                lowest = p
        return profit


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
    assert sol.maxProfit([1, 2]) == 1
    assert sol.maxProfit([2, 4, 1]) == 2
    assert sol.maxProfit([]) == 0
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
