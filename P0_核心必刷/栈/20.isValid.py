"""
题目：20. 有效的括号 (isValid)
难度：简单
分类：栈
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s，判断字符串是否有效。
有效字符串需满足：
1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。
3. 每个右括号都有一个对应的相同类型的左括号。

示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def isValid(self, s: str) -> bool:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.isValid("()") is True
    assert sol.isValid("()[]{}") is True
    assert sol.isValid("(]") is False
    assert sol.isValid("([)]") is False
    assert sol.isValid("{[]}") is True
    assert sol.isValid("") is True
    assert sol.isValid("(") is False
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
