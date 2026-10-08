"""
题目：46. 全排列 (permute)
难度：中等
分类：回溯
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个不含重复数字的数组 nums，返回其所有可能的全排列。你可以按任意顺序返回答案。

示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2：
输入：nums = [0,1]
输出：[[0,1],[1,0]]
"""


# ==================== 解题思路 ====================
"""
全排列，那么就是以每个数对新的非自身数进行排列， 然后实现最多组合

"""

# ==================== 代码实现 ====================
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        res = []
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(path)
                path.pop()
                used[i] =False
        backtrack([])
        return res


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert sol.permute([0, 1]) == [[0, 1], [1, 0]]
    assert sol.permute([1]) == [[1]]
    assert len(sol.permute([1, 2, 3, 4])) == 24
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
