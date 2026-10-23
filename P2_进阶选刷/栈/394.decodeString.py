"""
题目：394. 字符串解码 (decodeString)
难度：中等
分类：栈
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

示例 1：
输入：s = "3[a]2[bc]"
输出："aaabcbc"

示例 2：
输入：s = "3[a2[c]]"
输出："accaccacc"
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def decodeString(self, s: str) -> str:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.decodeString("3[a]2[bc]") == "aaabcbc"
    assert sol.decodeString("3[a2[c]]") == "accaccacc"
    assert sol.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert sol.decodeString("abc") == "abc"
    assert sol.decodeString("10[a]") == "a" * 10
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
