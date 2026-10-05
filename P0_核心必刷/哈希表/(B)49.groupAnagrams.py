"""
题目：49. 字母异位词分组 (groupAnagrams)
难度：中等
分类：哈希表
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个字符串数组，请你将字母异位词组合在一起。可以按任意顺序返回结果列表。
字母异位词是由重新排列源单词的所有字母得到的一个新单词。

示例 1：
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

示例 2：
输入: strs = [""]
输出: [[""]]
"""


# ==================== 解题思路 ====================
"""
维护一个dict， 以字母排序后的词作为key， value为存在相同字母的词
然后返回
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # from collections import defaultdict
        # dict_ = defaultdict(list)
        # for s in strs:
        #     dict_[tuple(sorted(s))].append(s)
        # return list(dict_.values())

        from collections import defaultdict
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:  # O(k) 数频次
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(s)  # 元组可哈希
        return list(groups.values())


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    result = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    result_sorted = sorted([sorted(group) for group in result])
    expected = sorted([sorted(group) for group in [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]])
    assert result_sorted == expected
    assert sol.groupAnagrams([""]) == [[""]]
    assert sol.groupAnagrams(["a"]) == [["a"]]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
