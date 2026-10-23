"""
题目：169. 多数元素 (majorityElement)
难度：简单
分类：排序
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个大小为 n 的数组 nums，返回其中的多数元素。多数元素是指在数组中出现次数大于 ⌊n/2⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1：
输入：nums = [3,2,3]
输出：3

示例 2：
输入：nums = [2,2,1,1,1,2,2]
输出：2
"""


# ==================== 解题思路 ====================
"""
**"候选人 + 票数抵消"**：
维护一个 `candidate` 和一个 `count`。遍历时，
`count == 0` 就重新立当前元素为候选人；
当前元素 == 候选人就 `count += 1`，否则 `count -= 1`。
抵消到最后，还站着的那个候选人，才是众数。
"""

# ==================== 代码实现 ====================
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0
        for n in nums:
            if count == 0:
                candidate = n
            if n == candidate:
                count += 1
            else:
                count -= 1
        return candidate


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.majorityElement([3, 2, 3]) == 3
    assert sol.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert sol.majorityElement([1]) == 1
    assert sol.majorityElement([1, 1, 2]) == 1
    assert sol.majorityElement([-1, -1, 2, -1]) == -1
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
