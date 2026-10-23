"""
题目：5. 最长回文子串 (longestPalindrome)
难度：中等
分类：字符串
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # TODO: 实现该方法
        pass
        def expand(left, right):
            # TODO: 实现该方法
            pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.longestPalindrome("babad") in ["bab", "aba"]
    assert sol.longestPalindrome("cbbd") == "bb"
    assert sol.longestPalindrome("a") == "a"
    assert sol.longestPalindrome("ac") in ["a", "c"]
    assert sol.longestPalindrome("bb") == "bb"
    assert sol.longestPalindrome("abcba") == "abcba"
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
