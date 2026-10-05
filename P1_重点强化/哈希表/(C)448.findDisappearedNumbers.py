"""
题目：448. 找到所有数组中消失的数字 (findDisappearedNumbers)
难度：简单
分类：哈希表
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个含 n 个整数的数组 nums，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。

示例 1：
输入：nums = [4,3,2,7,8,2,3,1]
输出：[5,6]

示例 2：
输入：nums = [1,1]
输出：[2]
"""


# ==================== 解题思路 ====================
"""
数组自身当哈希表 + 符号位编码
"""

class Solution:
    def findDisappearedNumbers (self, nums: List [int]) -> List [int]:
        for i in range(len(nums)):
            v = abs(nums[i])
            idx = v - 1
            if nums[idx] > 0: nums[idx] = - nums[idx]
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

        # res = []
        # set_ = set (nums)
        # for i in range (1, len (nums) + 1):
        #     if i not in set_:
        #         res.append (i)
        # return res

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert sol.findDisappearedNumbers([1, 1]) == [2]
    assert sol.findDisappearedNumbers([1, 2, 3]) == []
    assert sol.findDisappearedNumbers([2, 2]) == [1]
    assert sol.findDisappearedNumbers([1]) == []
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
