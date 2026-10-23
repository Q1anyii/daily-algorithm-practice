"""
题目：416. 分割等和子集 (canPartition)
难度：中等
分类：动态规划
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个只包含正整数的非空数组 nums。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11]。

示例 2：
输入：nums = [1,2,3,5]
输出：false
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.canPartition([1, 5, 11, 5]) is True
    assert sol.canPartition([1, 2, 3, 5]) is False
    assert sol.canPartition([1, 1]) is True
    assert sol.canPartition([1, 2, 5]) is False
    assert sol.canPartition([2, 2, 1, 1]) is True
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
