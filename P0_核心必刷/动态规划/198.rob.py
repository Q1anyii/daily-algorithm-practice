"""
题目：198. 打家劫舍 (rob)
难度：中等
分类：动态规划
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你不触动警报装置的情况下，一夜之内能够偷窃到的最高金额。

示例 1：
输入：[1,2,3,1]
输出：4
"""


# ==================== 解题思路 ====================
"""
遍历每个元素，间隔为2？ 然后求sum？
最后max（sum）
动态规划：
动态计算到每家能够偷取的与前面可偷取的最大值
计算是当前这家 + 偷的上一家金额更大还是前面的一家金额更大
dp[i] = max(dp[i-1], dp[i-2] + nums[i])
"""

# ==================== 代码实现 ====================
class Solution:
    def rob(self, nums: List[int]) -> int:
        # cache = {}
        # def dfs(n):
        #     if n == 0 : return nums[n]
        #     if n == 1 : return max(nums[0], nums[1])
        #     if n in cache: return cache[n]
        #     cache[n] = max(dfs(n - 1), dfs(n - 2) + nums[n])
        #     return cache[n]
        # return dfs(len(nums) - 1)

        prev2, prev1 = 0, nums[0]
        for x in nums[1:]:
            prev2, prev1 = prev1, max(prev1, prev2 + x)
        return prev1

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.rob([1, 2, 3, 1]) == 4
    assert sol.rob([2, 7, 9, 3, 1]) == 12
    assert sol.rob([0]) == 0
    assert sol.rob([2, 1, 1, 2]) == 4
    assert sol.rob([1, 2]) == 2
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
