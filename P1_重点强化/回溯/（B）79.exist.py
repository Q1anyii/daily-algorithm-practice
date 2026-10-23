"""
题目：79. 单词搜索 (exist)
难度：中等
分类：回溯
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word。如果 word 存在于网格中，返回 true；否则，返回 false。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中"相邻"单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
"""


# ==================== 解题思路 ====================
"""
设置两个指针？i， j
i++先对board查找是否存在word的第一个元素，如果存在,j++,
然后一直这样持续下去直到i == board.len * board[0].len
如果结果j ！= word.len 那么就返回false
"""

# ==================== 代码实现 ====================
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, index):
            if index == len(word):  # ① 成功终止：词全部匹配完
                return True
            if i < 0 or i >= m or j < 0 or j >= n:  # ② 越界 → 失败
                return False
            if board[i][j] != word[index]:  # ③ 字符不匹配 → 失败
                return False

            # ④ 匹配上了：标记已用 → 四方向递归 → 撤销标记
            temp = board[i][j]
            board[i][j] = ""
            found = (dfs(i + 1, j, index + 1) or
                     dfs(i - 1, j, index + 1) or
                     dfs(i, j + 1, index + 1) or
                     dfs(i, j - 1, index + 1))
            board[i][j] = temp
            return found

        for i in range(m):  # ⑤ 任意格子都能当起点
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert sol.exist(board, "ABCCED") is True
    assert sol.exist(board, "SEE") is True
    assert sol.exist(board, "ABCB") is False
    assert sol.exist([["a"]], "a") is True
    assert sol.exist([["a"]], "b") is False
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
