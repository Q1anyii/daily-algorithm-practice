"""
题目：238. 除自身以外数组的乘积 (productExceptSelf)
难度：中等
分类：数组/矩阵
"""
from itertools import accumulate
from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个整数数组 nums，返回数组 answer，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
题目数据保证数组 nums 之中任意元素的全部前缀元素和后缀的乘积都在 32 位整数范围内。
请不要使用除法，且在 O(n) 时间复杂度内完成此题。

示例 1：
输入: nums = [1,2,3,4]
输出: [24,12,8,6]
"""


# ==================== 解题思路 ====================
"""
动态计算求累积
ans[i] = 左边所有数的乘积 × 右边所有数的乘积
先用一个数组计算所有数字的前缀积
然后用一个suffix动态计算后缀积，每用过一次后再更新一次
ans[i] = prefix[i - 1] * suffix
"""

# ==================== 代码实现 ====================
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(prefix[i-1] * nums[i])
        res = [1] * len(nums)  # 预分配，按正序填，省得反转
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == 0:
                res[i] = suffix
                break
            res[i] = prefix[i - 1] * suffix  # i=0 时 prefix[i-1] 越界，单独处理为 1
            suffix *= nums[i]  # 用完再更新
        return res


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert sol.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert sol.productExceptSelf([1, 1]) == [1, 1]
    assert sol.productExceptSelf([2, 3]) == [3, 2]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
