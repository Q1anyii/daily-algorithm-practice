"""
题目：300. 最长递增子序列 (lengthOfLIS)
难度：中等
分类：动态规划
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个整数数组 nums，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。

示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4。
"""


# ==================== 解题思路 ====================
"""
最长递增序列，那么就需要动态计算每一组的递增长度，

对每个循环记最大值？ 
"""

# ==================== 代码实现 ====================
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums : return 0
        n = len(nums)
        dp = [1] * n  # 每个位置单独一个元素，长度至少 1
        for i in range(n):  # 外层：以 i 结尾
            for j in range(i):  # 内层：扫前面所有位置
                if nums[j] < nums[i]:  # 只有更小的才能接在链尾
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert sol.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert sol.lengthOfLIS([7, 7, 7, 7, 7]) == 1
    assert sol.lengthOfLIS([1]) == 1
    assert sol.lengthOfLIS([]) == 0
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
