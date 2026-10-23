"""
题目：647. 回文子串 (countSubstrings)
难度：中等
分类：字符串
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个字符串 s，请你统计并返回这个字符串中回文子串的数目。
回文字符串是正着读和倒过来读一样的字符串。
子字符串是字符串中的由连续字符组成的一个序列。

示例 1：
输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"

示例 2：
输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def countSubstrings(self, s: str) -> int:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.countSubstrings("abc") == 3
    assert sol.countSubstrings("aaa") == 6
    assert sol.countSubstrings("a") == 1
    assert sol.countSubstrings("ab") == 2
    assert sol.countSubstrings("aa") == 3
    assert sol.countSubstrings("fdsklf") == 6
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
