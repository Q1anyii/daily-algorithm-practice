"""
题目：215. 数组中的第 K 个最大元素 (findKthLargest)
难度：中等
分类：堆
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：
输入: [3,2,1,5,6,4], k = 2
输出: 5

示例 2：
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
"""

# ==================== 解题思路 ====================
"""
**小顶堆，固定大小为 k。** 维护 "**目前见过的最大 k 个数**" 这个堆，堆顶（堆里最小的那个）就是**第 k 大**。
"""

# ==================== 代码实现 ====================
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = nums[:k]
        heapq.heapify(heap)
        for x in nums[k:]:
            if x > heap[0]:  # 新数比堆顶（当前第 k 大）大 → 挤进前 k
                heapq.heapreplace(heap, x)
        return heap[0]

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert sol.findKthLargest([1], 1) == 1
    assert sol.findKthLargest([-1, -1], 2) == -1
    assert sol.findKthLargest([5, 2, 4, 1, 3, 6, 0], 4) == 3
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
