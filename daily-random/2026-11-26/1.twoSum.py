"""
题目：1. 两数之和 (twoSum)
"""

from typing import List


# ==================== 题目描述 ====================
"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出
和为目标值 target 的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]
"""


# ==================== 代码实现 ====================
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target - nums[i]], i]
            seen[nums[i]] = i
        return []

# ==================== 测试用例 ====================
def check(nums, target, expect):
    """按下标集合比较，允许任意返回顺序"""
    got = Solution().twoSum(nums, target)
    assert got is not None, f'twoSum({nums}, {target}) 返回 None'
    assert sorted(got) == sorted(expect), f'twoSum({nums}, {target}) = {got}, 期望 {expect}'
    assert len(set(got)) == 2, f'twoSum({nums}, {target}) = {got}, 两个下标必须不同'


def test_solution():
    # 示例
    check([2, 7, 11, 15], 9, [0, 1])
    check([3, 2, 4], 6, [1, 2])
    check([3, 3], 6, [0, 1])

    # 负数
    check([-1, -2, -3, -4, -5], -8, [2, 4])
    check([-3, 4, 3, 90], 0, [0, 2])

    # 答案出现在数组尾部
    check([1, 2, 3, 4, 5, 6], 11, [4, 5])

    # 0 参与
    check([0, 4, 3, 0], 0, [0, 3])

    # 两个元素的最小规模
    check([1, 2], 3, [0, 1])

    # 大数
    check([1000000, 500000, 2000000], 3000000, [0, 2])

    # 相同值不能复用一个下标
    check([2, 5, 5, 11], 10, [1, 2])

    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
