"""
题目：39. 组合总和 (combinationSum)
难度：中等
分类：回溯
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个无重复元素的整数数组 candidates 和一个目标整数 target，找出 candidates 中可以使数字和为目标数 target 的所有不同组合，并以列表形式返回。你可以按任意顺序返回这些组合。
candidates 中的同一个数字可以无限制重复被选取。

示例 1：
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
"""


# ==================== 解题思路 ====================
"""
用target每次减去当前的数字作为下一个递归的target，然后判断remaining是否为0，如果为0那么就说明数组中可以组成
然后再每次对新的start进行遍历，这样其实就等于一直在找能够组成target的数组，
直到candidates[i]>remaining,这就说明数组中没有可以组成target的数了

"""

# ==================== 代码实现 ====================
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start, path, remaining):
            # 判断remaining是否为0， 如果为0，那么就说明path可以满足条件，则存入res
            if remaining == 0:
                res.append(path[:])
            for i in range(start, len(candidates)):
                # 判断candidates[i] > remaining: True: no another item could in condition
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])
                path.pop() # 这一步是关键，用于剔除已满足的元素，然后计算新元素的组合

        backtrack(0, [], target)
        return res


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert sol.combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert sol.combinationSum([2], 1) == []
    assert sol.combinationSum([1], 1) == [[1]]
    assert sol.combinationSum([1], 2) == [[1, 1]]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
