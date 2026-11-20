"""
题目：128. 最长连续序列 (longestConsecutive)
难度：中等
分类：哈希表
"""
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
        nums_set = set(nums)
        max_len = 0

        for n in nums_set:
            if n - 1 not in nums_set:
                cur_num, cur_len = n, 1
                while cur_num + 1 in nums_set:
                    cur_len += 1
                    cur_num += 1
                max_len = max(max_len, cur_len)

        return max_len


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
