"""
题目：128. 最长连续序列 (longestConsecutive)
难度：中等
分类：哈希表
"""
from collections import defaultdict
from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个未排序的整数数组 nums，找出数字连续的最长序列的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4

示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
"""


# ==================== 解题思路 ====================
"""
凡是 "每个起点都要独立计数" 的循环，状态变量必须定义在循环内
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        dict_ = defaultdict(int)
        for n in nums: dict_[n] = 1
        longest = 0
        for n in nums:
            if n - 1 not in dict_:
                curr, length = n, 1
                while n + length in dict_:
                    curr += 1
                    length += 1
                longest = max(longest, length)
        return longest

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert sol.longestConsecutive([]) == 0
    assert sol.longestConsecutive([1]) == 1
    assert sol.longestConsecutive([1, 2, 0, 1]) == 3
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
