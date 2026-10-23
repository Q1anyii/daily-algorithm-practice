"""
题目：17. 电话号码的字母组合 (letterCombinations)
难度：中等
分类：回溯
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按任意顺序返回。
给出数字到字母的映射如下（与电话按键相同）。
数字	字母
2	abc
3	def
4	ghi
5	jkl
6	mno
7	pqrs
8	tuv
9	wxyz

示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

示例 2：
输入：digits = ""
输出：[]
"""


# ==================== 解题思路 ====================
"""
映射，那就是对第一个元素上的所有数映射到第二个元素上的所有数字

"""

# ==================== 代码实现 ====================
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                 "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if not digits:
            return []
        res = []

        def backstack(index, path):
            if index == len(digits):
                res.append("".join(path))
                return
            for ch in phone[digits[index]]:
                path.append(ch)
                backstack(index + 1, path)
                path.pop()

        backstack(0, [])
        return res

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert sol.letterCombinations("") == []
    assert sol.letterCombinations("2") == ["a", "b", "c"]
    assert len(sol.letterCombinations("234")) == 27
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
