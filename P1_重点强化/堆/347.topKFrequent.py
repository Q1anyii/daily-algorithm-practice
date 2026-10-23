"""
题目：347. 前 K 个高频元素 (topKFrequent)
难度：中等
分类：堆
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个整数数组 nums 和一个整数 k，请你返回其中出现频率前 k 高的元素。你可以按任意顺序返回答案。

示例 1：
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2：
输入: nums = [1], k = 1
输出: [1]
"""


# ==================== 解题思路 ====================
"""
前k高，那么其实堆存储的就应该是长度，而非数字本身？同时还需要记录每个数的出现次数，那就用一个dict封装？
"""

# ==================== 代码实现 ====================
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # from collections import defaultdict
        # import heapq
        # dict_ = defaultdict(int)
        # for n in nums:
        #     dict_[n] += 1
        #
        # heap = [(v, num) for num, v in list(dict_.items())[:k]]
        # heapq.heapify(heap)
        # for num, v in list(dict_.items())[k:]:  # ③ 只遍历剩下的候选
        #     if v > heap[0][0]:
        #         heapq.heapreplace(heap, (v, num))
        # return [num for _, num in heap]  # ⑤ 取数字（元组第二个元素）

        from collections import Counter
        import heapq
        freq = Counter(nums)
        heap = [(v, num) for num, v in list(freq.items())[:k]]
        heapq.heapify(heap)
        # for (num, v) in list(freq.items())[k:]:
        #     if v > heap[0][0]:
        #         heapq.heapreplace(heap, (num, v))
        return [num for num, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sorted(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert sol.topKFrequent([1], 1) == [1]
    assert sorted(sol.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2)) == [-1, 2]
    assert sorted(sol.topKFrequent([1, 2], 2)) == [1, 2]
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
