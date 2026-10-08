"""
题目：22. 括号生成 (generateParenthesis)
难度：中等
分类：回溯
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
输入：n = 1
输出：["()"]
"""


# ==================== 解题思路 ====================
"""
维护left，用于（ 添加，right，用于 ） 添加
对left和right同时进行递归， 当right > left时，表示右括号添加完毕
对左括号进行递归，每次left + 1，用于添加左括号，直到left > n， 同时在加完后path取出
"""

# ==================== 代码实现 ====================
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n: return []
        res = []
        def backtrack(path, left, right):
            if left == n and right == n:
                res.append("".join(path))
                return
            if left < n:  # ② 能放左括号：选 → 递归 → 撤销
                path.append("(")
                backtrack(path, left + 1, right)
                path.pop()
            if right < left:  # ③ 能放右括号：选 → 递归 → 撤销
                path.append(")")
                backtrack(path, left, right + 1)
                path.pop()
        backtrack([], 0, 0)
        return res

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert sol.generateParenthesis(1) == ["()"]
    assert sol.generateParenthesis(2) == ["(())", "()()"]
    assert len(sol.generateParenthesis(4)) == 14
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
