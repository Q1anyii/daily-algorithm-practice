"""
题目：283. 移动零 (moveZeroes)
难度：简单
分类：双指针
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
必须在不复制数组的情况下原地对数组进行操作。

示例 1：
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

示例 2：
输入: nums = [0]
输出: [0]
"""


# ==================== 解题思路 ====================
"""
左右指针
左指针为0， 右指针为1，
然后判断左右指针再交换
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    nums1 = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums1)
    assert nums1 == [1, 3, 12, 0, 0]
    nums2 = [0]
    sol.moveZeroes(nums2)
    assert nums2 == [0]
    nums3 = [1, 2, 3]
    sol.moveZeroes(nums3)
    assert nums3 == [1, 2, 3]
    nums4 = [0, 0, 1]
    sol.moveZeroes(nums4)
    assert nums4 == [1, 0, 0]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
