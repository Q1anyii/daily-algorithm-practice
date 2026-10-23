"""
题目：74. 搜索二维矩阵 (searchMatrix)
难度：中等
分类：二分查找
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个满足下述两条属性的 m x n 整数矩阵：
每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target，如果 target 在矩阵中，返回 true；否则，返回 false。
复杂度必须：O(log(m * n))
示例 1：
输入：matrix = [ [1,3,5,7],
                [10,11,16,20],
                [23,30,34,60]], target = 3
输出：true
"""


# ==================== 解题思路 ====================
"""
TODO: 该题已在原仓库 git 提交过（已刷），此版本已移除原思路与代码，请独立重做后自行总结。
将矩阵视为一个一维数组，然后进行二分
left = 0, right = len(martix) * len(martix[0]) - 1
mid = (left + right) // 2

middle = martix[mid // col][middle % col]

while left == right :
 return matrix[mid // col][middle % col]
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        col = len(matrix[0])
        row = len(matrix)
        left = 0
        right = col * row - 1
        while left < right:
            mid = (left + right) // 2
            middle = matrix[mid // col][mid % col]
            if middle == target:
                return True
            elif middle < target:
                left = mid + 1
            else:
                right = mid
        return matrix[left // col][left % col] == target






# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert sol.searchMatrix(matrix, 3) is True
    assert sol.searchMatrix(matrix, 13) is False
    assert sol.searchMatrix(matrix, 1) is True
    assert sol.searchMatrix(matrix, 60) is True
    assert sol.searchMatrix(matrix, 0) is False
    assert sol.searchMatrix([], 1) is False
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
