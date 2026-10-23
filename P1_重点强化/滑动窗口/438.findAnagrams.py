"""
题目：438. 找到字符串中所有字母异位词 (findAnagrams)
难度：中等
分类：滑动窗口
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定两个字符串 s 和 p，找到 s 中所有 p 的异位词的子串，返回这些子串的起始索引。

示例 1：
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]

示例 2：
输入: s = "abab", p = "ab"
输出: [0,1,2]
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert sol.findAnagrams("abab", "ab") == [0, 1, 2]
    assert sol.findAnagrams("aaaa", "aa") == [0, 1, 2]
    assert sol.findAnagrams("abc", "abcd") == []
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
