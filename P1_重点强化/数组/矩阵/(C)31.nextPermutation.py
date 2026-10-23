"""
题目：31. 下一个排列 (nextPermutation)
难度：中等
分类：数组/矩阵
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
整数数组的一个排列就是将其所有成员以序列或线性顺序排列。
下一个排列是指其按字典序排列的下一个更大的排列。如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须原地修改，只允许使用额外常数空间。

示例 1：
输入：nums = [1,2,3]
输出：[1,3,2]

示例 2：
输入：nums = [3,2,1]
输出：[1,2,3]
"""


# ==================== 解题思路 ====================
"""
第一步：从右往左找第一个nums[i] < nums[i + 1]的正序数字
第二步：找到第一个比nums[j]大的数字j，并交换i，j
第三步：左右指针，然后反转
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    nums1 = [1, 2, 3]
    sol.nextPermutation(nums1)
    assert nums1 == [1, 3, 2]
    nums2 = [3, 2, 1]
    sol.nextPermutation(nums2)
    assert nums2 == [1, 2, 3]
    nums3 = [1, 1, 5]
    sol.nextPermutation(nums3)
    assert nums3 == [1, 5, 1]
    nums4 = [1]
    sol.nextPermutation(nums4)
    assert nums4 == [1]
    nums5 = [1, 3, 2]
    sol.nextPermutation(nums5)
    assert nums5 == [2, 1, 3]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
