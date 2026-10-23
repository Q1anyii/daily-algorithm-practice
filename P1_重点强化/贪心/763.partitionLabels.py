"""
题目：763. 划分字母区间 (partitionLabels)
难度：中等
分类：贪心
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个字符串 s。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
返回一个表示每个字符串片段的长度的列表。

示例 1：
输入：s = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。每个字母最多出现在一个片段中。
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert sol.partitionLabels("eccbbbbdec") == [10]
    assert sol.partitionLabels("a") == [1]
    assert sol.partitionLabels("ab") == [1, 1]
    assert sol.partitionLabels("aa") == [2]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
