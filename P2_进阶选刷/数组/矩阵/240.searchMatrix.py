"""
题目：240. 搜索二维矩阵 II (searchMatrix)
难度：中等
分类：数组/矩阵
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

示例 1：
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    assert sol.searchMatrix(matrix, 5) is True
    assert sol.searchMatrix(matrix, 20) is False
    assert sol.searchMatrix(matrix, 1) is True
    assert sol.searchMatrix(matrix, 30) is True
    assert sol.searchMatrix(matrix, 0) is False
    assert sol.searchMatrix([], 1) is False
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
