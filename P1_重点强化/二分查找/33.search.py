"""
题目：33. 搜索旋转排序数组 (search)
难度：中等
分类：二分查找
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
整数数组 nums 按升序排列，数组中的值互不相同。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]。
给你旋转后的数组 nums 和一个整数 target，如果 nums 中存在这个目标值 target，则返回它的下标，否则返回 -1。

示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
"""


# ==================== 解题思路 ====================
"""
二分查找：
if mid > left: sequential
else : 
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return left if nums[left] == target else -1



# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert sol.search([1], 0) == -1
    assert sol.search([1], 1) == 0
    assert sol.search([5, 1, 3], 3) == 2
    assert sol.search([5, 1, 3], 5) == 0
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
