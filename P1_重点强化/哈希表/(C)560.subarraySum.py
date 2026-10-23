"""
题目：560. 和为 K 的子数组 (subarraySum)
难度：中等
分类：哈希表
"""
from collections import defaultdict
from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个整数数组 nums 和一个整数 k，请你统计并返回该数组中和为 k 的子数组的个数。
子数组是数组中元素的连续非空序列。

示例 1：
输入：nums = [1,1,1], k = 2
输出：2

示例 2：
输入：nums = [1,2,3], k = 3
输出：2
"""


# ==================== 解题思路 ====================
"""
和为k的子数组个数， 依次遍历？

m2:核心：不枚举所有子数组，利用前缀和公式，用哈希表记录前缀和出现次数，时间复杂度 O (n)。
    累加pre_sum, 
    找pre_sum-k 是否在map中， 如果存在,那就说明数组中
    
    前缀和 - 前面的某个前缀和 = 这段区间的和
    
"和为 k 的子数组个数 = 所有 ' 前缀和之差为 k' 的 (i, j) 对数"
—— 每个 j 只统计以它结尾的答案，前缀和相同的历史出现次数直接累加，所以不重不漏。
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        pre_sum = 0
        mp = defaultdict(int)
        mp[0] = 1
        for n in nums:
            pre_sum += n
            #"map 里有没有出现过 `当前前缀和 - k`"
            # =
            # " 有没有某个起点 i，使得从 i 到当前 j 的子数组和为 k"；
            # 出现几次，就是几个以 j 结尾的答案。
            if pre_sum - k in mp:
                count += mp[pre_sum - k]
            mp[pre_sum] += 1
        return count

        # n = 0
        # for i in range(len(nums)):
        #     sum_ = 0
        #     for j in range(i, len(nums)):
        #         sum_ += nums[j]
        #         if sum_ == k:
        #             n += 1
        # return n


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.subarraySum([1, 1, 1], 2) == 2
    assert sol.subarraySum([1, 2, 3], 3) == 2
    assert sol.subarraySum([1, -1, 0], 0) == 3
    assert sol.subarraySum([-1, -1, 1], 0) == 1
    assert sol.subarraySum([1], 1) == 1
    assert sol.subarraySum([1], 0) == 0
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
