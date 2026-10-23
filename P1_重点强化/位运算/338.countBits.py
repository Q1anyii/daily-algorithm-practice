"""
题目：338. 比特位计数 (countBits)
难度：简单
分类：位运算
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个整数 n，对于每个 i（0 <= i <= n），计算其二进制表示中 1 的个数，返回一个长度为 n + 1 的数组 ans 作为答案。

示例 1：
输入：n = 2
输出：[0,1,1]
解释：
0 --> 0 (0 个 1)
1 --> 1 (1 个 1)
2 --> 10 (1 个 1)

示例 2：
输入：n = 5
输出：[0,1,1,2,1,2]
"""


# ==================== 解题思路 ====================
"""
解法一：复杂度O（nlogn）
先转为二进制数组，然后取1的个数
十进制转二进制公式： 除以二取余，直到余数为1（直接加），或0

解法二：O（n）

"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        # ans = []
        # for i in range(n + 1):
        #     count = 0
        #     while i:
        #         if i & 1 == 1:
        #             count += 1
        #         i >>= 1
        #     ans.append(count)
        # return ans
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.countBits(2) == [0, 1, 1]
    assert sol.countBits(5) == [0, 1, 1, 2, 1, 2]
    assert sol.countBits(0) == [0]
    assert sol.countBits(1) == [0, 1]
    assert sol.countBits(10) == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
