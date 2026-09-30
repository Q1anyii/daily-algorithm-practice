"""
题目：136. 只出现一次的数字 (singleNumber)
难度：简单
分类：位运算
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个非空整数数组 nums，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

示例 1：
输入：nums = [2,2,1]
输出：1

示例 2：
输入：nums = [4,1,2,1,2]
输出：4
"""


# ==================== 解题思路 ====================
"""
异或运算，
异或规则：同0异1
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k = 0
        for n in nums:
            k ^= n
        return k

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.singleNumber([2, 2, 1]) == 1
    assert sol.singleNumber([4, 1, 2, 1, 2]) == 4
    assert sol.singleNumber([1]) == 1
    assert sol.singleNumber([-1, -1, -2]) == -2
    assert sol.singleNumber([0, 1, 0]) == 1
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
