"""
题目：11. 盛最多水的容器 (maxArea)
难度：中等
分类：双指针
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个长度为 n 的整数数组 height。有 n 条垂线，找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。

示例 1：
输入：[1,8,6,2,5,4,8,3,7]
输出：49

示例 2：
输入：height = [1,1]
输出：1
"""


# ==================== 解题思路 ====================
"""
定义一个最大水量
定义左右指针，
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        if not height: return max_area
        left, right = 0, len(height) - 1
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert sol.maxArea([1, 1]) == 1
    assert sol.maxArea([4, 3, 2, 1, 4]) == 16
    assert sol.maxArea([1, 2, 1]) == 2
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
