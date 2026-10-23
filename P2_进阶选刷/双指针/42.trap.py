"""
题目：42. 接雨水 (trap)
难度：困难
分类：双指针
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算下雨之后能接多少雨水。

示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6

示例 2：
输入：height = [4,2,0,3,2,5]
输出：9
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def trap(self, height: List[int]) -> int:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert sol.trap([4, 2, 0, 3, 2, 5]) == 9
    assert sol.trap([]) == 0
    assert sol.trap([1, 2, 3]) == 0
    assert sol.trap([3, 0, 3]) == 3
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
