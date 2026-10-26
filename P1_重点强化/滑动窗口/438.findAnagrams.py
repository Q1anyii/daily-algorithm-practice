"""
题目：438. 找到字符串中所有字母异位词 (findAnagrams)
难度：中等
分类：滑动窗口
"""

from typing import List, Optional, Dict, Tuple, Counter

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
"""
1. 先数出 p 的计数表（固定参考）
2. 窗口每右移一格：左边字符计数 -1，右边新字符计数 +1
3. 每次移动后比较：窗口计数表 == p 计数表？相等就记下窗口起点
"""

# ==================== 代码实现 ====================
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = Counter(p)
        ans = []

        left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1  # 右端点字母进入窗口
            while cnt[c] < 0:  # 字母 c 太多了
                cnt[s[left]] += 1  # 左端点字母离开窗口
                left += 1
            if right - left + 1 == len(p):  # t 和 p 的每种字母的出现次数都相同（证明见上）
                ans.append(left)  # t 左端点下标加入答案

        return ans


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
