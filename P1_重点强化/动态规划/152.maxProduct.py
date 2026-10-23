"""
题目：152. 乘积最大子数组 (maxProduct)
难度：中等
分类：动态规划
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个整数数组 nums，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1：
输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2：
输入: nums = [-2,0,-1]
输出: 0
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.maxProduct([2, 3, -2, 4]) == 6
    assert sol.maxProduct([-2, 0, -1]) == 0
    assert sol.maxProduct([-2, 3, -4]) == 24
    assert sol.maxProduct([0, 2]) == 2
    assert sol.maxProduct([-2]) == -2
    assert sol.maxProduct([2, -5, -2, -4, 3]) == 24
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
