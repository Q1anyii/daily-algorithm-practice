"""
题目：15. 三数之和 (threeSum)
难度：中等
分类：双指针
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个整数数组 nums，返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：
输入：nums = [0,1,1]
输出：[]
"""


# ==================== 解题思路 ====================
"""
双指针，同时对nums遍历，
同时对left，right，i去重，防止结果添加重复列表
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) < 3: return []
        nums.sort()
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]: continue
            while left < right:
                sum_ = nums[left] + nums[i] + nums[right]
                if sum_ == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]: left += 1
                    while left < right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
                elif sum_ > 0:
                    right -= 1
                else:
                    left += 1
        return res


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert sol.threeSum([0, 1, 1]) == []
    assert sol.threeSum([0, 0, 0]) == [[0, 0, 0]]
    assert sol.threeSum([]) == []
    assert sol.threeSum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
