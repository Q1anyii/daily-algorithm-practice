"""
题目：131. 分割回文串 (partition)
难度：中等
分类：回溯
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文串。返回 s 所有可能的分割方案。

示例 1：
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]

示例 2：
输入：s = "a"
输出：[["a"]]
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # TODO: 实现该方法
        pass
        def is_palindrome(sub):
            # TODO: 实现该方法
            pass
        def backtrack(start, path):
            # TODO: 实现该方法
            pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.partition("aab") == [["a", "a", "b"], ["aa", "b"]]
    assert sol.partition("a") == [["a"]]
    assert sol.partition("aa") == [["a", "a"], ["aa"]]
    assert sol.partition("ab") == [["a", "b"]]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
