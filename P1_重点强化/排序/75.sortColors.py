"""
题目：75. 颜色分类 (sortColors)
难度：中等
分类：排序
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。
必须在不使用库内置的 sort 函数的情况下解决这个问题。

示例 1：
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

示例 2：
输入：nums = [2,0,1]
输出：[0,1,2]
"""


# ==================== 解题思路 ====================
"""
三指针
"""

# ==================== 代码实现 ====================
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        p0, p2 = 0, len(nums) - 1
        i = 0
        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            elif nums[i] == 1:
                i += 1

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    nums1 = [2, 0, 2, 1, 1, 0]
    sol.sortColors(nums1)
    assert nums1 == [0, 0, 1, 1, 2, 2]
    nums2 = [2, 0, 1]
    sol.sortColors(nums2)
    assert nums2 == [0, 1, 2]
    nums3 = [0]
    sol.sortColors(nums3)
    assert nums3 == [0]
    nums4 = [1, 2, 0]
    sol.sortColors(nums4)
    assert nums4 == [0, 1, 2]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
