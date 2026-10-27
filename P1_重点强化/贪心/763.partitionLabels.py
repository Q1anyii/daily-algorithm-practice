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
"""
1， 首先看第一个字母，找到它在串里最后的一个位置，记作last或一段的最后位置。
2， 在从0~last这个范围里，挨个查其他字母，看他们的最后位置是不是比刚才的last或一段的最后位置大。
如果没有刚才的last或一段的最后位置大，无视它继续往后找。
如果比刚才的大，说明这一段的分隔位置必须往后移动，所以我们把last或一段的最后位置更新为当前的字母的最后位置。
3，肯定到有一个时间，这个last就更新不了了，那么这个时候这个位置就是我们的分隔位置。
注意题目要分隔后的长度，我们就用last - startindex + 1。
4，找到一个分割位，更新一下起始位置，同理搜索就行了。
"""

# ==================== 代码实现 ====================
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic = {s: index for index, s in enumerate(S)}  # 存储某个字母对应地最后一个序号
        num = 0  # 直接计数
        result = []
        j = dic[S[0]]  # 第一个字符的最后位置
        for i in range(len(S)):  # 逐个遍历
            num += 1  # 找到一个就加1个长度
            if dic[S[i]] > j:  # 思路一样，如果最后位置比刚才的大，就更新最后位置
                j = dic[S[i]]
            if i == j:  # 思路一样，形式不同，这里就是找到这一段的结束了，就说明当前位置的index和这个字母在字典里的最后位置应该是相同的。
                result.append(num)  # 加入result
                num = 0  # 归0
        return result

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
